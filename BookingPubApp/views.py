from django.shortcuts import render
from django.http import HttpResponse

from BookingPubApp.models import Restaurant

# Create your views here.
def main_page(request):
    return render(request, 'hello.html')

def restaurants_page(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants.html', {"rest" : restaurants})

def gogoasa(response, id):
    return HttpResponse("<h1> %s </h1>" %id)