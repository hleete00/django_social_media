from django.urls import path
from . import views

app_name = 'group'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='list-group'),
    path('new/', views.CreateGroup.as_view(), name='create-group'),
    path('post/in/<slug:slug>/', views.SingleGroup.as_view(), name='single-group'),
    path('join/<str:slug>', views.JoinGroup.as_view(), name='join-group'),
    path('leave/<str:slug>', views.LeaveGroup.as_view(), name='leave-group'),
]
