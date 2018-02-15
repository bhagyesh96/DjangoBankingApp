from rest_framework import serializers
from .models import dashboard



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = dashboard
        fields = ('name',)
        #fields = '__all__'


