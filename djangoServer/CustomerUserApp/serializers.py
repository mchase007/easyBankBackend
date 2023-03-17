from rest_framework import serializers
from .models import CustomerUser 

class CustomerUserSerializer(serializers.ModelSerializer):
     
    class Meta: 
        model = CustomerUser
        fields = ['id', 'first_name', 'last_name', 'address', 'username', 'email', 'password', 'mobile_number', 'balance', 'account_number']
 