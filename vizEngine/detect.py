import cv2, json, configparser as CP
from ultralytics import YOLO
from PIL import Image, ImageTk
from vizEngine.utils.root import dir

cp = CP.ConfigParser()
cp.read(f"{dir()}/vizEngine/setup.cfg")

with open(f"{dir()}{cp['files']['bb_color']}", 'r') as file:
    keys = json.load(file)

class ObjectDetection:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect_objects(self, image_path):
        results = self.model(image_path, verbose=False)
        img = cv2.imread(image_path)
        box_number = 0
        for result in results:
            for box in result.boxes:
                box_number += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls = int(box.cls[0])
                label = self.model.names[cls]
                color = (0, 255, 0)  # Default not boundingbox when not setup
                if label in keys:
                    color = (keys[label][0], keys[label][1], keys[label][2])
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                cv2.putText(img, f'{box_number}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Conversion opencv to tkinter
        image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)
        image_tk = ImageTk.PhotoImage(image_pil)
        return image_tk, img