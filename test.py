import os 
from ultralytics import YOLO

path = os.path.dirname(os.path.abspath(__file__))
# Load the model.
model = YOLO("best.pt")

# Testing.
results = model.predict(path+"/datasets/test/images/000246247_jpg.rf.fb915aef7c063ce2ac971f8de0d8b2c1.jpg")
print(results)