from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Page

# Para trabajar con formularios
from .forms import PageForm


class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario sea miembro del staff

    # Este no utiliza decoradores
    # def dispatch(self, request, *args, **kwargs):
    #     # print(request.user)
    #     if not request.user.is_staff:
    #         return redirect(reverse_lazy('admin:login'))
    #     return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)    """

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


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


# class PageCreate(CreateView):
# Para obligarlo a que sea un usuario del staff, heredamos del mixins StaffRequiredMixin
# class PageCreate(StaffRequiredMixin, CreateView):
# Aqui ya no utilizo el mixin, utilizo el decorador para comprobar si el usuario es staff

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    # Para trabajar con formularios
    form_class = PageForm

    # Lo quitamos porque en el formulario ya estan los formularios
    # fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')

    # Para no tener que sobreescribir el metodo su usa el reverse_lazy
    # def get_success_url(self):
    #     return reverse('pages:pages')

    # Para agregar segurdad, que solo acceda usuario auditado y miembro del staf El método de envío toma la solicitud
    # y finalmente devuelve la respuesta. Normalmente, devuelve una respuesta llamando(es decir, enviando a) otro
    # método como get.Piense en ello como un intermediario entre solicitudes y respuestas.
    # Utilizamos un mixing para no tener que sobreecribir en todas las vistas que necesite logearse

    # Un Mixin es una implementación de una o varias funcionalidades para una clase, podemos crearlo una vez y heredar
    # su comportamiento donde queramos dándole prioridad a su implementación antes que la de otra clase.

    # def dispatch(self, request, *args, **kwargs):
    #     # print(request.user)
    #     if not request.user.is_staff:
    #         return redirect(reverse_lazy('admin:login'))
    #     return super(PageCreate, self).dispatch(request, *args, **kwargs)


# Para obligarlo a que sea un usuario del staff, heredamos del mixins StaffRequiredMixin
# class PageUpdate(UpdateView):
# Aqui ya no utilizo el mixin, utilizo el decorador para comprobar si el usuario es staff
# class PageUpdate(StaffRequiredMixin, UpdateView):

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    # Para trabajar con formularios
    form_class = PageForm

    # Lo quitamos porque en el formulario ya estan los formularios
    # fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'

    # Podriamos redireccionar a la lista de paginas, pero si queremos mostrar el que acabamos de editar
    # Necesitamos el id, paro solo lo tendremos disponible en algun metodo, para tener disponible self.objects
    # que es la variable que esta gestionando el objeto interno, la instancia
    # success_url = reverse_lazy('pages:pages')

    def get_success_url(self):
        # return reverse_lazy('pages:update', args=[self.object.id])
        # Para saber si edito bien podemos concatenar un ok
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


# Para obligarlo a que sea un usuario del staff, heredamos del mixins StaffRequiredMixin
# class PageDeleteView(DeleteView):

# Aqui ya no utilizo el mixin, utilizo el decorador para comprobar si el usuario es staff
# class PageDeleteView(StaffRequiredMixin, DeleteView):

@method_decorator(staff_member_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
