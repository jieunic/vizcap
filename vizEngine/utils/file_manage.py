import os
import cv2
import time
from tkinter import filedialog, messagebox

class FileManager:
    def __init__(self, detection_save_path, captured_save_path, confirmation_path):
        self.detection_save_path = detection_save_path
        self.captured_save_path = captured_save_path
        self.confirmation_path = confirmation_path
        self._ensure_directories()
        self.timestamp = None

    def _ensure_directories(self):
        os.makedirs(self.detection_save_path, exist_ok=True)
        os.makedirs(self.captured_save_path, exist_ok=True)

    def _generate_timestamp(self):
        if self.timestamp is None:
            self.timestamp = time.strftime("%Y%m%d_%H%M%S")
        return self.timestamp

    def _reset_timestamp(self):
        self.timestamp = None

    def _save_image(self, frame, prefix, save_path):
        if frame is not None:
            timestamp = self._generate_timestamp()
            filename = f'{prefix}_{timestamp}.jpg'
            filename2 = f'{prefix}_{timestamp}'
            self.output_filename = os.path.join(save_path, filename)
            cv2.imwrite(self.output_filename, frame)
        else:
            messagebox.showwarning("Warning", "No image to save!")
        return filename, self.output_filename, filename2

    def save_raw(self, raw_frame):
        result = self._save_image(raw_frame, 'img_raw', self.captured_save_path)
        # self._reset_timestamp()
        return result

    def save_res(self, res_frame, *args):
        for arg in args:
            if arg == 'no_confirm':
                result = self._save_image(res_frame, 'img_res', self.detection_save_path)
                self._reset_timestamp()
                messagebox.showinfo("Information", f"Image saved in\n'{self.output_filename}'")
            elif arg == 'confirm':
                result = self._save_image(res_frame, 'img_res', self.confirmation_path)
                self._reset_timestamp()
        return result

    def open_folder(self):
        file_paths = filedialog.askopenfilenames(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
        )
        return file_paths
