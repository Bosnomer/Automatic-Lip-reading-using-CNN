import cv2

def resize1(path):
	#path = "/home/nikhere/Desktop/PROJECTFINAL/input_frame/image.jpg"
	#pathnew = "/home/nikhere/Desktop/PROJECTFINAL/nikhildataset/You are welcome/160.jpg"
	img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
		 
	width = 224
	height = 224
	dim = (width, height)
		 
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
		 
	#print('Resized Dimensions : ',resized.shape)
	#print(l)
	return resized
	#cv2.imwrite(pathnew, resized)



