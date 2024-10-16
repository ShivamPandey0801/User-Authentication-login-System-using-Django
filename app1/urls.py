from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home page'),
    path('profile',views.profile, name='profile page'),
    path('expression',views.expression, name='expression value')
]