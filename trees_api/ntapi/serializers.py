from rest_framework import serializers
from ntapi.models import Species, ECOLOGICAL_CLASSIFICATION, CONSERVATION_STATUS

class SpeciesSerializer(serializers.Serializer):
    # model = Species
    # fields = ['common_name', 'species']
    id                  = serializers.IntegerField(read_only=True)
    common_name         = serializers.CharField()
    species             = serializers.CharField()
    # family              = serializers.CharField()
    # common_name_other   = serializers.CharField()
    # min_altitude        = serializers.IntegerField() 
    # max_altitude        = serializers.IntegerField()
    # ecological_classification   = serializers.CharField()
    # conservation_status         = serializers.CharField()
    # alay_page           = serializers.IntegerField()

    def create(self, validated_data):
        return Species.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.common_name    = validated_data.get('common_name', instance.title)
        instance.species        = validated_data.get('species', instance.title)
        instance.save()
        return instance