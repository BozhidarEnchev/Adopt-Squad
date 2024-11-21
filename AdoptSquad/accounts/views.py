from django.contrib.auth import login, get_backends
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from AdoptSquad.accounts.forms import AppUserAuthenticationForm, AppUserCreationForm
from AdoptSquad.accounts.models import AppUser


class AppUserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AppUserAuthenticationForm

    def form_valid(self, form):
        """Override form_valid to explicitly set the backend."""
        user = form.get_user()

        backend = next(
            (backend for backend in get_backends() if hasattr(backend, 'authenticate')),
            None
        )
        if backend:
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"

        login(self.request, user)
        return super().form_valid(form)


class AppUserRegisterView(CreateView):
    model = AppUser
    form_class = AppUserCreationForm
    template_name = 'accounts/account-register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(request=self.request, user=self.object, backend='AdoptSquad.accounts.backends.EmailOrUsernameBackend')

        return response
