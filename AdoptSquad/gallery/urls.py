from django.urls import path, include

from AdoptSquad.gallery.views import PhotoDashboard, PhotoCreateView

urlpatterns = [
    path('', PhotoDashboard.as_view(), name='gallery'),
    path('create/', PhotoCreateView.as_view(), name='photo-create'),
]
