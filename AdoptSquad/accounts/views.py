from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from AdoptSquad.accounts.forms import AppUserCreationForm
from AdoptSquad.accounts.models import AppUser


class AppUserLoginView(LoginView):
    template_name = 'accounts/login.html'


class AppUserRegisterView(CreateView):
    model = AppUser
    form_class = AppUserCreationForm
    template_name = 'accounts/account-register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(request=self.request, user=self.object)

        return response
