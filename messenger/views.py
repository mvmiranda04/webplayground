from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from messenger.models import Thread
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404


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
