# Automatic Lip reading using CNN
This is a small project which actually classifies humans speaking 10 words and 10 phrases. The input is a video and the machine will classify the word/phrase out of the 20 objects based on the facial and lip movements in the video frames.

# Getting Started
Well there is a gui(app.py) which will give an idea about the project, where we input video, get frames, concat, resize, feed to model, classify. All this is explained below.

Table of contents
=================

<!--ts-->
   * [Automatic Lip reading using CNN](#automatic-lip-reading-using-cnn)
   * [Getting Started](#getting-started)
   * [Table of contents](#table-of-contents)
   * [Libraries](#libraries)
   * [Dataset](#dataset)
   * [Model](#model)
   * [Result and Analysis](#result-and-analysis)
   * [Overall Implementation](#overall-implementation)
   * [Conclusion](#conclusion)
<!--te-->

# Libraries
Many Python libraries were used in this project. I recommend to install them as:
```
Open CV: pip install opencv-python
Tkinter: apt-get install python-tk
Pillow: pip install Pillow
Numpy: pip install numpy
Tensorflow: pip install tensorflow-gpu
```
There might occur errors while installing libraries as there might be ambiguity in the versions. So check changing the version. Also i used tensorflow-gpu for training the model in google colab. So one can use colab, it is quite better.

# Dataset
<img src="/images/dataset.png" align="center">
For any ML problem, the most important thing is data. We got the data from [MIRACL-VC1](https://sites.google.com/site/achrafbenhamadou/-datasets/miracl-vc1). The Dataset consists of 10 words and 10 phrases spoken by 15 speakers 10 times each object.
The data was in the form of sequence of images. The difficult part was to convert this dataset into the right form which was required for the model.
We converted the dataset as a single image input. This can be illustrated as in figure below:

<img src="/images/dataset1.png" height="426px" width="885px"> 
<br/>
So as in the above figure, the dataset contains sequence of images as of the left side. We segmented the facial part of all the speakers in the sequence of images. As seen in the left side it is difficult to extract the features, that's why we extracted the face from images. This is done with every image in the dataset. 

<br/>
<img src="/images/dataset2.png" align="center" height="758px" width="684px">
<br/>

After we extracted faces from each image, we concatenated the image sequences into a single image. This might look like some sort of matrix. This step is done because we are using simpele CNN and not advanced topics like LSTM and RNN. Using Pillow we can do this easily. For every word/phrase uttered, we created such concatenated images.
Also we resized to a constant size i.e. here we resized to 224*224.
<br/>
So after this we get the dataset which contains 150 images for a single word/phrase but we added our own 20 more to each object i.e. our two speakers uttered 10 words and 10 phrases and this was added to the dataset.
<br/>
So overall we have 3400 images(17 speakers uttering 20 objects 10 times each) and we splitted train-test as 80-20.

# Model
Once getting the dataset in the right form, the next step is Implementing Model. 
<br/>
The entire model and its implementation is in the [final.ipynb](final.ipynb) file where we built the model. There is Image data generator, various layers of CNN, analysis part in the file.
<br/>
The model is as:
```
model = Sequential()

# 1 - Convolution
model.add(Conv2D(64,(3,3), padding='same', input_shape=(224, 224,1)))
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

opt = Adam(lr=0.0001)
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
```
 There are 4 Conv 2D layers(along with Normalization, MaxPooling, Dropout and Activation) and 2 fully connected layers. The model was compiled with Adam optimizer at 0.0001 lr and loss='categorical_crossentropy'. 
 ```
 epochs = 50

from keras.callbacks import ModelCheckpoint

checkpoint = ModelCheckpoint("my_model.h5", monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

history = model.fit_generator(generator=train_generator,
                                steps_per_epoch=train_generator.n//train_generator.batch_size,
                                epochs=epochs,
                                validation_data = validation_generator,
                                validation_steps = validation_generator.n//validation_generator.batch_size,
                                callbacks=callbacks_list
                                )
```
The model is then fitted with epochs=50 and batch size=20 as shown above. The Result and Analysis is discussed below.

# Result and Analysis
<img src="/images/acc.png" align="center" height="520px" width="520px">
<br/>
<img src="/images/loss.png" align="center" height="520px" width="540px">
<br/>
As seen the model shows a decent training validation accuracy. This is not the best model but it is quite a decent model. The Confusion matrix is as shown below:
<img src="/images/confusion.png" align="center" height="750px" width="700px">

# Overall Implementation
The overall implementation is running the app.py file which opens a GUI. We can select the video where we want to read lips. This video can be audioless or can be from a noisy environment.
The System will extract the frames from the video, i.e. its actually getting the sequence of images. The it will concat it into a single image and resize it to 224*224. Then it is passed to the saved model and the result is text prediction in the GUI itself.

# Conclusion
So this is a pretty decent project for entry level. Also some problems arise such as ambiguity, issues when new faces are detected due to limited dataset. Also it works fine with the known faces. So quite a good project to study.
