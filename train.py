from ultralytics import YOLO
import os 

def train():
   path = os.path.dirname(os.path.abspath(__file__))
   # Load the model.
   model = YOLO('yolov8n.pt')
   
   # Training.
   model.train(
      data= path + "/datasets/data.yaml",
      imgsz=416,
      epochs=300,
      batch=8,
      name='yolov8n_custom',
      save=True,
      save_period = 10
   )

if __name__ == '__main__':
   train()