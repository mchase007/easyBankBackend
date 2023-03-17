from django.urls import path
from .views import CustomerUserCreateView, CustomerUserRetrieveView, CustomerUserUpdateView, CustomerUserDeleteView

urlpatterns = [    
    path('customers/', CustomerUserCreateView.as_view(), name='customer-create'),
    path('customers/<int:pk>/', CustomerUserRetrieveView.as_view(), name='customer-retrieve'),
    path('customers/<int:pk>/update/', CustomerUserUpdateView.as_view(), name='customer-update'),
    path('customers/<int:pk>/delete/', CustomerUserDeleteView.as_view(), name='customer-delete'),
]


