# import necessary modules
from rest_framework import serializers
from .models import CustomUser
 

# serializer class to extend serializers.ModelSerializer
# serializers.ModelSerializer abstracts field validation and methods
class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        # set model to be used by serializer
        model = CustomUser
         
        # set fields of model to be used by serializer
        fields = ['id', 'username', 'email', 'password', 'mobile_number', 
                  'address', 'account_number','first_name','last_name']
 