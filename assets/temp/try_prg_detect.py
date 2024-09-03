# from ultralytics import YOLO
# import cv2

# # Load YOLOv8 model (pre-trained)
# model = YOLO('A:/TMMIN Project/cuptip_vision/vizcap/assets/model/yolov8n.pt')  # Anda bisa mengganti dengan 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt', atau 'yolov8x.pt' tergantung kebutuhan

# # Membaca gambar menggunakan OpenCV
# image_path = 'A:/TMMIN Project/cuptip_vision/vizcap/assets/temp/bottle_glass.jpg'
# image = cv2.imread(image_path)

# # Melakukan prediksi object detection
# results = model(image)

# # Mendefinisikan warna untuk label tertentu
# label_colors = {
#     'bottle': (255, 0, 0),  # Warna biru dalam format BGR
#     'cup': (0, 191, 255)    # Warna amber dalam format BGR
# }

# # Menampilkan hasil prediksi
# box_number = 0
# for result in results:
#     for box in result.boxes:
#         box_number += 1
#         # Mendapatkan koordinat bounding box
#         x1, y1, x2, y2 = map(int, box.xyxy[0])
#         # Mendapatkan kelas prediksi
#         cls = int(box.cls[0])
#         # Mendapatkan nama kelas
#         label = model.names[cls]

#         # Menentukan warna bounding box berdasarkan label
#         color = (0, 255, 0)  # Warna default hijau
#         if label in label_colors:
#             color = label_colors[label]

#         # Menggambar bounding box pada gambar
#         cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
#         # Menambahkan nomor bounding box pada gambar
#         cv2.putText(image, f'{box_number}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# # Menampilkan gambar hasil deteksi
# cv2.imshow('YOLOv8 Object Detection', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
from ultralytics import YOLO
import cv2

# Load YOLOv8 model (pre-trained)
model = YOLO('A:/TMMIN Project/cuptip_vision/vizcap/assets/model/yolov8n.pt')

# Membaca gambar menggunakan OpenCV
image_path = 'A:/TMMIN Project/cuptip_vision/vizcap/assets/temp/bottle_glass.jpg'
image = cv2.imread(image_path)

# Melakukan prediksi object detection
results = model(image)

# Mendefinisikan warna untuk label tertentu
label_colors = {
    'bottle': (255, 0, 0),  # Warna biru dalam format BGR
    'cup': (0, 191, 255)    # Warna amber dalam format BGR
}

# Menampilkan hasil prediksi
box_number = 0
for result in results:
    for box in result.boxes:
        box_number += 1
        # Mendapatkan koordinat bounding box
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        # Mendapatkan kelas prediksi
        cls = int(box.cls[0])
        # Mendapatkan nama kelas
        label = model.names[cls]

        # Menentukan warna bounding box berdasarkan label
        color = (0, 255, 0)  # Warna default hijau
        if label in label_colors:
            color = label_colors[label]

        # Menggambar bounding box pada gambar
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        # Menambahkan nomor bounding box pada gambar
        cv2.putText(image, f'{box_number}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Konversi gambar dari OpenCV ke format yang bisa ditampilkan di Tkinter
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_pil = Image.fromarray(image_rgb)
image_tk = ImageTk.PhotoImage(image_pil)

# Membuat jendela Tkinter
root = tk.Tk()
root.title('YOLOv8 Object Detection')

# Menambahkan Label dengan gambar hasil deteksi ke dalam jendela
label = Label(root, image=image_tk)
label.pack()

# Menjalankan loop utama Tkinter
root.mainloop()
