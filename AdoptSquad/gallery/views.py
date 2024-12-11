from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from AdoptSquad.gallery.forms import PhotoCreateForm, SearchBarForm
from AdoptSquad.gallery.models import Photo


class PhotoDashboard(ListView):
    model = Photo
    context_object_name = 'photos'
    template_name = 'gallery/photo-dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['search_bar'] = SearchBarForm(self.request.GET)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        pet = self.request.GET.get('pet')

        if pet:
            queryset = queryset.filter(pets__name__icontains=pet)

        return queryset


class PhotoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Photo
    success_url = reverse_lazy('gallery')
    form_class = PhotoCreateForm
    template_name = 'gallery/photo-create-form.html'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('gallery'))
