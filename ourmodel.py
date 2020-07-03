from tensorflow.keras.layers import Dense, Input, Dropout, GlobalAveragePooling2D, Flatten, Conv2D, BatchNormalization, Activation, MaxPooling2D
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam

# number of possible label values
nb_classes = 20

def createModel(height, width):
	# Initialising the CNN
	model = Sequential()

	# 1 - Convolution
	model.add(Conv2D(64,(3,3), padding='same', input_shape=(height, width,1)))
	model.add(BatchNormalization())
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.25))

	# 2nd Convolution layer
	model.add(Conv2D(128,(5,5), padding='same'))
	model.add(BatchNormalization())
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.25))

	# 3rd Convolution layer
	model.add(Conv2D(512,(3,3), padding='same'))
	model.add(BatchNormalization())
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.25))

	# 4th Convolution layer
	model.add(Conv2D(512,(3,3), padding='same'))
	model.add(BatchNormalization())
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.25))

	# Flattening
	model.add(Flatten())

	# Fully connected layer 1st layer
	model.add(Dense(256))
	model.add(BatchNormalization())
	model.add(Activation('relu'))
	model.add(Dropout(0.25))

	# Fully connected layer 2nd layer
	model.add(Dense(512))
	model.add(BatchNormalization())
	model.add(Activation('relu'))
	model.add(Dropout(0.25))

	model.add(Dense(nb_classes, activation='softmax'))
	
	return model

