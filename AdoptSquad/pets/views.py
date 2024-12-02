from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from AdoptSquad.pets.forms import CatCreateForm, DogCreateForm, DogUpdateForm, CatUpdateForm
from AdoptSquad.pets.models import Cat, Dog


class CatsDashboard(ListView):
    model = Cat
    template_name = 'pets/pet-dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_type'] = 'cat'

        return context


class DogsDashboard(ListView):
    model = Dog
    template_name = 'pets/pet-dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_type'] = 'dog'

        return context


class CatsCreateView(CreateView):
    model = Cat
    template_name = 'pets/pet-form.html'
    form_class = CatCreateForm
    success_url = reverse_lazy('cats-list')


class DogsCreateView(CreateView):
    model = Dog
    template_name = 'pets/pet-form.html'
    form_class = DogCreateForm
    success_url = reverse_lazy('dogs-list')


class CatsUpdateView(UpdateView):
    model = Cat
    template_name = 'pets/pet-form.html'
    form_class = CatUpdateForm

    def get_success_url(self):
        return reverse_lazy('dogs-details', kwargs={'pk': self.object.pk})


class DogsUpdateView(UpdateView):
    model = Dog
    template_name = 'pets/pet-form.html'
    form_class = DogUpdateForm

    def get_success_url(self):
        return reverse_lazy('dogs-details', kwargs={'pk': self.object.pk})


class CatsDeleteView(DeleteView):
    model = Cat
    success_url = reverse_lazy('cats-list')
    template_name = 'pets/pet-confirm-delete.html'


class DogsDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy('dogs-list')
    template_name = 'pets/pet_confirm_delete.html'


class CatsDetailView(DetailView):
    model = Cat
    template_name = 'pets/pet-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_type'] = 'cat'

        return context


class DogsDetailView(DetailView):
    model = Dog
    template_name = 'pets/pet-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_type'] = 'dog'

        return context
