import cv2
import dlib
from imutils.video import VideoStream
import imutils
import numpy as np
import math
import time
import keyboard
from pynput.keyboard import Key, Listener
#for detecting human face in frame
detector = dlib.get_frontal_face_detector()
#for predicting the 68 landmarks in the faces
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks (1).dat")
def live():
    #starting the webcam stream
    vs = VideoStream(usePiCamera=False).start()
    print("Starting stream.....")
    time.sleep(1)
    res=[]
    t=0
    while True:
        #reading the frame from video stream
        frame = vs.read()
        #resizing to max=400px
        frame = imutils.resize(frame, width=400)
        #converting to gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #detecting face from gray image
        rects = detector(gray, 0)
        print(rects)
        for rect in rects:
                #draw rectangel around face
                x1=rect.left()
                y1=rect.top()
                x2=rect.right()
                y2=rect.bottom()
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
                # get shape of face
                shape = predictor(gray, rect)
                #  (x, y)-coordinates of 68 face landmarks
                for i in range(0,68):
                    x=shape.part(i).x
                    y=shape.part(i).y
                    cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
                #forming a triangle around mouth
                lx=shape.part(54).x
                ly=shape.part(54).y
                cx=shape.part(66).x
                cy=shape.part(66).y
                rx=shape.part(48).x
                ry=shape.part(48).y
                #finding length of each side
                d1=(lx-cx)**2+(ly-cy)**2
                d1=math.sqrt(d1)
                d2=(cx-rx)**2+(cy-ry)**2
                d2=math.sqrt(d2)
                d3=(lx-rx)**2+(ly-ry)**2
                d3=math.sqrt(d3)
                #find angle using "LAW OF COSINES"
                cosalpha=(d1**2+d2**2-d3**2)/(2*d1*d2)
                alpha=math.degrees(math.acos(cosalpha))
                if(cy<ly or cy<ry):
                    alpha=360-alpha
                cv2.line(frame,(lx,ly),(cx,cy),(0,255,0),2)
                cv2.line(frame,(rx,ry),(cx,cy),(0,255,0),2)
                cv2.line(frame,(lx,ly),(rx,ry),(0,255,0),2)
                print(alpha)
                if(alpha>170):
                    res.append(0)
                else:
                    res.append(1)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                break
        if(keyboard.is_pressed('q')):
                print("quit")
                break
        if(t==15):
            break
        time.sleep(0.5)
        t=t+1
    cv2.destroyAllWindows()
    vs.stop()
    if(res.count(1)>res.count(0)):
        print("1")
        return("positve")
    else:
        print("0")
        return("negative")
##def on_press(key):
##    print('{0} pressed'.format(
##        key))
##
##def on_release(key):
##    print('{0} release'.format(
##        key))
##    if key == Key.esc:
##        # Stop listener
##        cv2.destroyAllWindows()
##        return False
##with Listener(on_press=on_press, on_release=on_release) as listener:
##           listener.join()
live()
