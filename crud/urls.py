from django.contrib import admin  
from django.urls import path ,include
from crud import views  
from django.urls import path 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'crop', views.CropViewSet)
urlpatterns = [  
    path('', include(router.urls)),

]  
