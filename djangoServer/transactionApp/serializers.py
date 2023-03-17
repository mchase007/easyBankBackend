from rest_framework import serializers
from .models import BankTransaction
from CustomerUserApp.models import CustomerUser
from CustomerUserApp.serializers import CustomerUserSerializer
 
class BankTransactionSerializer(serializers.ModelSerializer):
    
    sender_email = serializers.SlugRelatedField(slug_field="email", queryset=CustomerUser.objects.all())
    # sender_email = CustomerUserSerializer()
    receiver_email = serializers.SlugRelatedField(slug_field="email", queryset=CustomerUser.objects.all())

    # this permits changing from model to JSON or other formats but not vice versa
    class Meta:
        model = BankTransaction
        fields = '__all__'
        
        # this means fields can be read from but not updated
        # read_only_fields = fields
 