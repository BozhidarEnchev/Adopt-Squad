from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from AdoptSquad.forum.forms import PostCreateForm
from AdoptSquad.forum.models import Post


class PostDashboard(ListView):
    model = Post
    template_name = 'forum/post-dashboard.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'forum/post-create-form.html'
    success_url = reverse_lazy('post-dashboard')
    form_class = PostCreateForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/post-detail.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'forum/post-confirm-delete.html'
    success_url = reverse_lazy('post-dashboard')
