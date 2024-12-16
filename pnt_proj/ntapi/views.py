from ntapi.models import Species
from ntapi.serializers import SpeciesSerializer
from rest_framework import generics

field_mappings = SpeciesSerializer.field_mappings

class SpeciesDetail(generics.ListAPIView):
    serializer_class = SpeciesSerializer    

    def get_queryset(self):
        queryset = Species.objects.all()
        lu_field = self.kwargs.get('lu_field')
        lu_value = self.kwargs.get('lu_value')
        
        if lu_field and lu_value:
            if lu_field in field_mappings:
                lu_field = field_mappings[lu_field]
                filter_kwargs = {f"{lu_field}__iexact": lu_value}
                queryset = queryset.filter(**filter_kwargs)
            else:
                filter_kwargs = {f"{lu_field}__iexact": lu_value}
                queryset = queryset.filter(**filter_kwargs)

        return queryset