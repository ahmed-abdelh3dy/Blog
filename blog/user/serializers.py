from rest_framework import serializers
from .models import CustomUser



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


    def validate_name(self , value):
        if len(value) < 5 :
            raise serializers.ValidationError('name  must be more than 5 chars')
        return value
