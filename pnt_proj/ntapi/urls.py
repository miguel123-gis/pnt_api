from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ntapi import views

urlpatterns = [
    path('ntapi/', views.SpeciesList.as_view()),
    path('ntapi/<str:common_name>/', views.SpeciesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)