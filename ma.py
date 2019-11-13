import cv2
import numpy as np
def resized(frame):
	height, width, layers =  frame.shape
	new_h = height/4
	new_w = width/4
	print(int(new_w), int(new_h))
	resize = cv2.resize(frame, (int(new_w), int(new_h))) 
	return resize

def show(cap, cap2, cap3, cap4, cap5):
	if(cap.isOpened() == False):
		print("Error opening file")
	if(cap2.isOpened() == False):
		print("Error opening file")
	if(cap3.isOpened() == False):
		print("Error opening file")
	if(cap4.isOpened() == False):
		print("Error opening file")
	if(cap5.isOpened() == False):
		print("Error opening file")
	while(cap.isOpened()): 
		ret, frame = cap.read()
		ret2, foreground2 = cap2.read()
		ret3, foreground3 = cap3.read()
		ret4, foreground4 = cap4.read()
		ret5, foreground5 = cap5.read()
		foreground2 = resized(foreground2)
		foreground3 = resized(foreground3)
		foreground4 = resized(foreground4)
		foreground5 = resized(foreground5)
		added_image = cv2.addWeighted(frame[810:1080,1440:1920,:],0,foreground2[0:270,0:480,:],1,0)
		frame[810:1080,1440:1920,:] = added_image
		added_image = cv2.addWeighted(frame[540:810,960:1440,:],0,foreground3[0:270,0:480,:],1,0)
		frame[540:810,960:1440,:] = added_image
		added_image = cv2.addWeighted(frame[810:1080,960:1440,:],0,foreground4[0:270,0:480,:],1,0)
		frame[810:1080,960:1440,:] = added_image
		added_image = cv2.addWeighted(frame[540:810,1440:1920,:],0,foreground5[0:270,0:480,:],1,0)
		frame[540:810,1440:1920,:] = added_image
		#added_image = cv2.addWeighted(frame[30:70,350:650,:],0,foreground5[30:70,350:650,:],1,0)
		#frame[30:70,350:650,:] = added_image
		if ret == True:
			cv2.imshow('frame', frame)
			if cv2.waitKey(25) & 0xFF == ord('q'): 
				break
cap = cv2.VideoCapture('video1.mov')
cap2 = cv2.VideoCapture('video2.mov')
cap3 = cv2.VideoCapture('video3.mov')
cap4 = cv2.VideoCapture('video4.mov')
cap5 = cv2.VideoCapture('video5.mov')
show(cap, cap2, cap3, cap4, cap5)

cap.release()