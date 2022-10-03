from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.PostList.as_view(), name='list-post'),
    path('new/', views.CreatePost.as_view(), name='create-post'),
    path('by/<str:username>/', views.UserPosts.as_view(), name='for-user'),
    path('by/<str:username>/<int:pk>/', views.PostDetail.as_view(), name='single-post'),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete-post'),
]