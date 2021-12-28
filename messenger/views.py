from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Para generar la respuesta json
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404

from messenger.models import Thread, Message


# class ThreadList(ListView):
#     # Se Sobreescribe la queryset para que solo me traiga los hilos de un usuario,
#     # pero en realidad no me hace falta porque existe una relacion inversa user.thread.all(), por lo tanto
#     # todos lo que hicimos no nos hace falta
#     # model = Thread
#
#     # def get_queryset(self):
#     #     queryset = super(ThreadList, self).get_queryset()
#     #     return queryset.filter(users=self.request.user)


@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"


@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread

    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj


def add_message(request, pk):
    print(request.GET)
    # El diccionario que devuelve la peticion asincronica
    json_response = {'created': False}
    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
            # Para verificar si es el primer mensaje y recargar la pagina
            if len(thread.messages.all()) is 1:
                json_response['first'] = True
    else:
        raise Http404("Usuario no autenticado")

    return JsonResponse(json_response)


@login_required
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    theard = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[theard.pk]))
