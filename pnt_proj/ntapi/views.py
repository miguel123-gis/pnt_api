from ntapi.models import Species
from ntapi.serializers import SpeciesSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SpeciesList(APIView):
    # List all species, or add a new species

    def get(request, format=None):
        species = Species.objects.all()
        serializer = SpeciesSerializer(species, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SpeciesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpeciesDetail(APIView):
        # Retreive, update, or delete a species
    def get_object(self, common_name):
        try:
            return Species.objects.get(common_name=common_name)
        except Species.DoesNotExist:
            raise Http404

    def get(self, request, common_name, format=None):    
        species = self.get_object(common_name)
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)
     
    def put(self, request, common_name, format=None):    
        species = self.get_object(common_name)
        serializer = SpeciesSerializer(species)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, common_name, format=None):
        species = self.get_object(common_name)
        species.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)