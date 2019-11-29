import cv2
import numpy as np
def check(ret):
	if ret == False:
		print("Error opening file")

def resize(foreground, n):
	height , width, layers =  foreground.shape
	k = 2
	if n > 1:
		k = n
	height = height/k
	width = width/k
	resize = cv2.resize(foreground, (int(width), int(height)))
	return resize

def assembly(frame, foreground, n, i):
	height_max , width_max, layers =  frame.shape
	height, width, layers =  foreground.shape
	if (2 < n) and (n <= 4):
		if 1 < i and i < 4:
			height_max = height_max - height
			width_max = width_max + 2 * width
	width_max = width_max - width * i
	frame[(height_max - height):(height_max),(width_max - width):(width_max),:3] = foreground	
	return frame

if __name__ == "__main__":
	n = 8
	if 18 < n:
		print('Introduced too many video, reduce their number to 19, please')
		sys.exit()
	name_video = ['video2.mov', 'video3.mov', 'video4.mov', 'video5.mov', 'video6.mov', 'video7.mov', 'video8.mov', 'video9.mov']
	ret_array = ['ret2', 'ret3', 'ret4', 'ret5', 'ret6', 'ret7', 'ret8', 'ret9']
	source = {'cap2' : 'foreground2', 'cap3' : 'foreground3', 'cap4' : 'foreground4', 'cap5' : 'foreground5',  'cap6' : 'foreground6', 'cap7' : 'foreground7', 'cap8' : 'foreground8', 'cap9' : 'foreground9'}
	cap = cv2.VideoCapture('video1.mov')
	while cap.isOpened():
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



