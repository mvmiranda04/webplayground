from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Page


# Vistas basadas en funciones
# # Create your views here.
# def pages(request):
#     pages = get_list_or_404(Page)
#     return render(request, 'pages/pages.html', {'pages': pages})
#
#
# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/page.html', {'page': page})

# Vistas basadas en clases

class PagesListView(ListView):
    model = Page


class PagesDetailView(DetailView):
    model = Page


class PageCreate(CreateView):
    model = Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')

    # Para no tener que sobreescribir el metodo su usa el reverse_lazy
    # def get_success_url(self):
    #     return reverse('pages:pages')


class PageUpdate(UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'

    # Podriamos redireccionar a la lista de paginas, pero si queremos mostrar el que acabamos de editar
    # Necesitamos el id, paro solo lo tendremos disponible en algun metodo, para tener disponible self.objects
    # que es la variable que esta gestionando el objeto interno, la instancia
    # success_url = reverse_lazy('pages:pages')

    def get_success_url(self):
        # return reverse_lazy('pages:update', args=[self.object.id])
        # Para saber si edito bien podemos concatenar un ok
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
