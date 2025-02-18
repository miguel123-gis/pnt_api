from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from ntapi import views

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('ntapi/', views.SpeciesList.as_view()),
    re_path(r"^ntapi/(?P<filters>(\w+:[\w\s]+/?)*)$", views.SpeciesDetail.as_view(), name="species_detail")
]

# TODO Use custom path converters
# Return the filter as dict and process accordingly in views
urlpatterns = format_suffix_patterns(urlpatterns)