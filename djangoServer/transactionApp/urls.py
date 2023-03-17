from django.urls import path, include
from .views import BankTransactionList, UserBankTransactionList, BankTransactionDetail
urlpatterns = [
  path('transactions/', BankTransactionList.as_view(), name='transaction-list-create'),
  path('transactions/user/<str:email>', UserBankTransactionList.as_view(), name='transaction-list-user'),
  path('transactions/<int:pk>/', BankTransactionDetail.as_view(), name='transaction-retrieve'),
] 