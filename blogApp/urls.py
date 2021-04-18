from django.urls import path
from . import views

from .views import NewPost, AllPost, DetailPost, UpdatePost, DeletePost

urlpatterns = [
    path('', AllPost.as_view(), name='index'),
    path('post/<int:pk>', DetailPost.as_view(), name='detailPost'),
    path('new-post', NewPost.as_view(), name='newpost'),
    path('post/<int:pk>/update', UpdatePost.as_view(), name='updatePost'),
    path('post/<int:pk>/delete', DeletePost.as_view(), name='deletePost'),
]
