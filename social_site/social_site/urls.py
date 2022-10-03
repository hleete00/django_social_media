from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('account/', include('account.urls', namespace='account')),
    path('account/', include('django.contrib.auth.urls')),
    path('group/', include('group.urls', namespace='group')),
    path('post/', include('post.urls', namespace='post')),
]
