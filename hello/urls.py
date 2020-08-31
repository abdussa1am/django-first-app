from django.urls import path , include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Passenger', views.PassengerViewSet)
router.register(r'flight', views.FlightViewSet)

urlpatterns = [
    #path("" , views.index , name="index"),
    path("<int:flight_id>" , views.flight , name="flight"),
    path("<int:flight_id>/book" ,views.book , name="book" ),
    path("counter" , views.counter , name = "counter"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("greetu" , views.greetu , name="geetu"),
    path('pdf',views.getpdf),
]