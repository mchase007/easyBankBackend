from django.db import models
from CustomerUserApp.models import CustomerUser
# required auth imports for using foreign keys
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


from django.utils import timezone

# class TransactionManager(models.Manager):
#     def create_transaction(self, sender_email, receiver_email, amount, transaction_type):
#         """
#         Creates a new transaction object with the given sender, receiver, and amount.
#         """
#         # actualSender = CustomerUser.objects.get(email=sender)
#         sender_email = request.data.get('sender_email')
#         sender = CustomerUser.objects.get(email=sender_email)
         
#         transaction = self.model(sender=sender, amount=amount, transaction_type=transaction_type)
#         if transaction_type == 'transfer':
#             if sender.balance < amount:
#                 raise ValidationError('Insufficient funds')
#             if isinstance(receiver, CustomerUser):
#                 receiver.balance += amount
#                 receiver.save()
#             else:
#                 transaction.receiver_email = receiver.email
#             sender.balance -= amount
#             sender.save()
#         elif transaction_type == 'deposit':
#             sender.balance += amount
#             sender.save()
#         elif transaction_type == 'withdrawal':
#             if sender.balance < amount:
#                 raise ValidationError('Insufficient funds')
#             sender.balance -= amount
#             sender.save()
#         transaction.save()
#         return transaction

#     def get_transactions_for_user(self, user):
#         """
#         Returns a queryset of all transactions involving the given user as either the sender or receiver.
#         """
#         return self.filter(Q(sender=user) | Q(receiver=user))

class BankTransaction(models.Model):
    TRANSACTION_TYPES = (
        ('D', 'Deposit'),
        ('W', 'Withdrawal'),
        ('T', 'Transfer'), 
    ) 

    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    sender_email = models.ForeignKey(CustomerUser, related_name='sent_transactions', null=True, blank=False, on_delete=models.PROTECT)
    receiver_email = models.ForeignKey(CustomerUser, null=True, blank=True, related_name='received_transactions', on_delete=models.CASCADE, to_field='email')
    reference = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction from {self.sender_email} to {self.recipient_name} ({self.receiver_email})"

    # objects = TransactionManager()

    class Meta:
        ordering = ['-transaction_date']