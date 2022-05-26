import os
import numpy as np
import tensorflow as tf
import xml.etree.ElementTree as ET


def get_images_from_folder(folder: str):
    images_jpg = []
    images_xml = []
    for img in os.listdir(folder):
        if img.endswith('jpg'):
            images_jpg.append(img)
        elif img.endswith('xml'):
            images_xml.append(img)
    
    return images_jpg, images_xml


def get_subimages_from_image(img_dir, img_jpg, img_xml, number):
    complete_img = []
    tree = ET.parse(os.path.join(img_dir, img_xml[number]))
    root = tree.getroot()

    for member in root.findall('object'):
        bndbox = member.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)

        img = tf.keras.preprocessing.image.load_img(os.path.join(img_dir, img_jpg[number]))
        img_arr = tf.keras.preprocessing.image.img_to_array(img)

        img_arr = img_arr[ymin:ymax, xmin:xmax]
        img_arr = tf.image.resize(img_arr,(150, 150)).numpy()
        complete_img.append(img_arr)
    
    X_array = np.asarray(complete_img, dtype='float32')
    
    return X_array


def prediction(X_array, model):
    suma = 0
    for i in range(len(X_array)):
        subimg = X_array[i]/255.
        image = np.expand_dims(subimg, axis=0)
        value = model.predict(image, verbose=1, batch_size = 1)
        if value > 0.5:
            suma += 1
    
    suma = 4 - suma
    return suma
