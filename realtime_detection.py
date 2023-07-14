import cv2
import os
from ultralytics import YOLO
import supervision as sv

box_annotator = sv.BoxAnnotator(
    thickness=1,
    text_thickness=1,
    text_scale=1
)

path = os.path.dirname(os.path.abspath(__file__))
model = YOLO(path + "/runs/detect/yolov8n_custom/weights/best.pt")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    
    result = model(frame)[0]
    detections = sv.Detections.from_yolov8(result)
    
    frame = box_annotator.annotate(scene=frame, detections=detections)
            
    cv2.imshow('YOLO', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()