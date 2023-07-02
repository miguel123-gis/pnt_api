from rest_framework import serializers
from ntapi.models import Species

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['id', 'common_name', 'species', 'family', 'ecological_classification', 'conservation_status', 'binhi_priority']

        # Other fields to include soon
        # family              = serializers.CharField()
        # common_name_other   = serializers.CharField()
        # min_altitude        = serializers.IntegerField() 
        # max_altitude        = serializers.IntegerField()
        # conservation_status         = serializers.CharField()
        # alay_page           = serializers.IntegerField()