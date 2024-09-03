"""
Program for visual inspection cuptip developed by internal DX Maintenance

    rev = 2
    version = 
    author = Niko Kristian
    date_created = June 28, 2024
"""


import tkinter as tk, configparser as CP
from vizEngine.middleware.camera import Camera
from vizEngine.middleware.logger_conf import ConfirmationLogger
from vizEngine.detect import ObjectDetection
from vizEngine.ui.ui import UI
from vizEngine.measure import Measurement
from vizEngine.utils.file_manage import FileManager
from vizEngine.utils.root import dir

cp = CP.ConfigParser()
cp.read(f"{dir()}/vizEngine/setup.cfg")
root = tk.Tk()
camera = Camera()
logger = ConfirmationLogger(log_path=f"{dir()}{cp['logs']['confirmation_record']}")
detection = ObjectDetection(model_path=f"{dir()}{cp['models']['model_path']}")
file_manager = FileManager(detection_save_path=f"{dir()}{cp['files']['save_result']}", captured_save_path=f"{dir()}{cp['files']['save_raw']}", confirmation_path=f"{dir()}{cp['files']['save_confirmation']}")
measurement = Measurement()

UI(root, camera, detection, file_manager, measurement, cp, logger)

root.mainloop()