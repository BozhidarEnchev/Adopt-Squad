from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from AdoptSquad.accounts.models import AppUser


class AppUserPermissionMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        appuser = get_object_or_404(AppUser, pk=self.kwargs['pk'])
        return self.request.user == appuser

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('home'))