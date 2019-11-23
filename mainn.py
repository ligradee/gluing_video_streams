import cv2
import numpy as np
def check(ret):
	if(ret == False):
		print("Error opening file")

def resize(foreground, n):
	height , width, layers =  foreground.shape
	k = 0
	if(n == 2):
		k = 2
	if(2< n <= 5):
		k = 4
	if(5 < n):
		k = 8
	height = height/k
	width = width/k
	resize = cv2.resize(foreground, (int(height), int(width)))
	return resize

def assembly(frame, foreground, n, i):
	height_max , width_max, layers =  frame.shape
	width, height, layers =  foreground.shape
	if(2 < n <= 5):
		if(i <= 3):
			width_max = width_max - width * (i-2)
		if(3 < i <= 5):
			height_max = height_max - height
			width_max = width_max - width * (i-2)
	if (5 < n):
		if(i <= 9):
			width_max = width_max - width * (i-2)
		if(9 < i):
			height_max = height
			width_max = width_max - width * (i-2)
	print(height_max - height, height_max, height, width_max - width, width_max, width)
	added_image = cv2.addWeighted(frame[height_max - height:height_max,width_max - width:width_max,:],0,foreground[0:height,0:width,:],1,0)
	frame[height_max - height:height_max,width_max - width:width_max,:] = added_image	
	return frame

if__name__="__main__"
n = 5
name_video = ['video2.mov', 'video3.mov', 'video4.mov', 'video5.mov']
ret_array = ['ret2', 'ret3', 'ret4', 'ret5']
source = {'cap2' : 'foreground2', 'cap3' : 'foreground3', 'cap4' : 'foreground4', 'cap5' : 'foreground5' }
cap = cv2.VideoCapture('video1.mov')
if(19 < n):
	print('Introduced too many video, reduce their number to 19, please')
	sys.exit()
while (cap.isOpened()):
	ret, frame = cap.read()
	i = 0
	for key in source:
		key = cv2.VideoCapture(name_video[i])
		foreground = source.get(key)
		ret_array[i], foreground = key.read()
		check(ret_array[i])
		foreground = resize(foreground, n)
		frame = assembly(frame, foreground, n, i)
		i = i + 1	
	if ret == True:
		cv2.imshow('frame', frame)
		if cv2.waitKey(25) & 0xFF == ord('q'): 
				break
cap.release()



