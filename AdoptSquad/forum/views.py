from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from AdoptSquad.forum.forms import PostCreateForm, CommentCreateForm
from AdoptSquad.forum.models import Post, Comment


class PostDashboard(ListView):
    model = Post
    template_name = 'forum/post-dashboard.html'


class PostCreateView(LoginRequiredMixin, CreateView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentCreateForm()
        return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'forum/post-confirm-delete.html'
    success_url = reverse_lazy('post-dashboard')

    def test_func(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return self.request.user == post.author or self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('post-dashboard'))


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        if form.is_valid():
            comment.author = self.request.user
            comment.post = Post.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'forum/comment-confirm-delete.html'

    def get_success_url(self):
        context = self.get_context_data()
        return reverse_lazy('post-detail', kwargs={'pk': context['comment'].post.pk})

    def test_func(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        return self.request.user == comment.author or self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('post-dashboard'))
