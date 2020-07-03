import cv2

def extractFrames(vidcap):
	def crop(x,y,w,h,img):

	    # Crop image
		imCrop = img[int(y):int(y+h), int(x):int(x+w)]
	    #print(imCrop)
	 
	    # Display cropped image
	    #cv2.imshow(name,imCrop)
		cv2.imwrite("frames_extracted/frame"+str(i)+".jpg", imCrop)
	    #cv2.imwrite(imagePath, imCrop)



	def getFace(image):
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.3,
			minNeighbors=3,
			minSize=(30, 30)
		)
		#print(faces)
		for (x, y, w, h) in faces:
			cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
			crop(x,y,w,h,image)  

	def getFrame(sec):
		vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
		hasFrames,image = vidcap.read()
		if hasFrames:
			getFace(image)
		return hasFrames
	sec = 0
	i = 0
	frameRate = 0.3
	success = getFrame(i)
	while success:
		sec = sec + frameRate
		sec = round(sec, 2)
		success = getFrame(sec)
		i = i+1

