from functools import reduce
import operator
from ntapi.models import Species
from ntapi.serializers import SpeciesSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
from django.http import JsonResponse


field_mappings = SpeciesSerializer.field_mappings

class SpeciesList(generics.ListAPIView):
    queryset = Species.objects.all().order_by('id')
    serializer_class = SpeciesSerializer

class SpeciesDetail(generics.ListAPIView):
    serializer_class = SpeciesSerializer  

    @staticmethod
    def get_alt_fieldname(field):
        if field in field_mappings:
            field = field_mappings[field]
            return field
        return field
    
    def get_queryset(self):
        queryset = Species.objects.all()
        return queryset
    
    @staticmethod
    def filter_queryset(queryset, filters, condition):
        queries = [Q(**{f"{key}__iexact": value}) for key, value in filters.items()]

        queryset = \
            queryset.filter( \
            reduce( \
                operator.or_ if condition=='or' else operator.and_, \
                queries
        ))
        
        return queryset
        

    def get(self, request, filters=None):
        queryset = self.get_queryset()
        filter_dict = {} 

        if filters:
            filter_pairs = filters.strip("/").split("/")
            for pair in filter_pairs:
                key, value = pair.split(":", 1)
                key = self.get_alt_fieldname(key)
                filter_dict[key] = value
            
            
            queryset = self.filter_queryset(queryset=queryset, filters=filter_dict, condition='and')
            serializer = self.get_serializer(queryset, many=True)
            
            return Response({
                "results": len(serializer.data),
                "data": serializer.data
            })