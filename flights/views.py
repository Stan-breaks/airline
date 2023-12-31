from django.shortcuts import render
from .models import Flight,Passengers
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all(),
    })

def flight(request,flight_id):
    try:
        flight=Flight.objects.get(pk=flight_id)
    except ObjectDoesNotExist:
         return HttpResponseNotFound('Flight not found.', status=404)
    return render(request,"flights/flight.html",{
        "flight": flight,
        "passengers":flight.passengers.all(),
        "non_passengers":Passengers.objects.exclude(flights=flight).all()
    })

def book(request,flight_id):
    if(request.method=='POST'):
        flight=Flight.objects.get(pk=flight_id)
        passenger=Passengers.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))

 