from rest_framework import serializers

from imager.models import Imager

class ImagerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Imager
        fields = ('name','description','image')