import cv2
import numpy as np
from PIL import Image
import numpy as np


def concatFrames(val):
	def get_concat_h_multi_resize(im_list, resample=Image.BICUBIC):
		min_height = min(im.height for im in im_list)
		im_list_resize = [im.resize((int(im.width * min_height / im.height), min_height),resample=resample)
		                  for im in im_list]
		total_width = sum(im.width for im in im_list_resize)
		dst = Image.new('RGB', (total_width, min_height))
		pos_x = 0
		for im in im_list_resize:
		    dst.paste(im, (pos_x, 0))
		    pos_x += im.width
		return dst

	def get_concat_v_multi_resize(im_list, resample=Image.BICUBIC):
		min_width = min(im.width for im in im_list)
		im_list_resize = [im.resize((min_width, int(im.height * min_width / im.width)),resample=resample)
		                  for im in im_list]
		total_height = sum(im.height for im in im_list_resize)
		dst = Image.new('RGB', (min_width, total_height))
		pos_y = 0
		for im in im_list_resize:
		    dst.paste(im, (0, pos_y))
		    pos_y += im.height
		return dst
		
		
	def get_concat_tile_resize(im_list_2d, resample=Image.BICUBIC):
		im_list_v = [get_concat_h_multi_resize(im_list_h, resample=resample) for im_list_h in im_list_2d]
		return get_concat_v_multi_resize(im_list_v, resample=resample)

	ima = []

	l = 0
	while l < 30:
		path1 = "frames_extracted/frame"
		path = path1 + str(l)
		
		imagep2 = ".jpg"
		imagePath = path + imagep2			
		
			
		try:
			image = Image.open(imagePath)

			if np.any(image != None) :
				ima.append(image)
		except: 
			break
						
		l=l+1

	if (len(ima) == 5):
		get_concat_tile_resize([[ima[0], ima[1], ima[2]],
					   	[ima[3], ima[4], ima[4]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 6):
		get_concat_tile_resize([[ima[0], ima[1], ima[2]],
					[ima[3], ima[4], ima[5]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 7):
		get_concat_tile_resize([[ima[0], ima[1], ima[2]],
					[ima[3], ima[4], ima[5]],
					   	[ima[6], ima[6], ima[6]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 8):
		get_concat_tile_resize([[ima[0], ima[1], ima[2]],
					[ima[3], ima[4], ima[5]],
					[ima[6], ima[7], ima[7]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 9):
		get_concat_tile_resize([[ima[0], ima[1], ima[2]],
					[ima[3], ima[4], ima[5]],
					   	[ima[6], ima[7], ima[8]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 10):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3]],
					[ima[4], ima[5], ima[6], ima[7]],
					   	[ima[8], ima[9], ima[9], ima[9]]]).save('input_frame/image'+'.jpg')		
						
						
	elif (len(ima) == 11):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3]],
					[ima[4], ima[5], ima[6], ima[7]],
					[ima[8], ima[9], ima[10], ima[10]]]).save('input_frame/image'+'.jpg')			
				
					
	elif (len(ima) == 12):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3]],
			          		[ima[4], ima[5], ima[6], ima[7]],
			           		[ima[8], ima[9], ima[10], ima[11]]]).save('input_frame/image'+'.jpg')
				           				
	elif (len(ima) == 13):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3]],
			           		[ima[4], ima[5], ima[6], ima[7]],
			          		[ima[8], ima[9], ima[10], ima[11]],
			           		[ima[12], ima[12], ima[12], ima[12]]]).save('input_frame/image'+'.jpg')
				           				
	elif (len(ima) == 14):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3]],
			           		[ima[4], ima[5], ima[6], ima[7]],
			           		[ima[8], ima[9], ima[10], ima[11]],
			           		[ima[12], ima[13], ima[13], ima[13]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 15):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3]],
			           		[ima[4], ima[5], ima[6], ima[7]],
			          		[ima[8], ima[9], ima[10], ima[11]],
			           		[ima[12], ima[13], ima[14], ima[14]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 16):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3]],
			            	[ima[4], ima[5], ima[6], ima[7]],
			           		[ima[8], ima[9], ima[10], ima[11]],
			           		[ima[12], ima[13], ima[14], ima[15]]]).save('input_frame/image'+'.jpg')

	elif (len(ima) == 17):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4]],
			            	[ima[5], ima[6], ima[7], ima[8], ima[9]],
			           		[ima[10], ima[11], ima[12], ima[13], ima[14]],
			           		[ima[15], ima[16], ima[16], ima[16], ima[16]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 18):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4]],
			            	[ima[5], ima[6], ima[7], ima[8], ima[9]],
			           		[ima[10], ima[11], ima[12], ima[13], ima[14]],
			           		[ima[15], ima[16], ima[17], ima[17], ima[17]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 19):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4]],
			            	[ima[5], ima[6], ima[7], ima[8], ima[9]],
			           		[ima[10], ima[11], ima[12], ima[13], ima[14]],
			           		[ima[15], ima[16], ima[17], ima[18], ima[18]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 20):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4]],
			            	[ima[5], ima[6], ima[7], ima[8], ima[9]],
			           		[ima[10], ima[11], ima[12], ima[13], ima[14]],
			           		[ima[15], ima[16], ima[17], ima[18], ima[19]]]).save('input_frame/image'+'.jpg')
				   
				           				
	elif (len(ima) == 21):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4]],
			            	[ima[5], ima[6], ima[7], ima[8], ima[9]],
			           		[ima[10], ima[11], ima[12], ima[13], ima[14]],
				           	[ima[15], ima[16], ima[17], ima[18], ima[19]],
				           	[ima[20], ima[20], ima[20], ima[20], ima[20]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 22):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4]],
			            	[ima[5], ima[6], ima[7], ima[8], ima[9]],
			           		[ima[10], ima[11], ima[12], ima[13], ima[14]],
			           		[ima[15], ima[16], ima[17], ima[18], ima[19]],
			           		[ima[20], ima[21], ima[21], ima[21], ima[21]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 23):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4]],
			            	[ima[5], ima[6], ima[7], ima[8], ima[9]],
			           		[ima[10], ima[11], ima[12], ima[13], ima[14]],
			           		[ima[15], ima[16], ima[17], ima[18], ima[19]],
			           		[ima[20], ima[21], ima[22], ima[22], ima[22]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 24):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4]],
			            	[ima[5], ima[6], ima[7], ima[8], ima[9]],
			           		[ima[10], ima[11], ima[12], ima[13], ima[14]],
			           		[ima[15], ima[16], ima[17], ima[18], ima[19]],
			           		[ima[20], ima[21], ima[22], ima[23], ima[23]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 25):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4]],
			            	[ima[5], ima[6], ima[7], ima[8], ima[9]],
			           		[ima[10], ima[11], ima[12], ima[13], ima[14]],
			           		[ima[15], ima[16], ima[17], ima[18], ima[19]],
			           		[ima[20], ima[21], ima[22], ima[23], ima[24]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 26):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4], ima[5]],
			            	[ima[6], ima[7], ima[8], ima[9], ima[10], ima[11]],
			           		[ima[12], ima[13], ima[14], ima[15], ima[16], ima[17]],
			           		[ima[18], ima[19], ima[20], ima[21], ima[22], ima[23]],
			           		[ima[24], ima[25], ima[25], ima[25], ima[25], ima[25]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 27):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4], ima[5]],
				            [ima[6], ima[7], ima[8], ima[9], ima[10], ima[11]],
				           	[ima[12], ima[13], ima[14], ima[15], ima[16], ima[17]],
				           	[ima[18], ima[19], ima[20], ima[21], ima[22], ima[23]],
				           	[ima[24], ima[25], ima[26], ima[26], ima[26], ima[26]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 28):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4], ima[5]],
			            	[ima[6], ima[7], ima[8], ima[9], ima[10], ima[11]],
			           		[ima[12], ima[13], ima[14], ima[15], ima[16], ima[17]],
			           		[ima[18], ima[19], ima[20], ima[21], ima[22], ima[23]],
			           		[ima[24], ima[25], ima[26], ima[27], ima[27], ima[27]]]).save('input_frame/image'+'.jpg')


	elif (len(ima) == 29):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4], ima[5]],
			            	[ima[6], ima[7], ima[8], ima[9], ima[10], ima[11]],
			           		[ima[12], ima[13], ima[14], ima[15], ima[16], ima[17]],
			           		[ima[18], ima[19], ima[20], ima[21], ima[22], ima[23]],
			           		[ima[24], ima[25], ima[26], ima[27], ima[28], ima[28]]]).save('input_frame/image'+'.jpg')
		
		
	elif (len(ima) == 30):
		get_concat_tile_resize([[ima[0], ima[1], ima[2], ima[3], ima[4], ima[5]],
			            	[ima[6], ima[7], ima[8], ima[9], ima[10], ima[11]],
			           		[ima[12], ima[13], ima[14], ima[15], ima[16], ima[17]],
			           		[ima[18], ima[19], ima[20], ima[21], ima[22], ima[23]],
			           		[ima[24], ima[25], ima[26], ima[27], ima[28], ima[29]]]).save('input_frame/image'+'.jpg')
				          		

