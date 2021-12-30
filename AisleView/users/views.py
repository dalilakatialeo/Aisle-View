from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer
from users import serializers

# Create your views here.

# /users
class CustomUserList(APIView):
    # GET method - retrieve all users
    def get(self, request):
        if self.request.user.is_superuser:
            customuser = CustomUser.objects.all()
        else:
            customuser = CustomUser.objects.filter(username=self.request.user)

        serializer = CustomUserSerializer(customuser, many=True) #explicitly stating the relationship
        return Response(serializer.data)
        
    # POST method - create a new user
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# /users/<pk>
class CustomUserDetail(APIView):
    
    # helper method for getting a user and raising a 404 if that user does not exist
    def get_object(self, pk):
        # try getting the user with the specified pk
        try:
            return CustomUser.objects.get(pk=pk)
        # catch the exception that we'll get if the user with that pk doesn't exist
        except CustomUser.DoesNotExist:
            # raise an Http404 exception so that Django knows to show a 404
            raise Http404

    # GET a single user's detail
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    #updating user details
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(
            instance=user,
            data = request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        # return Response (status = status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'User deleted'})