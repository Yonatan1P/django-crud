from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('new/', BlogCreateView.as_view(), name='blog_create'),
    path('new/', BlogDeleteView.as_view(), name='blog_delete'),
]