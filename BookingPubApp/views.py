from django.shortcuts import render
from django.http import HttpResponse
from BookingPubApp.models import Restaurant
import os
import random
import keras
import numpy as np
import xml.etree.ElementTree as ET
import tensorflow as tf

# Create your views here.
def main_page(request):
    return render(request, 'hello.html')

def restaurants_page(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants.html', {"rest" : restaurants})

def single_restaurant_page(request, id):
    dictionar = {}
    restaurant = Restaurant.objects.get(id = id)
    dictionar["r"] = restaurant
    folder = restaurant.images
    
    images_jpg = []
    images_xml = []
    for img in os.listdir(folder):
        if img.endswith('jpg'):
            images_jpg.append(img)
        elif img.endswith('xml'):
            images_xml.append(img)
    
    number = random.randint(0, len(images_jpg)-1)
    print(images_jpg[number])

    complete_img = []
    tree = ET.parse(os.path.join(restaurant.images, images_xml[number]))
    root = tree.getroot()
    for member in root.findall('object'):
        bndbox = member.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)

        img = tf.keras.preprocessing.image.load_img(os.path.join(restaurant.images, images_jpg[number]))
        img_arr = tf.keras.preprocessing.image.img_to_array(img)

        img_arr = img_arr[ymin:ymax, xmin:xmax]
        img_arr = tf.image.resize(img_arr,(150, 150)).numpy()
        complete_img.append(img_arr)
    
    X_array = np.asarray(complete_img, dtype='float32')

    trained_model = keras.Model()
    trained_model = keras.models.load_model("model_v1_1.h5")

    #TODO adauga numar mese in model restaurant, si ca sa vezi cate sunt ocupate scazi nr mese - suma

    suma = 0
    for i in range(len(X_array)):
        subimg = X_array[i]/255.
        image = np.expand_dims(subimg, axis=0)
        value = trained_model.predict(image, verbose=1, batch_size = 1)
        if value > 0.5:
            suma += 1

    print(suma)
    dictionar["tables"] = suma
    print(dictionar)


    return render(request, 'single_restaurant.html', dictionar)