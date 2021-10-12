# Transformo Vistas basadas en funciones en vistas basadas en clases
# from django.shortcuts import render
#
#
# def home(request):
#     return render(request, "core/home.html")
#
#
# def sample(request):
#     return render(request, "core/sample.html")

from django.views.generic.base import TemplateView

from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    # ** kwargs (argumentos en clave y valor)/  No lo mando en el diccionario de contexto lo mando con el metodo Get
    # def get_context_data(self, **kwargs):
    #     # Recuperamos el diccionario de contexto de super
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = "Mi Super Web Playground"
    #     return context

    # La respuesta de las vistas se hace en el metodo Get
    # Como buenas practicas enviar argumentos, y argumentos en clave y valor
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': "Mi Super Web Playground"})


class SamplePageView(TemplateView):
    template_name = 'core/sample.html'
