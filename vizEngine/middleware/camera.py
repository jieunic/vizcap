import cv2, numpy as np
from PIL import Image

class Camera:
    def __init__(self):
        pass

    def src_camera(self, source):
        self.cam_source = source
        self.vid = cv2.VideoCapture(source)

    def start(self):
        self.vid.open(self.cam_source)

    def stop(self):
        self.vid.release()

    def cap(self):
        if self.vid is not None and self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return frame
        return None

    def update_frame(self):
        ret, frame = self.vid.read()
        if ret:
            frame = cv2.GaussianBlur(frame, (5, 5), 0)
            kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
            frame = cv2.filter2D(frame, -1, kernel)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame)
            # pil_image = pil_image.rotate(180)
            return pil_image
        return None
