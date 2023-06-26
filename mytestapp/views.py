from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view

# import permission classes decorator
from rest_framework.decorators import permission_classes
from django.shortcuts import render


from .models import Service

from .serializers import ServiceSerializer

# Create your views here.
class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# Creating Service requires authentication using JWT
# class ServiceCreate(generics.CreateAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#     permission_classes = (IsAuthenticated,)


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    content = {'message': 'Hello, World!'}
    return Response(content)
