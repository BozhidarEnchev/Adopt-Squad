from django.contrib.auth.views import LogoutView
from django.urls import path, include

from AdoptSquad.accounts.views import AppUserLoginView, AppUserRegisterView

urlpatterns = [
    path('login/', AppUserLoginView.as_view(), name='login'),
    path('register/', AppUserRegisterView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
