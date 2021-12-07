from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
# Lo comento porque ya no muestra un un template, ahora tiene que modificarlo
# from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from .models import Profile


class SignUpView(CreateView):
    # Ya no usamo UserCreationForm para usar el que agrega el email
    # form_class = UserCreationForm
    form_class = UserCreationFormWithEmail

    # Lo comenta para concatenarle un variale que se registro exitosamente
    # success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Mofificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre '
                                                                                                             'de '
                                                                                                             'usuario'})
        # Agregamos el campo email
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Direccion '
                                                                                                           'de email'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Repite Contraseña'})

        return form


# Ahora ya no muestra solo el template, ahora lo editha
# class ProfileUpdate(TemplateView):
#     template_name = 'registration/profile_form.html'

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    # Borramos el model porque viene del formulario
    # model = Profile
    # Como utilizamos formularios lo sacamos de aqui
    # fields = ['avatar', 'bio', 'link']
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    # No podemos hacer esto: return Profile.objects.get_or_create(user=self.request.user)
    # porque devuelve una tupla
    # Recupera el objeto que se va a editar
    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    # Recupera el objeto que se va a editar
    def get_object(self, queryset=None):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Mofificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        return form