from ntapi.models import Species
from ntapi.serializers import SpeciesSerializer
from rest_framework import generics

class SpeciesList(generics.ListCreateAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class SpeciesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class SpeciesDetail_name(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Species.objects.filter(common_name='common_name')
    queryset = Species.objects.all()
    lookup_field = 'common_name'
    serializer_class = SpeciesSerializer