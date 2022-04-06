from rest_framework import serializers

from imager.models import Imager

class ImagerSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Imager
        fields = ('name','description','image')
    
    def create(self, validated_data):
        imager = Imager(
            name = validated_data['name'],
            description = validated_data['description'],
            image=validated_data['image'],
            user=self.context['request'].user
        )
        imager.save()
        return imager