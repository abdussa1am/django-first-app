from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight , Passenger
from rest_framework import viewsets
from .serializers import PassengerSerializer , FlightSerializer
from reportlab.pdfgen import canvas  
from django.http import HttpResponse  
  
# Create your views here.

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    
def greetu(request):
    return render(request , "hello/greet.html")
def flight(request , flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request , "hello/passengers.html", {
        "flights": flight , 
        "passengers" : flight.passengers.all() , 
        "non_passengers" : Passenger.objects.exclude(flights=flight).all()
})

def book(request , flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
def counter(request):
   return render(request , "hello/counter.html")     

def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, Javatpoint.")  
    p.showPage()  
    p.save()  
    return response  