from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from AdoptSquad.gallery.forms import PhotoCreateForm
from AdoptSquad.gallery.models import Photo


class PhotoDashboard(ListView):
    model = Photo
    context_object_name = 'photos'
    template_name = 'gallery/photo-dashboard.html'


class PhotoCreateView(CreateView):
    model = Photo
    success_url = reverse_lazy('gallery')
    form_class = PhotoCreateForm
    template_name = 'gallery/photo-create-form.html'
