from FramesExtraction import extractFrames
from concat import concatFrames
from resize import resize1
from ourmodel import createModel
import os
import cv2


from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Input, Dropout, GlobalAveragePooling2D, Flatten, Conv2D, BatchNormalization, Activation, MaxPooling2D
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model

import numpy as np
import seaborn as sns
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt
import os

import cv2
import tensorflow


def prediction(vidcap):
	#vidcap = cv2.VideoCapture('/home/nikhere/Desktop/PROJECTFINAL/Test/You are Welcome/VID20200306085607.mp4')
	#demo1(vidcap)
	#os.remove(file) for file in os.listdir('/home/nikhere/Desktop/PROJECTFINAL/frames_extracted/') if file.endswith('.jpg')
	vidcap = cv2.VideoCapture(vidcap)
	#print(vidcap)
	extractFrames(vidcap)
	concatFrames(1)

	path = "frames_extracted/"
	for file in os.scandir(path):
		if file.name.endswith(".jpg"):
		    os.unlink(file.path)

	pathnew = "input_frame/image.jpg"       
	image1 = resize1(pathnew)
	height, width, channels = image1.shape
	#print (height, width, channels)

	# size of the image: 224*224 pixels
	pic_size = 224

	# input path for the images
	#base_path = "/home/nikhere/Desktop/PROJECTFINAL/datasetToUse/"

	"""
	# number of images to feed into the NN for every batch
	batch_size = 20

	datagen_train = ImageDataGenerator()
	datagen_validation = ImageDataGenerator()

	train_generator = datagen_train.flow_from_directory(base_path + "train",
		                                                target_size=(pic_size,pic_size),
		                                                color_mode="grayscale",
		                                                batch_size=batch_size,
		                                                class_mode='categorical',
		                                                shuffle=True)

	validation_generator = datagen_validation.flow_from_directory(base_path + "test",
		                                                target_size=(pic_size,pic_size),
		                                                color_mode="grayscale",
		                                                batch_size=batch_size,
		                                                class_mode='categorical',
		                                                shuffle=False)
	"""	                                                
	model = createModel(pic_size, pic_size)

	model.load_weights("/home/nikhere/Desktop/PROJECTFINAL/my_newmodel.h5")
	print("Model weights loaded")

	OBJECT_LIST = ["Begin", "Choose", "Connection", "Excuse me", "Good Bye", "Have a good time",
		                 "Hello", "How are you", "I am sorry", "I love this game", "Navigation", 
		                 "Next", "Nice to meet you" ,"Previous", "Start", "Stop", "Stop Navigation",
		                 "Thank you", "Web", "You are welcome"]
		                 
		                 
	gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
	gray = gray.reshape(224,224,1)
	gray = tensorflow.cast(gray, tensorflow.float32)
	#print(type(gray))
	height, width, channels = gray.shape
	#print (height, width, channels)

	some = (OBJECT_LIST[model.predict_classes(np.array([gray]))[0]])
	print("done")
	return some
