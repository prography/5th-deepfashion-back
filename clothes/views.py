from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, permissions, generics, permissions
from .serializers import ImageSerializer, ClothingSerializer, CodiSerializer
from .models import Clothing, CodiList
from .permissions import is_owner
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser



# only for admin, testin purposes
class AdminClothingList(generics.ListCreateAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer
    permission_classes = [permissions.IsAdminUser]



# get the list of all clothes a specific user has
class UserClothingList(generics.ListCreateAPIView):
    serializer_class = ClothingSerializer
    queryset = Clothing.objects.all()
    # permission_classes = [is_owner]

    def get_queryset(self):
        """
        This view should return a list of all the clothes
        for the currently authenticated user.
        """
        # print("user is :", self.request.user)
        # user = self.request.user
        user = self.request.user
        # print(user, "is the current user")
        return Clothing.objects.filter(owner=user)

    def perform_create(self, serializer):
        return super().perform_create(serializer)

# get individual clothing, only works for owners


class ClothingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer
    permission_classes = [is_owner]


# get list of all codis for a user
class CodiListList(generics.ListCreateAPIView):
    serializer_class = CodiSerializer
    queryset = CodiList.objects.all()
    permission_classes = [is_owner]

    def post(self, request, *args, **kwargs):
        # test for clothing ownership
        for clothing in request.data['clothes']:
            if Clothing.objects.get(id=clothing).owner != request.user:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        """
        This view should return a list of all the codis
        for the currently authenticated user.
        """
        user = self.request.user
        return CodiList.objects.filter(owner=user)


class CodiListDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CodiSerializer
    queryset = CodiList.objects.all()
    permission_classes = [is_owner]
