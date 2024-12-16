from rest_framework import serializers
from ntapi.models import Species

class SpeciesSerializer(serializers.ModelSerializer):
    field_mappings = {
        'name': 'common_name',
        'classification': 'ecological_classification',
        'status': 'conservation_status'
    }

    class Meta:
        model = Species 
        fields = ['id', 'common_name', 'species', 'family', 'ecological_classification', 'conservation_status', 'binhi_priority']