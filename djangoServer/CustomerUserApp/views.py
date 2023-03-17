from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import CustomerUser
from .serializers import CustomerUserSerializer
 
class CustomerUserCreateView(generics.CreateAPIView):
    # Define queryset and serializer_class attributes
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer

class CustomerUserRetrieveView(generics.RetrieveAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer
    # permission_classes = [IsAuthenticated]  # set your desired permission classes

    def get_object(self):
        pk = self.kwargs.get('pk')  # get the primary key from the URL
        return self.queryset.get(pk=pk)   
    
class CustomerUserUpdateView(generics.UpdateAPIView):
    # Define queryset and serializer_class attributes
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer

    def put(self, request, *args, **kwargs):
        # Retrieve the object to be updated by calling get_object_or_404 function
        instance = self.get_object()
        # Create an instance of the serializer with the retrieved object and request data
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        # Validate the serializer instance
        serializer.is_valid(raise_exception=True)
        # Save the updated object
        serializer.save()
        # Return the updated data
        return Response(serializer.data)

class CustomerUserDeleteView(generics.DestroyAPIView):
    # Define queryset and serializer_class attributes
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer

    def delete(self, request, *args, **kwargs):
        # Retrieve the object to be deleted by calling get_object_or_404 function
        instance = self.get_object()
        # Call perform_destroy method to delete the object
        self.perform_destroy(instance)
        # Return success message with HTTP 204 No Content status code
        return Response(status=status.HTTP_204_NO_CONTENT)
  