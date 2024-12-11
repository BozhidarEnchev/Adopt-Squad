from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from AdoptSquad.pets.forms import CatCreateForm, DogCreateForm, DogUpdateForm, CatUpdateForm
from AdoptSquad.pets.mixins import CatBaseViewMixin, DogBaseViewMixin, DogPermissionMixin, CatPermissionMixin
from AdoptSquad.pets.models import Cat, Dog


class CatsDashboard(CatBaseViewMixin, ListView):
    model = Cat
    template_name = 'pets/pet-dashboard.html'


class DogsDashboard(DogBaseViewMixin, ListView):
    model = Dog
    template_name = 'pets/pet-dashboard.html'


class CatsCreateView(CatPermissionMixin, CreateView):
    model = Cat
    template_name = 'pets/pet-form.html'
    form_class = CatCreateForm
    success_url = reverse_lazy('cats-list')


class DogsCreateView(DogPermissionMixin, CreateView):
    model = Dog
    template_name = 'pets/pet-form.html'
    form_class = DogCreateForm
    success_url = reverse_lazy('dogs-list')


class CatsUpdateView(CatPermissionMixin, UpdateView):
    model = Cat
    template_name = 'pets/pet-form.html'
    form_class = CatUpdateForm

    def get_success_url(self):
        return reverse_lazy('dogs-details', kwargs={'pk': self.object.pk})


class DogsUpdateView(DogPermissionMixin, UpdateView):
    model = Dog
    template_name = 'pets/pet-form.html'
    form_class = DogUpdateForm

    def get_success_url(self):
        return reverse_lazy('dogs-details', kwargs={'pk': self.object.pk})


class CatsDeleteView(CatPermissionMixin, CatBaseViewMixin, DeleteView):
    model = Cat
    success_url = reverse_lazy('cats-list')
    template_name = 'pets/pet-confirm-delete.html'


class DogsDeleteView(DogPermissionMixin, DogBaseViewMixin, DeleteView):
    model = Dog
    success_url = reverse_lazy('dogs-list')
    template_name = 'pets/pet-confirm-delete.html'


class CatsDetailView(CatBaseViewMixin, DetailView):
    model = Cat
    template_name = 'pets/pet-details.html'


class DogsDetailView(DogBaseViewMixin, DetailView):
    model = Dog
    template_name = 'pets/pet-details.html'
