# jobs/urls.py
from django.urls import path
from .views import job_list, job_create, job_update, job_delete
from . import views

urlpatterns = [
    path('meet_team/', views.meet_team, name='meet_team'),
    path('contact/', views.contact, name='contact'),
    path('', job_list, name='job_list'),
    path('create/', job_create, name='job_create'),
    path('update/<int:pk>/', job_update, name='job_update'),
    path('delete/<int:pk>/', job_delete, name='job_delete'),
]
