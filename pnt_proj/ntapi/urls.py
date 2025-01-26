from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ntapi import views

urlpatterns = [
    path('ntapi/', views.SpeciesList.as_view()),
    path('ntapi/<str:lu_field>=<str:lu_value>/', views.SpeciesDetail.as_view(), name='species_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)