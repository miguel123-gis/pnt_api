from django.urls import path
from ntapi import views

urlpatterns = [
    path('ntapi/', views.species_list),
    path('ntapi/<int:pk>/', views.species_detail),
]