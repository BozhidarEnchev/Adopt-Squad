from django.contrib.auth import login, get_backends
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from AdoptSquad.accounts.forms import AppUserAuthenticationForm, AppUserCreationForm, AppUserChangeForm
from AdoptSquad.accounts.mixins import AppUserPermissionMixin
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


class AppUserDetailsView(LoginRequiredMixin, DetailView):
    model = AppUser
    template_name = 'accounts/account-details.html'


class AppUserUpdateView(AppUserPermissionMixin, UpdateView):
    model = AppUser
    template_name = 'accounts/account-edit.html'
    form_class = AppUserChangeForm

    def get_success_url(self):
        return reverse_lazy('user details', kwargs={'pk': self.request.user.pk})


class AppUserDeleteView(AppUserPermissionMixin, DeleteView):
    model = AppUser
    success_url = reverse_lazy('home')
    template_name = 'accounts/user-confirm-delete.html'
