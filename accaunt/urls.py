from django.urls import path
from .views import (AllView,
                    DetailView,
                    UpdateView,
                    CreateView,
                    DeleteView,
                    View,
                    )


urlpatterns = [
    path('get_all/',AllView.as_view(),name='get_all'),
    path('get_by_id/<int:pk>/',DetailView.as_view(),name='detail'),
    path('update/<int:pk>/',UpdateView.as_view(),name='update'),
    path('create/',CreateView.as_view(),name='create'),
    path('delete/<int:pk>/',DeleteView.as_view(),name='delete'),
    path('by/<int:id>/',View.as_view(),name='by')
]


