from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ntapi.models import Species
from ntapi.serializers import SpeciesSerializer

@csrf_exempt
def species_list(request):
    # List all species, or add a new species
    if request.method == 'GET':
        species = Species.objects.all()
        serializer = SpeciesSerializer(species, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = SpeciesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def species_detail(request, pk):
    # Retreive, update, or delete a species
    try:
        species = Species.objects.get(pk=pk)
    except Species.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SpeciesSerializer(species)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = SpeciesSerializer(species, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        species.delete()
        return HttpResponse(status=204)