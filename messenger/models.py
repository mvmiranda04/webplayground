from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import m2m_changed


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class ThreadManager(models.Manager):
    def find(self, user1, user2):
        queryset = self.filter(users=user1).filter(users=user2)
        if len(queryset) > 0:
            return queryset[0]
        return None

    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread


class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)

    objects = ThreadManager()


# instance: La instancia que manda la señal, es decir el hilo al que estamos intentando enviar los mensajes action:
# la accion que se esta ejecutando- pre_add o post_add pk_set: que hace referencia a un conjunto que almace  todos
# los identificadores de los mensajes que se van a añadir en este manytomany
def messages_changed(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    action = kwargs.pop('action', None)
    pk_set = kwargs.pop('pk_set', None)
    print(instance, action, pk_set)
    false_pk_set = set()
    if action is "pre_add":
        for mgs_pk in pk_set:
            msg = Message.objects.get(pk=mgs_pk)
            if msg.user not in instance.users.all():
                print("Ups, ({}) no forma para del hilo".format(msg.user))
                false_pk_set.add(mgs_pk)

        # Buscar los mensajes si si estan en fals_pk_set y los borramos de pk_set
        # Resta los que estan en false_pk_set los resta de pk_set
        pk_set.difference_update(false_pk_set)


# Para conectar la señal con cualquier cambio que suceda en el campo message
m2m_changed.connect(messages_changed, sender=Thread.messages.through)
