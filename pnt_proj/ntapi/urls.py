from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ntapi import views

urlpatterns = [
    path('ntapi/', views.SpeciesList.as_view()),
    path('ntapi/id=<int:pk>/', views.SpeciesDetail.as_view()),
    path('ntapi/name=<str:common_name>/', views.SpeciesDetail_name.as_view(), name='common_name'),
    path('ntapi/species=<str:species>/', views.SpeciesDetail_species.as_view(), name='species'),
    path('ntapi/family=<str:family>/', views.SpeciesDetail_family.as_view(), name='family'),
    path('ntapi/classification=<str:ecological_classification>/', views.SpeciesDetail_classification.as_view(), name='ecological_classification'),
    path('ntapi/status=<str:conservation_status>/', views.SpeciesDetail_status.as_view(), name='conservation_status'),
    path('ntapi/binhi_priority=<str:binhi_priority>/', views.SpeciesDetail_binhi.as_view(), name='binhi_priority')
]

urlpatterns = format_suffix_patterns(urlpatterns)