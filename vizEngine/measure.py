import cv2
import numpy as np
from scipy.spatial import distance as dist
from imutils import perspective
from PIL import Image, ImageTk
import imutils

class Measurement:
    def __init__(self, video_source=2, pixels_per_metric=7):
        self.video_source = video_source
        self.cap = cv2.VideoCapture(self.video_source)
        self.pixels_per_metric = pixels_per_metric
        self.measuring = False

    def start(self):
        self.measuring = True
        if not self.cap.isOpened():
            self.cap.open(self.video_source)

    def stop(self):
        self.measuring = False
        if self.cap.isOpened():
            self.cap.release()

    def midpoint(self, ptA, ptB):
        return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

    def update_frame(self):
        if not self.measuring:
            self.cap.release()
            cv2.destroyAllWindows()
            return None

        ret, frame = self.cap.read()
        if not ret:
            self.stop()
            return None

        frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
        orig = frame[:1080, 0:1920]

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(gray, 15)
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        kernel = np.ones((3, 3), np.uint8)
        closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=3)

        result_img = closing.copy()
        contours, hierachy = cv2.findContours(result_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        hitung_objek = 0

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 1000 or area > 120000:
                continue

            orig = frame.copy()
            box = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
            box = np.array(box, dtype="int")
            box = perspective.order_points(box)
            cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 64), 2)

            for (x, y) in box:
                cv2.circle(orig, (int(x), int(y)), 5, (0, 255, 64), -1)

            (tl, tr, br, bl) = box
            (tltrX, tltrY) = self.midpoint(tl, tr)
            (blbrX, blbrY) = self.midpoint(bl, br)
            (tlblX, tlblY) = self.midpoint(tl, bl)
            (trbrX, trbrY) = self.midpoint(tr, br)

            cv2.circle(orig, (int(tltrX), int(tltrY)), 0, (0, 255, 64), 5)
            cv2.circle(orig, (int(blbrX), int(blbrY)), 0, (0, 255, 64), 5)
            cv2.circle(orig, (int(tlblX), int(tlblY)), 0, (0, 255, 64), 5)
            cv2.circle(orig, (int(trbrX), int(trbrY)), 0, (0, 255, 64), 5)

            cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
            cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)

            lebar_pixel = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
            panjang_pixel = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

            dimA = lebar_pixel / self.pixels_per_metric
            dimB = panjang_pixel / self.pixels_per_metric

            cv2.putText(orig, "L: {:.1f}CM".format(dimA / 25.5), (int(trbrX + 10), int(trbrY)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(orig, "P: {:.1f}CM".format(dimB / 25.5), (int(tltrX - 15), int(tltrY - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            hitung_objek += 1

        cv2.putText(orig, "Jumlah: {}".format(hitung_objek), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        rgb_image = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_image)
        tk_image = ImageTk.PhotoImage(image=pil_image)
        return tk_image
