from django.urls import path
from . import views

app_name = 'recipe_crud'

urlpatterns = [
    path('', views.PostListView.as_view(),name='list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name="detail"),
    path('create/',views.CreatePostView.as_view(),name='create'),
    path('update/<int:pk>/',views.PostUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.PostDeleteView.as_view(),name='delete'),
]
