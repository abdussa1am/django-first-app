from django.shortcuts import render , redirect  
from django.http import HttpResponseRedirect , HttpResponse 
from django.urls import reverse
from .models import Crop
from rest_framework import viewsets
from .serializers import CropSerializer 
  



class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    filter_fields = ('elem', 'item' , 'year')
