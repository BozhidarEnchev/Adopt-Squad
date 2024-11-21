from django.urls import path

from AdoptSquad.accounts.views import AppUserLoginView, AppUserRegisterView

urlpatterns = [
    path('accounts/', AppUserLoginView.as_view(), name='login'),
    path('accounts/', AppUserRegisterView.as_view(), name='registration'),
]