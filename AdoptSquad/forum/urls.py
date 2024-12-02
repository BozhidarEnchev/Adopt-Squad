from django.urls import path, include

from AdoptSquad.forum.views import PostDashboard

urlpatterns = [
    path('', PostDashboard.as_view(), name='post-dashboard'),
]
