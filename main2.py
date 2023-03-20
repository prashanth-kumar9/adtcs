import cv2
import torch
from tracker import *
import numpy as np
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

cap=cv2.VideoCapture('./video/lane2.mp4')


def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('ADAPTIVE TRAFFIC CONTROLL')
cv2.setMouseCallback('ADAPTIVE TRAFFIC CONTROLL', POINTS)

tracker = Tracker()
area_1=[(263, 247),(655, 269), (704, 197), (672, 171), (563, 150), (275, 227)]
area1=set()
pl=[]
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(1020,500))
    cv2.polylines(frame, [np.array(area_1, np.int32)], True, (0, 0, 0),1)
    results=model(frame)
    list=[]
    for index, row in results.pandas().xyxy[0].iterrows():
        x1=int(row['xmin'])
        y1=int(row['ymin'])
        x2=int(row['xmax'])
        y2=int(row['ymax'])
        b=str(row['name'])
        if 'car' in b or 'motorcycle' in b or 'bus' in b or 'truck' in b:
            list.append([x1,y1,x2,y2])
        #cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0, 255),2)
        #cv2.putText(frame, b, (x1, y1), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
    boxes_ids=tracker.update(list)
    for box_id in boxes_ids:
        x,y,w,h,id=box_id
        cv2.rectangle(frame, (x,y),(w,h), (255, 0, 0),1)
        cv2.putText(frame, str(id), (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255),2)
        #cv2.putText(frame, b, (x+20,y), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255),2)
        result=cv2.pointPolygonTest(np.array(area_1, np.int32), (int(w), int(h)), False)
        if result>0:
            area1.add(id)
            
    p=(len(area1))
    cv2.putText(frame, 'vechile count: '+str(p), (20,30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255),3)
    cv2.imshow('ADAPTIVE TRAFFIC CONTROLL',frame)
    pl.append(p)
    print(str(p) + "- vechiles")
    
    if cv2.waitKey(1) & 0xFF== ord('q'):
        f=open('out', 'a')
        f.write(str(max(pl)))
        break

cap.release()
cv2.destroyAllWindows()
    
    

