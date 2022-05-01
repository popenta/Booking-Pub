from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from BookingPubApp.models import Restaurant
import random
import keras
from .utils import *

#loading the model
trained_model = keras.Model()
trained_model = keras.models.load_model("model_v1_1.h5")


# Create your views here.
def main_page(request):
    return render(request, 'hello.html')


def restaurants_page(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants.html', {"rest" : restaurants})

@login_required
def single_restaurant_page(request, id):
    dictionar = {}
    restaurant = Restaurant.objects.get(id = id)
    dictionar["r"] = restaurant
    folder = restaurant.images
    
    images_jpg, images_xml = get_images_from_folder(folder)
    
    number = random.randint(0, len(images_jpg)-1)
    print(images_jpg[number])

    X_array = get_subimages_from_image(restaurant.images, images_jpg, images_xml, number)

    dictionar["tables"] = prediction(X_array, trained_model)

    return render(request, 'single_restaurant.html', dictionar)
