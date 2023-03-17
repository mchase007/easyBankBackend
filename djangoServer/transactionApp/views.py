from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import BankTransaction
from .serializers import BankTransactionSerializer
from CustomerUserApp.models import CustomerUser

class BankTransactionList(generics.ListCreateAPIView):
    queryset = BankTransaction.objects.all()
    serializer_class = BankTransactionSerializer 
    
class UserBankTransactionList(generics.ListAPIView):
    serializer_class = BankTransactionSerializer 
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        # queryset = Purchase.objects.all()
        queryset = BankTransaction.objects.all()
        sender_email = self.request.query_params.get('sender_email')
        if sender_email is not None:
            queryset = queryset.filter(CustomerUser_email=sender_email)
        return queryset

 
class BankTransactionDetail(generics.RetrieveAPIView):
    queryset = BankTransaction.objects.all()
    serializer_class = BankTransactionSerializer
