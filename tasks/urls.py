from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'tasks'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('home/', views.home, name='home'),
    path('create/', views.create_task, name='create'),
    path('update/<int:pk>/', views.update_task, name='update'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
    path('date/<str:selected_date>/', views.tasks_by_date, name='tasks_by_date'),
    path('register/', views.register, name='register'),
]