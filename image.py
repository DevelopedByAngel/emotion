import cv2
import dlib
import numpy as np
import math
import time
def detect(file):
    img=cv2.imread(file)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    detector=dlib.get_frontal_face_detector()
    faces=detector(gray)
    print(faces)
    for face in faces:
        x1=face.left()
        y1=face.top()
        x2=face.right()
        y2=face.bottom()
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),5)
    print("Detecting Landmarks.....")
    p = "shape_predictor_68_face_landmarks (1).dat"
    predictor = dlib.shape_predictor(p)
    landmarks=predictor(gray, face)
    for i in range(0,68):
        x=landmarks.part(i).x
        y=landmarks.part(i).y
        cv2.circle(img,(x,y),3,(0,0,255),-1)
    lx=landmarks.part(54).x
    ly=landmarks.part(54).y
    cx=landmarks.part(66).x
    cy=landmarks.part(66).y
    rx=landmarks.part(48).x
    ry=landmarks.part(48).y
##    m1=(cy-ly)/(cx-lx)
##    m1=m1*-1 if  m1<0 else m1
##    m2=(cy-ry)/(cx-rx)
##    m2=m2*-1 if m2<0 else m2
##    print(m1,m2)
##    tanO=(m1-m2)/(1+(m1*m2))
##    tanO=tanO*-1 if tanO<0 else tanO
##    O=math.atan(tanO)
##    print(tanO,O,math.degrees(O))
    d1=(lx-cx)**2+(ly-cy)**2
    d1=math.sqrt(d1)
    d2=(cx-rx)**2+(cy-ry)**2
    d2=math.sqrt(d2)
    d3=(lx-rx)**2+(ly-ry)**2
    d3=math.sqrt(d3)
    cosalpha=(d1**2+d2**2-d3**2)/(2*d1*d2)
    alpha=math.degrees(math.acos(cosalpha))
## make changes for slanting face by checking if both eyes are in same line or not    
    if(cy<ly or cy<ry):
        alpha=360-alpha
    print(alpha)
    cv2.line(img,(lx,ly),(cx,cy),(0,255,0),2)
    cv2.line(img,(rx,ry),(cx,cy),(0,255,0),2)
    cv2.line(img,(lx,ly),(rx,ry),(0,255,0),2)
    cv2.imshow("Emotion Detection",img)
    key = cv2.waitKey() 
    if(alpha<170):
        return("positive")
    else:
        return("negative")
##detect("face1.jpg")
