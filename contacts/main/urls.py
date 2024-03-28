from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.add_client, name='add_client'),
    path('clients/edit/<int:id>/', views.edit_client, name='edit_client'),
    path('clients/delete/<int:id>/', views.delete_client, name='delete_client'),
]