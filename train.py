from ultralytics import YOLO
import os 

path = os.path.dirname(os.path.abspath(__file__))
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data= path + "/datasets/data.yaml",
   imgsz=416,
   epochs=10,
   batch=8,
   name='yolov8n_custom'
)
