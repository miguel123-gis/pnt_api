from ntapi.models import Species
from ntapi.serializers import SpeciesSerializer
from rest_framework import generics

class SpeciesList(generics.ListAPIView):
    queryset = Species.objects.all().order_by('id')
    serializer_class = SpeciesSerializer

class SpeciesDetail(generics.ListAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class SpeciesDetail_name(generics.ListAPIView):
    serializer_class = SpeciesSerializer    

    def get_queryset(self):
        queryset = Species.objects.filter()
        common_name = self.kwargs['common_name']
        if common_name is not None:
            queryset = queryset.filter(common_name__iexact=common_name)
        return queryset

class SpeciesDetail_species(generics.ListAPIView):
    serializer_class = SpeciesSerializer

    def get_queryset(self):
        queryset = Species.objects.filter()
        species = self.kwargs['species']
        if species is not None:
            queryset = queryset.filter(species__iexact=species)
        return queryset

class SpeciesDetail_family(generics.ListAPIView):
    serializer_class = SpeciesSerializer

    def get_queryset(self):
        queryset = Species.objects.all()
        family = self.kwargs['family']
        if family is not None:
            queryset = queryset.filter(family__iexact=family)
        return queryset

class SpeciesDetail_classification(generics.ListAPIView):
    serializer_class = SpeciesSerializer

    def get_queryset(self):
        queryset = Species.objects.all()
        eco_class = self.kwargs['ecological_classification']
        if eco_class is not None:
            queryset = queryset.filter(ecological_classification=eco_class)
        return queryset

class SpeciesDetail_status(generics.ListAPIView):
    serializer_class = SpeciesSerializer

    def get_queryset(self):
        queryset = Species.objects.all()
        con_status = self.kwargs['conservation_status']
        if con_status is not None:
            queryset = queryset.filter(conservation_status=con_status)
        return queryset

class SpeciesDetail_binhi(generics.ListAPIView):
    serializer_class = SpeciesSerializer

    def get_queryset(self):
        queryset = Species.objects.all()
        binhi_prio = self.kwargs['binhi_priority']
        if binhi_prio is not None:
            queryset = queryset.filter(binhi_priority=binhi_prio)
        return queryset
