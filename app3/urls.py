from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path
from .views import upload_file
from .views import login, dashboard, upload_file, upload_success, delete_file
urlpatterns=[
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('upload/', upload_file, name='upload_file'),
    path('upload/success/', upload_success, name='upload_success'),
    path('delete_file/<int:file_id>/', delete_file, name='delete_file'),
    
]
