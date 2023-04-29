from rest_framework import serializers
from ntapi.models import Species, ECOLOGICAL_CLASSIFICATION, CONSERVATION_STATUS

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['common_name', 'species']

        # Other fields to include soon
        # family              = serializers.CharField()
        # common_name_other   = serializers.CharField()
        # min_altitude        = serializers.IntegerField() 
        # max_altitude        = serializers.IntegerField()
        # ecological_classification   = serializers.CharField()
        # conservation_status         = serializers.CharField()
        # alay_page           = serializers.IntegerField()