import os 
from ultralytics import YOLO

def test():
    path = os.path.dirname(os.path.abspath(__file__))
    # Load the model.
    model = YOLO(path + "/runs/detect/yolov8n_custom/weights/best.pt")

    metrics = model.val(
        data = path + "/datasets/test.yaml",
        imgsz=416,
    )
    
    print(metrics)

if __name__ == '__main__':
   test()