from django.urls import path, include

from AdoptSquad.forum.views import PostDashboard, PostCreateView, PostDetailView, PostDeleteView, CommentCreateView, \
    CommentDeleteView

urlpatterns = [
    path('', PostDashboard.as_view(), name='post-dashboard'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', include([
        path('',  PostDetailView.as_view(), name='post-detail'),
        path('delete/', PostDeleteView.as_view(), name='post-delete'),
        path('comment/', include([
            path('', CommentCreateView.as_view(), name='comment'),
        ]))
    ])),
    path('comments/<int:pk>/', include([
        path('delete/', CommentDeleteView.as_view(), name='comment-delete'),
    ])),
]
