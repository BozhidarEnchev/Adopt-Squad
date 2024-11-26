from django.urls import path, include

from AdoptSquad.pets.views import CatsDashboard, DogsDashboard, CatsCreateView, DogsCreateView, CatsUpdateView, \
    DogsUpdateView, CatsDetailView, DogsDetailView, DogsDeleteView, CatsDeleteView

urlpatterns = [
    path('cats/', include([
        path('', CatsDashboard.as_view(), name='cats-list'),
        path('register/', CatsCreateView.as_view(), name='cats-register'),
        path('<int:pk>/', include([
            path('edit/', CatsUpdateView.as_view(), name='cats-edit'),
            path('delete/', CatsDeleteView.as_view(), name='cats-delete'),
            path('details/', CatsDetailView.as_view(), name='cats-details'),
        ]))
    ])),
    path('dogs/', include([
        path('', DogsDashboard.as_view(), name='dogs-list'),
        path('register/', DogsCreateView.as_view(), name='dogs-register'),
        path('<int:pk>/', include([
            path('edit/', DogsUpdateView.as_view(), name='dogs-edit'),
            path('delete/', DogsDeleteView.as_view(), name='dogs-delete'),
            path('details/', DogsDetailView.as_view(), name='dogs-details'),
        ]))
    ])),
]
