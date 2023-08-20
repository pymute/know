from django.shortcuts import render
from .serializers import ModelSerializer
from rest_framework.views import APIView
from .models import CustomUser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView)
# Create your views here.

class AllView(ListAPIView):
    queryset =CustomUser.objects.all()
    serializer_class = ModelSerializer

class DetailView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ModelSerializer

class UpdateView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ModelSerializer

class CreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ModelSerializer

class DeleteView(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ModelSerializer


class View(APIView):
    def get(self,request,*args,**kwargs):
        by = get_object_or_404(CustomUser,id=kwargs['id'])
        serializer = ModelSerializer(by)
        return Response(dict(serializer.data)['bo'])

