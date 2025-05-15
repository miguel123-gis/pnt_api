from . import views
from django.urls import path, re_path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('ntapi/', views.SpeciesList.as_view()),
    re_path(r"^ntapi/(?P<filters>(\w+:[\w\s]+/?)*)$", views.SpeciesDetail.as_view(), name="species_detail"),
    re_path(r"^test/(?P<latlon>-?\d+\.\d+,-?\d+\.\d+)/$", views.TestView.as_view(), name="test"),
]

urlpatterns = format_suffix_patterns(urlpatterns)