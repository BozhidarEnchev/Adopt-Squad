from django.contrib.auth.views import LogoutView
from django.urls import path, include

from AdoptSquad.accounts.views import AppUserLoginView, AppUserRegisterView, AppUserDetailsView, AppUserUpdateView, \
    AppUserDeleteView

urlpatterns = [
    path('login/', AppUserLoginView.as_view(), name='login'),
    path('register/', AppUserRegisterView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('', AppUserDetailsView.as_view(), name='user details'),
        path('edit/', AppUserUpdateView.as_view(), name='user update'),
        path('delete/', AppUserDeleteView.as_view(), name='user delete'),
    ])),
]
