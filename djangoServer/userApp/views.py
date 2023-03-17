from django.shortcuts import render
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
  
# create an instance of APIView
# class CustomUserList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     # handle GET request
#     def get(self, request, format=None):
#         # get all instances of model
#         users = CustomUser.objects.all()
#         # serialize data to prefered format
#         serializer = CustomUserSerializer(users, many=True)
#         # send response
#         return Response(serializer.data)

#     # handle POST request
#     def post(self, request, format=None):
#         # validate incoming customerUser data
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             # save if data is valid
#             serializer.save()
#             # send client appropriate response
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
# class CustomUserDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """

#     # Helper method to get a snippet instance given its primary key
#     def get_object(self, pk):
#         try:
#             return CustomUser.objects.get(pk=pk)
#         except CustomUser.DoesNotExist:
#             raise Http404

#     # Handle GET requests to retrieve a snippet instance
#     def get(self, request, pk, format=None):
#         # Use the helper method to get the snippet instance
#         CustomUser = self.get_object(pk)
#         # Serialize the snippet instance using the SnippetSerializer
#         serializer = CustomUserSerializer(CustomUser)
#         # Return the serialized data in a Response object
#         return Response(serializer.data)

#     # Handle PUT requests to update a snippet instance
#     def put(self, request, pk, format=None):
#         # Use the helper method to get the snippet instance
#         CustomUser = self.get_object(pk)
#         # Deserialize the request data using the SnippetSerializer and the existing snippet instance
#         serializer = CustomUserSerializer(CustomUser, data=request.data)
#         # If the deserialization is valid, save the updated instance and return the serialized data
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         # If the deserialization is invalid, return the errors in a Response object
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Handle DELETE requests to delete a snippet instance
#     def delete(self, request, pk, format=None):
#         # Use the helper method to get the snippet instance
#         CustomUser = self.get_object(pk)
#         # Delete the snippet instance
#         CustomUser.delete()
#         # Return a Response object with no content and a 204 status code
#         return Response(status=status.HTTP_204_NO_CONTENT)



class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer