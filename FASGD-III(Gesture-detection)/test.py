#!/usr/bin/env python
#     converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
#     skinMask = cv2.inRange(converted, lower, upper) 

    # Apply a series of erosions and dilations to the mask 
    # using an elliptical kernel 
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    # skinMask = cv2.erode(skinMask, kernel, iterations = 2) 
    # skinMask = cv2.dilate(skinMask, kernel, iterations = 2) 

    # # Blur the mask to help remove noise, then apply the mask to 
    # # the frame 
    # skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    # skin = cv2.bitwise_and(frame, frame, mask=skinMask) 

    # # Show the skin in the image along with the mask 
    # cv2.imshow("images", np.hstack([frame, skin]))


# # while camera.isOpened():
# #     ret, frame = camera.read()

# #     cv2.imshow("Frame", frame)
# #     key = cv2.waitKey(1) & 0xFF;
    
# #     if key == ord("q"):
# #         break

# bg = None 

# # Finging the running average over the background
# def run_avg(image, aWeight): 
#     global bg 
#     # Initialize the background 
#     if bg is None: 
#         bg = image.copy().astype("float")
#         return 

#     # Compute weighted avearage, accumulate it and update the background
#     cv2.accumulateWeighted(image, bg, aWeight)

# # To segment the region of hand in the image
# def segment(image, threshold=25): 
#     global bg
#     # Find the absolute difference between background and current frame
#     diff = cv2.absdiff(bg.astype("uint8"), image)
    
#     # threshold the diff image so that we got the foreground
#     threshold = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]

#     # Get the contours in the thresholded image 
#     cnts = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Return None, if no countours detected 
#     if len(cnts) == 0: 
#         return None 

#     else:
#         # based on contor area, get the maximum contour which is the hand 
#         segmented = max(cnts, key = cv2.contourArea) 
#         return (thresholded, segmented) 
    

# # cv2.destroyAllWindows()

# # Initialize the video stream and allow the camera sensor to warm up
# print("[INFO] starting the video stream")
# vs = VideoStream(src=0).start()

# # Sleeping for 2 seconds
# time.sleep(0.2)

# # Starting the FPS counter
# fps = FPS().start()

# # Initailize weight for running average 
# aWeight = 0.5 

# # region of interest (ROI) co-ordinates 
# top, right, bottom, left = 10, 350, 225, 590 

# # Initialize the number of frames 
# num_frame = 0 

# # loop over the frames from the video file stream
# while True:
#     # Grabbing the frame from the threaded video stream and resize it to
#     # to 500px (to speed up the processing)
#     frame = vs.read()
#     frame = imutils.resize(frame, width=700)

#     # flip the frame so that is is not the mirror view 
#     frame = cv2.flip(frame, 1) 

#     # Clone the frame 
#     clone = frame.copy() 

#     # get the height and width of the frame 
#     (height, width) = frame.shape[:2]

#     # Get the ROI 
#     roi = frame[top:bottom, right:left]

#     # Convert the roi to grayscale and blur it 
#     gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) 
#     gray = cv2.GaussianBlur(gray, (7, 7), 0) 

#     # To get the background, keep looking till a threshold is reached 
#     # so that our running average model gets calibrated 
#     if num_frame < 30: 
#         run_avg(gray, aWeight)  

#     else: 
#         # Segment the hand region 
#         hand = segment(gray) 

#         # Check whether hand region is segmented 
#         if hand is not None: 
#             # if yes, unpack the threshold image and 
#             # Segmented region 
#             (thresholded, segmented) = hand 

#             # Draw the segmented region and display the frame 
#             cv2.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))
#             cv2.imshow("Thresholded", thresholded) 

#     # Draw the segmented hand 
#     cv2.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)

#     # Increment the number of frames 
#     num_frame += 1 

#     # Display the frames with segmented hand 
#     cv2.imshow("Video Feed", clone)




    
#     # # Convert the input from (1) BGR to grayscale
#     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # #
#     # (thresh, blackAndWhite) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

#     # # Describing the font to be used
#     # font = cv2.FONT_HERSHEY_SIMPLEX
    
#     # # Using puttext method for inserting text on video
#     # cv2.putText(frame, "Hello Chinedum", (9, 25), font, 0.72,
#     #                                     (0, 0, 255), 2) 

#     # # Displaying both images
#     # cv2.imshow("Gray", blackAndWhite)
#     # cv2.imshow("RGB", frame)
    
#     # Exiting
#     key = cv2.waitKey(1) & 0xFF;
#     if key == ord("q"):
#         break

# # Cleaning up 
# cv2.destroyAllWindows(); 


# import cv2
# import numpy as np
# import math


# cap = cv2.VideoCapture(0)
# while(cap.isOpened()):
#     # read image
#     ret, img = cap.read()

#     # get hand data from the rectangle sub window on the screen
#     cv2.rectangle(img, (300,300), (100,100), (0,255,0),0)
#     crop_img = img[100:300, 100:300]

#     # convert to grayscale
#     grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

#     # applying gaussian blur
#     value = (35, 35)
#     blurred = cv2.GaussianBlur(grey, value, 0)

#     # thresholdin: Otsu's Binarization method
#     _, thresh1 = cv2.threshold(blurred, 127, 255,
#                                cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#     # show thresholded image
#     cv2.imshow('Thresholded', thresh1)

#     # check OpenCV version to avoid unpacking error
#     (version, _, _) = cv2.__version__.split('.')

#     if version == '3':
#         image, contours, hierarchy = cv2.findContours(thresh1.copy(), \
#                cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#     elif version == '2':
#         contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
#                cv2.CHAIN_APPROX_NONE)

#     # find contour with max area
#     cnt = max(contours, key = lambda x: cv2.contourArea(x))

#     # create bounding rectangle around the contour (can skip below two lines)
#     x, y, w, h = cv2.boundingRect(cnt)
#     cv2.rectangle(crop_img, (x, y), (x+w, y+h), (0, 0, 255), 0)

#     # finding convex hull
#     hull = cv2.convexHull(cnt)

#     # drawing contours
#     drawing = np.zeros(crop_img.shape,np.uint8)
#     cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 0)
#     cv2.drawContours(drawing, [hull], 0,(0, 0, 255), 0)

#     # finding convex hull
#     hull = cv2.convexHull(cnt, returnPoints=False)

#     # finding convexity defects
#     defects = cv2.convexityDefects(cnt, hull)
#     count_defects = 0
#     cv2.drawContours(thresh1, contours, -1, (0, 255, 0), 3)

#     # applying Cosine Rule to find angle for all defects (between fingers)
#     # with angle > 90 degrees and ignore defects
#     for i in range(defects.shape[0]):
#         s,e,f,d = defects[i,0]

#         start = tuple(cnt[s][0])
#         end = tuple(cnt[e][0])
#         far = tuple(cnt[f][0])

#         # find length of all sides of triangle
#         a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
#         b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
#         c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

#         # apply cosine rule here
#         angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57

#         # ignore angles > 90 and highlight rest with red dots
#         if angle <= 90:
#             count_defects += 1
#             cv2.circle(crop_img, far, 1, [0,0,255], -1)
#         #dist = cv2.pointPolygonTest(cnt,far,True)

#         # draw a line from start to end i.e. the convex points (finger tips)
#         # (can skip this part)
#         cv2.line(crop_img,start, end, [0,255,0], 2)
#         #cv2.circle(crop_img,far,5,[0,0,255],-1)

#     # define actions required
#     if count_defects == 1:
#         cv2.putText(img,"I am Vipul", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
#     elif count_defects == 2:
#         str = "This is a basic hand gesture recognizer"
#         cv2.putText(img, str, (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
#     elif count_defects == 3:
#         cv2.putText(img,"This is 4 :P", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
#     elif count_defects == 4:
#         cv2.putText(img,"Hi!!!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
#     else:
#         cv2.putText(img,"Hello World!!!", (50, 50),\
#                     cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

#     # show appropriate images in windows
#     cv2.imshow('Gesture', img)
#     all_img = np.hstack((drawing, crop_img))
#     cv2.imshow('Contours', all_img)

#     k = cv2.waitKey(10)
#     if k == 27:
#         break


# import cv2
# import numpy as np
# import math
# cap = cv2.VideoCapture(0)
     
# while(1):
        
#     try:  #an error comes if it does not find anything in window as it cannot find contour of max area
#           #therefore this try error statement
          
#         ret, frame = cap.read()
#         frame=cv2.flip(frame,1)
#         kernel = np.ones((3,3),np.uint8)
        
#         #define region of interest
#         roi=frame[100:300, 100:300]
        
        
#         cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)    
#         hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        
        
         
#     # define range of skin color in HSV
#         lower_skin = np.array([0,20,70], dtype=np.uint8)
#         upper_skin = np.array([20,255,255], dtype=np.uint8)
        
#      #extract skin colur imagw  
#         mask = cv2.inRange(hsv, lower_skin, upper_skin)
        
   
        
#     #extrapolate the hand to fill dark spots within
#         mask = cv2.dilate(mask,kernel,iterations = 4)
        
#     #blur the image
#         mask = cv2.GaussianBlur(mask,(5,5),100) 
        
        
        
#     #find contours
#         _,contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
#    #find contour of max area(hand)
#         cnt = max(contours, key = lambda x: cv2.contourArea(x))
        
#     #approx the contour a little
#         epsilon = 0.0005*cv2.arcLength(cnt,True)
#         approx= cv2.approxPolyDP(cnt,epsilon,True)
       
        
#     #make convex hull around hand
#         hull = cv2.convexHull(cnt)
        
#      #define area of hull and area of hand
#         areahull = cv2.contourArea(hull)
#         areacnt = cv2.contourArea(cnt)
      
#     #find the percentage of area not covered by hand in convex hull
#         arearatio=((areahull-areacnt)/areacnt)*100
    
#      #find the defects in convex hull with respect to hand
#         hull = cv2.convexHull(approx, returnPoints=False)
#         defects = cv2.convexityDefects(approx, hull)
        
#     # l = no. of defects
#         l=0
        
#     #code for finding no. of defects due to fingers
#         for i in range(defects.shape[0]):
#             s,e,f,d = defects[i,0]
#             start = tuple(approx[s][0])
#             end = tuple(approx[e][0])
#             far = tuple(approx[f][0])
#             pt= (100,180)
            
            
#             # find length of all sides of triangle
#             a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
#             b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
#             c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
#             s = (a+b+c)/2
#             ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
            
#             #distance between point and convex hull
#             d=(2*ar)/a
            
#             # apply cosine rule here
#             angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
            
        
#             # ignore angles > 90 and ignore points very close to convex hull(they generally come due to noise)
#             if angle <= 90 and d>30:
#                 l += 1
#                 cv2.circle(roi, far, 3, [255,0,0], -1)
            
#             #draw lines around hand
#             cv2.line(roi,start, end, [0,255,0], 2)
            
            
#         l+=1
        
#         #print corresponding gestures which are in their ranges
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         if l==1:
#             if areacnt<2000:
#                 cv2.putText(frame,'Put hand in the box',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
#             else:
#                 if arearatio<12:
#                     cv2.putText(frame,'0',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
#                 elif arearatio<17.5:
#                     cv2.putText(frame,'Best of luck',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                   
#                 else:
#                     cv2.putText(frame,'1',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                    
#         elif l==2:
#             cv2.putText(frame,'2',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
#         elif l==3:
         
#               if arearatio<27:
#                     cv2.putText(frame,'3',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
#               else:
#                     cv2.putText(frame,'ok',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                    
#         elif l==4:
#             cv2.putText(frame,'4',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
#         elif l==5:
#             cv2.putText(frame,'5',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
#         elif l==6:
#             cv2.putText(frame,'reposition',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
#         else :
#             cv2.putText(frame,'reposition',(10,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
#         #show the windows
#         cv2.imshow('mask',mask)
#         cv2.imshow('frame',frame)
#     except:
#         pass
        
    
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
    
# cv2.destroyAllWindows()
# cap.release()    
