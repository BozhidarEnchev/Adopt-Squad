from django.views.generic import ListView
from AdoptSquad.forum.models import Post


class PostDashboard(ListView):
    model = Post
    template_name = 'forum/post-dashboard.html'
