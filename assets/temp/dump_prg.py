# import tkinter as tk
# from tkinter import ttk, filedialog, messagebox, PhotoImage
# from PIL import Image, ImageTk
# from vizEngine.utils.root import dir

# class UI:
#     def __init__(self, tk_root, camera, detection, file_manager, measurement):
#         self.root = tk_root
#         self.root.iconbitmap(f"{dir()}/assets/icon/dxicon.ico")
#         self.camera = camera
#         self.detection = detection
#         self.file_manager = file_manager
#         self.measurement = measurement

#         self.root.title("VIZcap - Visual Inspection Cuptip")
#         self.root.geometry("1100x600")

#         self.notebook = ttk.Notebook(self.root)
#         self.notebook.pack(fill='both', expand=True)
#         self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)

#         self.detection_tab = ttk.Frame(self.notebook)
#         self.measure_tab = ttk.Frame(self.notebook)

#         self.notebook.add(self.detection_tab, text="Object Detection")
#         self.notebook.add(self.measure_tab, text="Measure")

#         self.setup_detection_tab()
#         self.setup_measure_tab()

#     def setup_detection_tab(self):
#         # Create new frame for detection tab
#         self.bottom_frame = tk.Frame(self.detection_tab, height=50)
#         self.bottom_frame.pack(side=tk.BOTTOM, anchor=tk.S)

#         # Size value for button
#         self.btn_height = 40
#         self.btn_width = 270

#         # Create dropdown menu bar 'File'
#         self.menubar = tk.Menu(self.root)
#         self.file_menu = tk.Menu(self.menubar, tearoff=0)
#         self.file_menu.add_command(label="Open", command=self.open_file)
#         self.file_menu.add_command(label="Save", command=self.save_file)
#         self.file_menu.add_separator()
#         self.file_menu.add_command(label="Exit", command=self.root.quit)
#         self.menubar.add_cascade(label="File", menu=self.file_menu)

#         # Create dropdown menu bar 'Help'
#         self.help_menu = tk.Menu(self.menubar, tearoff=0)
#         self.help_menu.add_command(label="About", command=self.show_about)
#         self.menubar.add_cascade(label="Help", menu=self.help_menu)

#         # Configure for button icon
#         self.icon_cameraon = PhotoImage(file=f"{dir()}/assets/icon/cameraon.png")
#         self.icon_cameraon = self.icon_cameraon.subsample(10)
#         self.icon_cameraoff = PhotoImage(file=f"{dir()}/assets/icon/cameraoff.png")
#         self.icon_cameraoff = self.icon_cameraoff.subsample(10)
#         self.icon_capture = PhotoImage(file=f"{dir()}/assets/icon/capture.png")
#         self.icon_capture = self.icon_capture.subsample(7)
#         self.icon_save = PhotoImage(file=f"{dir()}/assets/icon/save.png")
#         self.icon_save = self.icon_save.subsample(7)
#         self.icon_foldercapture = PhotoImage(file=f"{dir()}/assets/icon/openfolder.png")
#         self.icon_foldercapture = self.icon_foldercapture.subsample(7)

#         self.root.config(menu=self.menubar)

#         # Canvas for preview image
#         self.canvas1 = tk.Canvas(self.detection_tab, bg="black")
#         self.canvas1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
#         self.canvas2 = tk.Canvas(self.detection_tab, bg="black")
#         self.canvas2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

#         # Button group
#         self.switch_cam = tk.Button(self.bottom_frame, text="Start Camera", command=self.toggle_camera, height=self.btn_height, width=self.btn_width)
#         self.switch_cam.pack(side=tk.LEFT, padx=10, pady=10)
#         self.capture_button = tk.Button(self.bottom_frame, text="Capture", command=self.capture, height=self.btn_height, width=self.btn_width)
#         self.capture_button.pack(side=tk.LEFT, padx=10, pady=10)
#         self.save_button = tk.Button(self.bottom_frame, text="Save", command=self.save_detection_result, height=self.btn_height, width=self.btn_width)
#         self.save_button.pack(side=tk.LEFT, padx=10, pady=10)
#         self.open_button = tk.Button(self.bottom_frame, text="Open Folder", command=self.open_folder, height=self.btn_height, width=self.btn_width)
#         self.open_button.pack(side=tk.LEFT, padx=10, pady=10)

#         self.camera_running = False

#     def setup_measure_tab(self):
#         self.bottom_frame = tk.Frame(self.measure_tab, height=50)
#         self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

#         self.canvas = tk.Canvas(self.measure_tab, bg="gray")
#         self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

#         self.stop_button = tk.Button(self.bottom_frame, text="Stop", command=self.stop_measure)
#         self.stop_button.pack(side=tk.LEFT, padx=10)

#     def on_tab_changed(self, event):
#         if self.notebook.index("current") == 0:
#             self.camera.start()
#         else:
#             self.camera.stop()
#             self.measurement.stop()

#     def toggle_camera(self):
#         if not self.camera_running:
#             self.camera.start()
#             self.camera_running = True
#             self.switch_cam.config(text="Stop Camera", image=self.icon_cameraoff)
#             self.update()
#         else:
#             self.camera.stop()
#             self.camera_running = False
#             self.switch_cam.config(text="Start Camera", image=self.icon_cameraon)

#     def update(self):
#         if self.camera_running:
#             frame = self.camera.update_frame()
#             if frame is not None:
#                 self.photo = ImageTk.PhotoImage(frame)
#                 self.canvas1.create_image(0, 0, image=self.photo, anchor=tk.NW)
#             self.root.after(10, self.update)

#     def capture(self):
#         save_path = self.file_manager.captured_save_path
#         image_filename = self.camera.capture_image(save_path)
#         if image_filename:
#             im_array, photo = self.detection.detect_objects(image_filename)
#             if photo:
#                 self.canvas2.create_image(0, 0, image=photo, anchor=tk.NW)
#                 self.detected_frame = im_array

#     def save_detection_result(self):
#         self.file_manager.save_detection_result(self.detected_frame)

#     def open_folder(self):
#         file_paths = self.file_manager.open_folder()
#         if file_paths:
#             for file_path in file_paths:
#                 im_array, photo = self.detection.detect_objects(file_path)
#                 if photo:
#                     self.canvas2.create_image(0, 0, image=photo, anchor=tk.NW)
#                     self.detected_frame = im_array

#     def start_measure(self):
#         self.measurement.start()
#         self.update_measure()

#     def stop_measure(self):
#         self.measurement.stop()

#     def update_measure(self):
#         if self.measurement.measuring:
#             tk_image = self.measurement.update_frame()
#             if tk_image:
#                 self.canvas.create_image(0, 0, image=tk_image, anchor=tk.NW)
#             self.root.after(10, self.update_measure)

#     def open_file(self):
#         pass

#     def save_file(self):
#         pass

#     def show_about(self):
#         messagebox.showinfo("About", "Object Detection and Measurement App")

# import tkinter as tk
# from tkinter import ttk, Menu, PhotoImage
# from PIL import Image, ImageTk
# from vizEngine.utils.root import dir

# class UI:
#     def __init__(self, tk_root, camera, detection, file_manager, measurement):
#         self.root = tk_root
#         self.root.iconbitmap(f"{dir()}/assets/icon/dxicon.ico")
        
#         self.root.title("VIZcap - Visual Inspection Cuptip")
#         self.root.geometry("800x600")

#         # Object for support function
#         self.camera = camera
#         self.detection = detection
#         self.file_manager = file_manager
#         self.measurement = measurement
#         self.delay = 10

#         # Run UI
#         self.tab_detection()

#         # Creating a menu bar
#         menu_bar = Menu(self.root)
#         self.root.config(menu=menu_bar)

#         # Adding file menu
#         file_menu = Menu(menu_bar, tearoff=0)
#         file_menu.add_command(label="Open")
#         file_menu.add_separator()
#         file_menu.add_command(label="Exit", command=self.root.quit)
#         menu_bar.add_cascade(label="File", menu=file_menu)

#         # Adding view menu
#         view_menu = Menu(menu_bar, tearoff=0)
#         menu_bar.add_cascade(label="View", menu=view_menu)

#         # Adding help menu
#         help_menu = Menu(menu_bar, tearoff=0)
#         menu_bar.add_cascade(label="Help", menu=help_menu)

#         # Adding tab control
#         self.tab_control = ttk.Notebook(self.root)
#         self.tab1 = ttk.Frame(self.tab_control)
#         self.tab2 = ttk.Frame(self.tab_control)

#         self.tab_control.add(self.tab1, text='Detect')
#         self.tab_control.add(self.tab2, text='Measure')
#         self.tab_control.pack(expand=1, fill="both")

#     def tab_detection(self):
#         # Configuring grid layout for tab1
#         self.tab1.grid_rowconfigure(0, weight=1)
#         self.tab1.grid_rowconfigure(1, weight=4)
#         self.tab1.grid_rowconfigure(2, weight=1)
#         self.tab1.grid_columnconfigure(0, weight=1)
#         self.tab1.grid_columnconfigure(1, weight=1)
#         self.tab1.grid_columnconfigure(2, weight=1)
#         self.tab1.grid_columnconfigure(3, weight=1)

#         # Adding colored boxes with labels
#         # box_hello = tk.Label(self.tab1, bg='blue', width=2, height=1)
#         # box_hello.grid(row=0, column=0, padx=5, pady=5, sticky='e')
#         # label_hello = tk.Label(self.tab1, text="hello")
#         # label_hello.grid(row=0, column=1, padx=5, pady=5, sticky='w')

#         # box_hai = tk.Label(self.tab1, bg='orange', width=2, height=1)
#         # box_hai.grid(row=0, column=2, padx=5, pady=5, sticky='e')
#         # label_hai = tk.Label(self.tab1, text="hai")
#         # label_hai.grid(row=0, column=3, padx=5, pady=5, sticky='w')

#         # box_hehe = tk.Label(self.tab1, bg='red', width=2, height=1)
#         # box_hehe.grid(row=0, column=4, padx=5, pady=5, sticky='e')
#         # label_hehe = tk.Label(self.tab1, text="hehe")
#         # label_hehe.grid(row=0, column=5, padx=5, pady=5, sticky='w')

#         # Adding labels for image frames
#         label1 = tk.Label(self.tab1, text="CAMERA LIVE")
#         label1.grid(row=0, column=0, columnspan=2)
#         label2 = tk.Label(self.tab1, text="DETECTED IMAGE")
#         label2.grid(row=0, column=2, columnspan=2)

#         # Adding a frame container for the image frames to ensure equal size
#         frame_container = tk.Frame(self.tab1)
#         frame_container.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

#         # Configure grid in the frame container
#         frame_container.grid_rowconfigure(0, weight=1)
#         frame_container.grid_columnconfigure(0, weight=1)
#         frame_container.grid_columnconfigure(1, weight=1)

#         # Adding frames for images inside the container
#         frame1 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
#         frame1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
#         self.cam_canvas = tk.Canvas(frame1, width=640, height=480)
#         self.cam_canvas.pack(expand=True)
#         frame2 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
#         frame2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
#         self.res_canvas = tk.Canvas(frame2, width=640, height=480)
#         self.res_canvas.pack(expand=True)

#         # Configure for button icon
#         self.icon_cameraon = PhotoImage(file=f"{dir()}/assets/icon/cameraon.png")
#         self.icon_cameraon = self.icon_cameraon.subsample(10)
#         self.icon_cameraoff = PhotoImage(file=f"{dir()}/assets/icon/cameraoff.png")
#         self.icon_cameraoff = self.icon_cameraoff.subsample(10)
#         self.icon_capture = PhotoImage(file=f"{dir()}/assets/icon/capture.png")
#         self.icon_capture = self.icon_capture.subsample(7)
#         self.icon_save = PhotoImage(file=f"{dir()}/assets/icon/save.png")
#         self.icon_save = self.icon_save.subsample(7)
#         self.icon_foldercapture = PhotoImage(file=f"{dir()}/assets/icon/openfolder.png")
#         self.icon_foldercapture = self.icon_foldercapture.subsample(7)

#         # Adding buttons
#         btn_camera      = tk.Button(self.tab1, text="OPEN CAMERA", compound=tk.TOP, command=self.open_camera, bg="grey", fg="black", image=self.icon_cameraon)
#         btn_camera.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

#         btn_cap_detect  = tk.Button(self.tab1, text="CAPTURE & DETECT", compound=tk.TOP, command=self.capture_and_detect, bg="grey", fg="black", image=self.icon_capture)
#         btn_cap_detect.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

#         btn_confirm     = tk.Button(self.tab1, text="CONFIRMATION", compound=tk.TOP, command=self.confirmation, bg="grey", fg="black", image=self.icon_foldercapture)
#         btn_confirm.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')

#         btn_save        = tk.Button(self.tab1, text="SAVE IMAGE", compound=tk.TOP, command=self.get_current_tab, bg="grey", fg="black", image=self.icon_save)
#         btn_save.grid(row=2, column=3, padx=10, pady=10, sticky='nsew')


#     # Function for button UI
#     def open_camera(self):
#         print("Open Camera button clicked")
#         self.camera.start()
#         self.update_canvas_livecam()

#     def capture_and_detect(self):
#         print("Capture & Detect button clicked")

#     def confirmation(self):
#         def save_value():
#             input_value = input_entry.get()
#             print(f"Input value saved: {input_value}")
#             confirmation_window.destroy()

#         # Create a new window
#         confirmation_window = tk.Toplevel(self.root)
#         confirmation_window.iconbitmap(f"{dir()}/assets/icon/dxicon.ico")
#         confirmation_window.title("Confirmation Detected Image!")
#         confirmation_window.geometry("300x150")

#         # Create a label and entry widget
#         input_label = tk.Label(confirmation_window, text="Input Number")
#         input_label.pack(pady=10)

#         input_entry = tk.Entry(confirmation_window)
#         input_entry.pack(pady=5)

#         # Create a save button
#         save_button = tk.Button(confirmation_window, text="save", command=save_value)
#         save_button.pack(pady=10)

#     def save_image(self):
#         print("Save Image button clicked")


#     # Function for backend
#     def update_canvas_livecam(self):
#         self.cam_frame = self.camera.update_frame()
#         self.img_cam = ImageTk.PhotoImage(image=self.cam_frame)
#         self.cam_canvas.create_image(0, 0, image=self.img_cam, anchor=tk.NW)
#         self.root.after(self.delay, self.update_canvas_livecam)
#     def get_current_tab(self):
#         current_tab = self.tab_control.select()
#         tab_index = self.tab_control.index(current_tab)
#         print(f"Tab yang terbuka adalah tab {tab_index + 1}")



# import tkinter as tk
# from tkinter import ttk, Menu, PhotoImage
# from PIL import Image, ImageTk
# from vizEngine.utils.root import dir

# class UI:
#     def __init__(self, tk_root, camera, detection, file_manager, measurement):
#         self.root = tk_root
#         self.root.iconbitmap(f"{dir()}/assets/icon/dxicon.ico")
        
#         self.root.title("VIZcap - Visual Inspection Cuptip")
#         self.root.geometry("800x600")

#         # Object for support function
#         self.camera_on = 0
#         self.camera = camera()
#         self.detection = detection
#         self.file_manager = file_manager
#         self.measurement = measurement
#         self.delay = 10

#         # Adding tab control
#         self.tab_control = ttk.Notebook(self.root)
#         self.tab1 = ttk.Frame(self.tab_control)
#         self.tab2 = ttk.Frame(self.tab_control)
#         self.tab_control.add(self.tab1, text='Detect')
#         self.tab_control.add(self.tab2, text='Measure')
#         self.tab_control.pack(expand=1, fill="both")
#         self.tab_control.bind("<<NotebookTabChanged>>", self.run_current_tab)

#         # Run UI
#         self.tab_detection()
#         self.tab_measure()

#         # Creating a menu bar
#         menu_bar = Menu(self.root)
#         self.root.config(menu=menu_bar)

#         # Adding file menu
#         file_menu = Menu(menu_bar, tearoff=0)
#         file_menu.add_command(label="Open")
#         file_menu.add_separator()
#         file_menu.add_command(label="Exit", command=self.root.quit)
#         menu_bar.add_cascade(label="File", menu=file_menu)

#         # Adding view menu
#         view_menu = Menu(menu_bar, tearoff=0)
#         menu_bar.add_cascade(label="View", menu=view_menu)

#         # Adding help menu
#         help_menu = Menu(menu_bar, tearoff=0)
#         menu_bar.add_cascade(label="Help", menu=help_menu)

#     def tab_detection(self):
#         # Object initialization camera
#         self.camera_on = 0

#         # Configuring grid layout for tab1
#         self.tab1.grid_rowconfigure(0, weight=1)
#         self.tab1.grid_rowconfigure(1, weight=4)
#         self.tab1.grid_rowconfigure(2, weight=1)
#         self.tab1.grid_columnconfigure(0, weight=1)
#         self.tab1.grid_columnconfigure(1, weight=1)
#         self.tab1.grid_columnconfigure(2, weight=1)
#         self.tab1.grid_columnconfigure(3, weight=1)

#         # Adding labels for image frames
#         label1 = tk.Label(self.tab1, text="CAMERA LIVE")
#         label1.grid(row=0, column=0, columnspan=2)
#         label2 = tk.Label(self.tab1, text="DETECTED IMAGE")
#         label2.grid(row=0, column=2, columnspan=2)

#         # Adding a frame container for the image frames to ensure equal size
#         frame_container = tk.Frame(self.tab1)
#         frame_container.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

#         # Configure grid in the frame container
#         frame_container.grid_rowconfigure(0, weight=1)
#         frame_container.grid_columnconfigure(0, weight=1)
#         frame_container.grid_columnconfigure(1, weight=1)

#         # Adding frames for images inside the container
#         frame1 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
#         frame1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
#         self.cam_canvas = tk.Canvas(frame1, width=640, height=480)
#         self.cam_canvas.pack(expand=True)
#         frame2 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
#         frame2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
#         self.res_canvas = tk.Canvas(frame2, width=640, height=480)
#         self.res_canvas.pack(expand=True)

#         # Configure for button icon
#         self.icon_cameraon = PhotoImage(file=f"{dir()}/assets/icon/cameraon.png")
#         self.icon_cameraon = self.icon_cameraon.subsample(10)
#         self.icon_cameraoff = PhotoImage(file=f"{dir()}/assets/icon/cameraoff.png")
#         self.icon_cameraoff = self.icon_cameraoff.subsample(10)
#         self.icon_capture = PhotoImage(file=f"{dir()}/assets/icon/capture.png")
#         self.icon_capture = self.icon_capture.subsample(7)
#         self.icon_save = PhotoImage(file=f"{dir()}/assets/icon/save.png")
#         self.icon_save = self.icon_save.subsample(7)
#         self.icon_foldercapture = PhotoImage(file=f"{dir()}/assets/icon/openfolder.png")
#         self.icon_foldercapture = self.icon_foldercapture.subsample(7)

#         # Adding buttons
#         self.btn_camera      = tk.Button(self.tab1, text="START CAMERA", compound=tk.TOP, command=self.camera_button, bg="grey", fg="black", image=self.icon_cameraon)
#         self.btn_camera.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
#         self.btn_cap_detect  = tk.Button(self.tab1, text="CAPTURE & DETECT", compound=tk.TOP, command=self.capture_and_detect, bg="grey", fg="black", image=self.icon_capture)
#         self.btn_cap_detect.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
#         self.btn_confirm     = tk.Button(self.tab1, text="CONFIRMATION", compound=tk.TOP, command=self.confirmation, bg="grey", fg="black", image=self.icon_foldercapture)
#         self.btn_confirm.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')
#         self.btn_save        = tk.Button(self.tab1, text="SAVE IMAGE", compound=tk.TOP, command=self.run_current_tab, bg="grey", fg="black", image=self.icon_save)
#         self.btn_save.grid(row=2, column=3, padx=10, pady=10, sticky='nsew')

#     def tab_measure(self):
#         # Configuring grid layout for tab2
#         self.tab2.grid_rowconfigure(0, weight=1)
#         self.tab2.grid_rowconfigure(1, weight=4)
#         self.tab2.grid_rowconfigure(2, weight=1)
#         self.tab2.grid_rowconfigure(3, weight=1)
#         self.tab2.grid_columnconfigure(0, weight=4)
#         self.tab2.grid_columnconfigure(1, weight=1)

#         # Adding a frame for the large image
#         frame3 = tk.Frame(self.tab2, bd=2, relief=tk.SUNKEN, bg='black')
#         frame3.grid(row=0, column=0, rowspan=3, padx=10, pady=10, sticky='nsew')

#         # Adding a frame for the measurement information
#         frame4 = tk.Frame(self.tab2, bd=2, relief=tk.SUNKEN)
#         frame4.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky='nsew')

#         # Adding labels to the measurement information frame
#         measure_label = tk.Label(frame4, text="Measure Surface")
#         measure_label.grid(row=0, column=0, sticky='w')
#         h_label = tk.Label(frame4, text="H: xxxx")
#         h_label.grid(row=1, column=0, sticky='w')
#         w_label = tk.Label(frame4, text="W: xxxx")
#         w_label.grid(row=2, column=0, sticky='w')
#         status_label = tk.Label(frame4, text="Status: xx")
#         status_label.grid(row=3, column=0, sticky='w')

#         # Adding buttons with equal size
#         button_frame = tk.Frame(self.tab2)
#         button_frame.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
#         button_frame.grid_rowconfigure(0, weight=1)
#         button_frame.grid_columnconfigure(0, weight=1)
#         button_frame.grid_columnconfigure(1, weight=1)

#         button5 = tk.Button(button_frame, text="BUTTON 1", bg="grey", fg="black")
#         button5.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
#         button6 = tk.Button(button_frame, text="BUTTON 2", bg="grey", fg="black")
#         button6.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
#         button7 = tk.Button(button_frame, text="BUTTON 3", bg="grey", fg="black")
#         button7.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
#         button8 = tk.Button(button_frame, text="BUTTON 4", bg="grey", fg="black")
#         button8.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')


#     # Function for button UI
#     def capture_and_detect(self):
#         print("Capture & Detect button clicked")

#     def confirmation(self):
#         def save_value():
#             input_value = input_entry.get()
#             print(f"Input value saved: {input_value}")
#             confirmation_window.destroy()

#         # Create a new window
#         confirmation_window = tk.Toplevel(self.root)
#         confirmation_window.iconbitmap(f"{dir()}/assets/icon/dxicon.ico")
#         confirmation_window.title("Confirmation Detected Image!")
#         confirmation_window.geometry("300x150")

#         # Create a label and entry widget
#         input_label = tk.Label(confirmation_window, text="Input Number")
#         input_label.pack(pady=10)

#         input_entry = tk.Entry(confirmation_window)
#         input_entry.pack(pady=5)

#         # Create a save button
#         save_button = tk.Button(confirmation_window, text="save", command=save_value)
#         save_button.pack(pady=10)

#     def save_image(self):
#         print("Save Image button clicked")


#     # Function for backend
#     # Function update canvas (for viedo in canvas)
#     def update_canvas_livecam(self):
#         if self.camera_on:
#             self.cam_frame = self.camera.update_frame()
#             self.img_cam = ImageTk.PhotoImage(image=self.cam_frame)
#             self.cam_canvas.create_image(0, 0, image=self.img_cam, anchor=tk.NW)
#             self.root.after(self.delay, self.update_canvas_livecam)

#     # Function for getting current tab and interlock camera
#     def run_current_tab(self, event):
#         current_tab = self.tab_control.select()
#         tab_index = self.tab_control.index(current_tab)
#         if tab_index == 0:
#             self.btn_camera.config(text="START CAMERA", image=self.icon_cameraon, command=self.camera_button)
#             self.camera.src_camera(0)
#             self.cam_canvas.delete("all")
#             if self.camera_on:
#                 self.camera.stop()
#                 self.camera_on = 0
#         elif tab_index == 1:
#             self.camera.src_camera(1)
#             self.camera.stop()
#             self.camera_on = 0

#     # Function for button camera open and close
#     def camera_button(self):
#         self.camera_on = not self.camera_on
#         if self.camera_on:
#             self.btn_camera.config(text="STOP CAMERA", image=self.icon_cameraoff, command=self.camera_button)
#             self.camera.start()
#             self.update_canvas_livecam()
#         else:
#             self.btn_camera.config(text="START CAMERA", image=self.icon_cameraon, command=self.camera_button)
#             self.camera.stop()
#             self.cam_canvas.delete("all")






        # for r in results:
        #     im_array = r.plot()
        #     im = Image.fromarray(im_array[..., ::-1])
        #     photo = ImageTk.PhotoImage(im)
        #     return im_array, photo
        # return None, None

    # def confirmation(self):
    #     def save_value():
    #         input_value = input_entry.get()
    #         print(f"Input value saved: {input_value}")
    #         confirmation_window.destroy()

    #     # Create a new window
    #     confirmation_window = tk.Toplevel(self.root)
    #     confirmation_window.iconbitmap(f"{dir()}/assets/icon/dxicon.ico")
    #     confirmation_window.title("Confirmation Detected Image!")
    #     confirmation_window.geometry("300x150")

    #     # Create a label and entry widget
    #     input_label = tk.Label(confirmation_window, text="Input Number")
    #     input_label.pack(pady=10)

    #     input_entry = tk.Entry(confirmation_window)
    #     input_entry.pack(pady=5)

    #     # Create a save button
    #     save_button = tk.Button(confirmation_window, text="save", command=save_value)
    #     save_button.pack(pady=10)


# def capture_and_detect(self):
    #     if self.camera_on:
    #         # self.img_path = self.camera.capture_image(f"{dir()}{self.cp['files']['save_raw']}")
    #         self.cap = self.camera.cap()
    #         print(self.cap)
    #         self.img_path = self.file_manager.save_raw(self.cap)
    #     try:
    #         print(self.img_path)
    #         # self.res_detect = self.detection.detect_objects(self.img_path)
    #         # self.res_canvas.create_image(0, 0, image=self.res_detect, anchor=tk.NW)
    #     except Exception as e:
    #         print(f"Error updating canvas livecam: {e}")


# class ConfirmationLogger:
#     def __init__(self, log_path):
#         self.log_path = log_path
#         self.filename = None
#         self.logger = logging.getLogger('CustomLogger')
#         self.logger.setLevel(logging.DEBUG)
#         self.initial_log_written = False
#         self.confirmation_counter = 1
#         self.log_file = None
#         self.fh = None
        
#     def _check_initial_log_written(self):
#         if not os.path.exists(self.log_file):
#             return False
#         with open(self.log_file, 'r') as file:
#             content = file.read()
#             if '.RAW_IMAGE_DIRECTORY' in content and '.CONFIRMATION_RES_IMAGE_DIRECTORY' in content and '.CONFIRMATION_LIST' in content:
#                 return True
#         return False
    
#     def _get_initial_confirmation_counter(self):
#         if not os.path.exists(self.log_file):
#             return 1
#         with open(self.log_file, 'r') as file:
#             content = file.read()
#             conf_lines = [line for line in content.split('\n') if line.startswith('CONF')]
#             return len(conf_lines) + 1
    
#     def log_name(self, name):
#         self.filename = name
#         self.log_file = f"{self.log_path}/{self.filename}.txt"
        
#         if self.fh:  # Remove the old file handler if it exists
#             self.logger.removeHandler(self.fh)
        
#         self.fh = logging.FileHandler(self.log_file)
#         self.fh.setLevel(logging.DEBUG)
#         formatter = logging.Formatter('%(message)s')
#         self.fh.setFormatter(formatter)
#         self.logger.addHandler(self.fh)
        
#         self.initial_log_written = self._check_initial_log_written()
#         self.confirmation_counter = self._get_initial_confirmation_counter()
    
#     def log_initial_info(self, raw_image_path, res_image_path):
#         if not self.initial_log_written:
#             self.logger.info(f'.RAW_IMAGE_DIRECTORY\n{raw_image_path}')
#             self.logger.info(f'.CONFIRMATION_RES_IMAGE_DIRECTORY\n{res_image_path}')
#             self.logger.info(f'.CONFIRMATION_LIST')
#             self.initial_log_written = True

#     def log_confirmation(self, judgement, object_number):
#         if not self.filename:
#             raise ValueError("Filename not set. Please call log_name() first.")
        
#         conf_number = self.confirmation_counter
#         self.logger.info(f'CONF{conf_number} JUDGEMENT--({judgement})--IN--OBJECTNUMBER--({object_number})')
#         self.confirmation_counter += 1




# import logging
# import os

# class ConfirmationLogger:
#     def __init__(self, log_path):
#         self.log_file = f"{log_path}/{self.filename}.txt"
#         self.logger = logging.getLogger('CustomLogger')
#         self.logger.setLevel(logging.DEBUG)
#         fh = logging.FileHandler(self.log_file)
#         fh.setLevel(logging.DEBUG)
#         formatter = logging.Formatter('%(message)s')
#         fh.setFormatter(formatter)
#         self.logger.addHandler(fh)
        
#         # Check if the log file already exists and contains the initial headers
#         self.initial_log_written = self._check_initial_log_written()
#         self.confirmation_counter = self._get_initial_confirmation_counter()
    
#     def _check_initial_log_written(self):
#         if not os.path.exists(self.log_file):
#             return False
#         with open(self.log_file, 'r') as file:
#             content = file.read()
#             if '.RAW_IMAGE_DIRECTORY' in content and '.CONFIRMATION_RES_IMAGE_DIRECTORY' in content and '.CONFIRMATION_LIST' in content:
#                 return True
#         return False
    
#     def _get_initial_confirmation_counter(self):
#         if not os.path.exists(self.log_file):
#             return 1
#         with open(self.log_file, 'r') as file:
#             content = file.read()
#             conf_lines = [line for line in content.split('\n') if line.startswith('CONF')]
#             return len(conf_lines) + 1
    
#     def log_name(self, name):
#         self.filename = name
    
#     def log_initial_info(self, raw_image_path, res_image_path):
#         if not self.initial_log_written:
#             self.logger.info(f'.RAW_IMAGE_DIRECTORY\n{raw_image_path}')
#             self.logger.info(f'.CONFIRMATION_RES_IMAGE_DIRECTORY\n{res_image_path}')
#             self.logger.info(f'.CONFIRMATION_LIST')
#             self.initial_log_written = True

#     def log_confirmation(self, judgement, object_number):
#         conf_number = self.confirmation_counter
#         self.logger.info(f'CONF{conf_number} JUDGEMENT--({judgement})--IN--OBJECTNUMBER--({object_number})')
#         self.confirmation_counter += 1



# def confirmation(self):
    #     def add_judgement(self):
    #         judgement = judgement_entry.get()
    #         object_number = object_number_entry.get()
    #         judgement_list.insert(tk.END, f"judge == {judgement} || obj_point == {object_number}")
    #         self.logger.log_confirmation(judgement, object_number)
        
    #     def finish_judgement():
    #         print("Judgement finished")
    #         judgement_window.destroy()
        
    #     def on_closing_judgement():
    #         if messagebox.askokcancel("Cancel", "Do you want to cancel confirm?"):
    #             judgement_window.destroy()

    #     # Create saving camera
    #     try:
    #         if self.res_img:
    #             self.confirm_img = self.file_manager.save_res(self.res_img, 'confirm')
    #     except Exception as e:
    #         print(f"Error saving confirm: {e}")

    #     # Create log file
    #     try:
    #         if self.raw_img and self.res_img:
    #             self.logger.log_name(self.raw_img[2])
    #             self.logger.log_initial_info(self.raw_img[1], self.confirm_img[1])
    #     except Exception as e:
    #         print(f"Error from log: {e}")

    #     # Create a new window
    #     judgement_window = tk.Toplevel(self.root)
    #     judgement_window.title("Confirmation Cuptip")
    #     judgement_window.geometry("750x300")

    #     # Image Name label
    #     image_name_label = tk.Label(judgement_window, text=f"Image Location: {self.raw_img[0]}", font=("Arial", 10, "bold"))
    #     image_name_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    #     # Judgement Actual label and entry
    #     judgement_label = tk.Label(judgement_window, text="Judgement Actual")
    #     judgement_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
    #     judgement_entry = tk.Entry(judgement_window)
    #     judgement_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

    #     # Object Number label and entry
    #     object_number_label = tk.Label(judgement_window, text="Object Number")
    #     object_number_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
    #     object_number_entry = tk.Entry(judgement_window)
    #     object_number_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

    #     # Add and Finish buttons
    #     add_button = tk.Button(judgement_window, text="Add", command=add_judgement(self))
    #     add_button.grid(row=3, column=0, padx=10, pady=10, sticky='e')
    #     finish_button = tk.Button(judgement_window, text="Finish", command=finish_judgement)
    #     finish_button.grid(row=3, column=1, padx=10, pady=10, sticky='w')

    #     # Added Judgement listbox
    #     judgement_list_label = tk.Label(judgement_window, text="Added Judgement:")
    #     judgement_list_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
    #     judgement_list = tk.Listbox(judgement_window, width=50, height=10)
    #     judgement_list.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    #     # Handling close window
    #     judgement_window.protocol("WM_DELETE_WINDOW", on_closing_judgement)






# import os
# import cv2
# import time
# from tkinter import filedialog, messagebox

# class FileManager:
#     def __init__(self, detection_save_path, captured_save_path):
#         self.detection_save_path = detection_save_path
#         self.captured_save_path = captured_save_path
#         self._ensure_directories()

#     def _ensure_directories(self):
#         os.makedirs(self.detection_save_path, exist_ok=True)
#         os.makedirs(self.captured_save_path, exist_ok=True)

#     def _save_image(self, frame, prefix, save_path):
#         if frame is not None:
#             timestamp = time.strftime("%Y%m%d_%H%M%S")
#             filename = f'{prefix}_{timestamp}.jpg'
#             output_filename = os.path.join(save_path, filename)
#             cv2.imwrite(output_filename, frame)
#             messagebox.showinfo("Information", f"Image saved in\n'{output_filename}'")
#         else:
#             messagebox.showwarning("Warning", "No image to save!")
#         return filename, output_filename

#     def save_raw(self, raw_frame):
#         return self._save_image(raw_frame, 'img_raw', self.captured_save_path)

#     def save_res(self, res_frame):
#         return self._save_image(res_frame, 'img_res', self.detection_save_path)

#     def open_folder(self):
#         file_paths = filedialog.askopenfilenames(
#             filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
#         )
#         return file_paths