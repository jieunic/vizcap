import tkinter as tk
from tkinter import ttk, Menu, PhotoImage, messagebox
from PIL import Image, ImageTk
from vizEngine.utils.root import dir

class UI:
    def __init__(self, tk_root, camera, detection, file_manager, measurement, config, logger):
        # Object for support function
        self.root = tk_root
        self.root.iconbitmap(f"{dir()}/assets/icon/dxicon.ico")
        self.root.title("VIZcap - Visual Inspection Cuptip")
        self.root.geometry("1400x700")
        self.camera_on = 0
        self.logger = logger
        self.cp = config
        self.cp.read(f"{dir()}/vizEngine/setup.cfg")
        self.camera = camera
        self.detection = detection
        self.file_manager = file_manager
        self.measurement = measurement
        self.delay = 10

        # Adding tab control
        self.tab_control = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='Detect')
        self.tab_control.add(self.tab2, text='Measure')
        self.tab_control.pack(expand=1, fill="both")
        self.tab_control.bind("<<NotebookTabChanged>>", self.run_current_tab)

        # Run UI
        self.tab_detection()
        self.tab_measure()

        # Creating a menu bar
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        # Adding file menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Adding view menu
        view_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="View", menu=view_menu)

        # Adding help menu
        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Handling Close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def tab_detection(self):
        # Object initialization camera
        self.camera_on = 0

        # Configuring grid layout for tab1
        self.tab1.grid_rowconfigure(0, weight=1)
        self.tab1.grid_rowconfigure(1, weight=4)
        self.tab1.grid_rowconfigure(2, weight=1)
        self.tab1.grid_columnconfigure(0, weight=1)
        self.tab1.grid_columnconfigure(1, weight=1)
        self.tab1.grid_columnconfigure(2, weight=1)
        self.tab1.grid_columnconfigure(3, weight=1)

        # Adding labels for image frames
        label1 = tk.Label(self.tab1, text="CAMERA LIVE")
        label1.grid(row=0, column=0, columnspan=2)
        label2 = tk.Label(self.tab1, text="DETECTED IMAGE")
        label2.grid(row=0, column=2, columnspan=2)

        # Adding a frame container for the image frames to ensure equal size
        frame_container = tk.Frame(self.tab1)
        frame_container.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # Configure grid in the frame container
        frame_container.grid_rowconfigure(0, weight=1)
        frame_container.grid_columnconfigure(0, weight=1)
        frame_container.grid_columnconfigure(1, weight=1)

        # Adding frames for images inside the container
        frame1 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
        frame1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.cam_canvas = tk.Canvas(frame1, width=640, height=480)
        self.cam_canvas.pack(expand=True)
        frame2 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
        frame2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        self.res_canvas = tk.Canvas(frame2, width=640, height=480)
        self.res_canvas.pack(expand=True)

        # Configure for button icon
        self.icon_cameraon = PhotoImage(file=f"{dir()}/assets/icon/cameraon.png")
        self.icon_cameraon = self.icon_cameraon.subsample(10)
        self.icon_cameraoff = PhotoImage(file=f"{dir()}/assets/icon/cameraoff.png")
        self.icon_cameraoff = self.icon_cameraoff.subsample(10)
        self.icon_capture = PhotoImage(file=f"{dir()}/assets/icon/capture.png")
        self.icon_capture = self.icon_capture.subsample(7)
        self.icon_save = PhotoImage(file=f"{dir()}/assets/icon/save.png")
        self.icon_save = self.icon_save.subsample(7)
        self.icon_foldercapture = PhotoImage(file=f"{dir()}/assets/icon/openfolder.png")
        self.icon_foldercapture = self.icon_foldercapture.subsample(7)

        # Adding buttons
        self.btn_camera      = tk.Button(self.tab1, text="START CAMERA", compound=tk.TOP, command=self.camera_button, bg="grey", fg="black", image=self.icon_cameraon)
        self.btn_camera.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        self.btn_cap_detect  = tk.Button(self.tab1, text="CAPTURE & DETECT", compound=tk.TOP, command=self.capture_and_detect, bg="grey", fg="black", image=self.icon_capture)
        self.btn_cap_detect.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
        self.btn_confirm     = tk.Button(self.tab1, text="CONFIRMATION", compound=tk.TOP, command=self.confirmation, bg="grey", fg="black", image=self.icon_foldercapture)
        self.btn_confirm.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')
        self.btn_save        = tk.Button(self.tab1, text="SAVE IMAGE", compound=tk.TOP, command=self.save_image, bg="grey", fg="black", image=self.icon_save)
        self.btn_save.grid(row=2, column=3, padx=10, pady=10, sticky='nsew')

    def tab_measure(self):
        # Configuring grid layout for tab2
        self.tab2.grid_rowconfigure(0, weight=1)
        self.tab2.grid_rowconfigure(1, weight=4)
        self.tab2.grid_rowconfigure(2, weight=1)
        self.tab2.grid_rowconfigure(3, weight=1)
        self.tab2.grid_columnconfigure(0, weight=4)
        self.tab2.grid_columnconfigure(1, weight=1)

        # Adding a frame for the large image
        frame3 = tk.Frame(self.tab2, bd=2, relief=tk.SUNKEN, bg='black')
        frame3.grid(row=0, column=0, rowspan=3, padx=10, pady=10, sticky='nsew')

        # Adding a frame for the measurement information
        frame4 = tk.Frame(self.tab2, bd=2, relief=tk.SUNKEN)
        frame4.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky='nsew')

        # Adding labels to the measurement information frame
        measure_label = tk.Label(frame4, text="Measure Surface")
        measure_label.grid(row=0, column=0, sticky='w')
        h_label = tk.Label(frame4, text="H: xxxx")
        h_label.grid(row=1, column=0, sticky='w')
        w_label = tk.Label(frame4, text="W: xxxx")
        w_label.grid(row=2, column=0, sticky='w')
        status_label = tk.Label(frame4, text="Status: xx")
        status_label.grid(row=3, column=0, sticky='w')

        # Adding buttons with equal size
        button_frame = tk.Frame(self.tab2)
        button_frame.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        button5 = tk.Button(button_frame, text="BUTTON 1", bg="grey", fg="black")
        button5.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        button6 = tk.Button(button_frame, text="BUTTON 2", bg="grey", fg="black")
        button6.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        button7 = tk.Button(button_frame, text="BUTTON 3", bg="grey", fg="black")
        button7.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        button8 = tk.Button(button_frame, text="BUTTON 4", bg="grey", fg="black")
        button8.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

    def confirmation(self):
        def add_judgement():
            judgement = judgement_entry.get()
            object_number = object_number_entry.get()
            judgement_list.insert(tk.END, f"judge == {judgement} || obj_point == {object_number}")
            self.logger.log_confirmation(judgement, object_number)
        
        def finish_judgement():
            print("Judgement finished")
            judgement_window.destroy()
            messagebox.showinfo("Information", f"Image successfully confirmed and saved!")
        
        def on_closing_judgement():
            if messagebox.askokcancel("Cancel", "Do you want to cancel confirm?"):
                judgement_window.destroy()

        # Create saving camera
        try:
            if self.res_img:
                self.confirm_img = self.file_manager.save_res(self.res_img[1], 'confirm')
        except Exception as e:
            print(f"Error saving confirm: {e}")

        # Create log file
        try:
            if self.raw_img and self.res_img:
                self.logger.log_name(self.raw_img[2])
                self.logger.log_initial_info(self.raw_img[1], self.confirm_img[1])
        except Exception as e:
            print(f"Error from log: {e}")

        # Create a new window
        judgement_window = tk.Toplevel(self.root)
        judgement_window.title("Confirmation Cuptip")
        judgement_window.geometry("350x350")

        # Image Name label
        image_name_label = tk.Label(judgement_window, text=f"Image Location: {self.raw_img[0]}", font=("Arial", 10, "bold"))
        image_name_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Judgement Actual label and entry
        judgement_label = tk.Label(judgement_window, text="Judgement Actual")
        judgement_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        judgement_entry = tk.Entry(judgement_window)
        judgement_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        # Object Number label and entry
        object_number_label = tk.Label(judgement_window, text="Object Number")
        object_number_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        object_number_entry = tk.Entry(judgement_window)
        object_number_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        # Add and Finish buttons
        add_button = tk.Button(judgement_window, text="Add", command=add_judgement)
        add_button.grid(row=3, column=0, padx=10, pady=10, sticky='e')
        finish_button = tk.Button(judgement_window, text="Finish", command=finish_judgement)
        finish_button.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        # Added Judgement listbox
        judgement_list_label = tk.Label(judgement_window, text="Added Judgement:")
        judgement_list_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        judgement_list = tk.Listbox(judgement_window, width=50, height=10)
        judgement_list.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        # Handling close window
        judgement_window.protocol("WM_DELETE_WINDOW", on_closing_judgement)


    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()


    # Function for button UI
    def capture_and_detect(self):
        if self.camera_on:
            self.cap = self.camera.cap()
            if self.cap is not None:
                self.raw_img = self.file_manager.save_raw(self.cap)
            else:
                print("Failed to capture frame")
        try:
            if self.raw_img:
                self.res_img = self.detection.detect_objects(self.raw_img[1])
                self.res_canvas.create_image(0, 0, image=self.res_img[0], anchor=tk.NW)
        except Exception as e:
            print(f"Error updating canvas livecam: {e}")



    def save_image(self):
        try:
            if self.res_img:
                self.save_img = self.file_manager.save_res(self.res_img[1], 'no_confirm')
        except Exception as e:
            print(f"Error saving: {e}")

    # Function for backend
    # Function update canvas (for viedo in canvas)
    def update_canvas_livecam(self):
        if self.camera_on:
            try:
                self.cam_frame = self.camera.update_frame()
                self.img_cam = ImageTk.PhotoImage(image=self.cam_frame)
                self.cam_canvas.create_image(0, 0, image=self.img_cam, anchor=tk.NW)
                self.root.after(self.delay, self.update_canvas_livecam)
            except Exception as e:
                print(f"Error updating canvas livecam: {e}")
                self.camera_on = 0

    # Function for getting current tab and interlock camera
    def run_current_tab(self, event):
        current_tab = self.tab_control.select()
        tab_index = self.tab_control.index(current_tab)
        print(f"Current tab index: {tab_index}")
        if tab_index == 0:
            self.btn_camera.config(text="START CAMERA", image=self.icon_cameraon, command=self.camera_button)
            try:
                self.camera.src_camera(0)
                self.cam_canvas.delete("all")
                if self.camera_on:
                    self.camera.stop()
                    self.camera_on = 0
            except Exception as e:
                print(f"Error accessing camera: {e}")
        elif tab_index == 1:
            try:
                self.camera.src_camera(1)
                self.camera.stop()
                self.camera_on = 0
            except Exception as e:
                print(f"Error accessing camera: {e}")

    # Function for button camera open and close
    def camera_button(self):
        self.camera_on = not self.camera_on
        if self.camera_on:
            try:
                self.btn_camera.config(text="STOP CAMERA", image=self.icon_cameraoff, command=self.camera_button)
                self.camera.start()
                self.update_canvas_livecam()
            except Exception as e:
                print(f"Error starting camera: {e}")
                self.camera_on = 0
        else:
            try:
                self.btn_camera.config(text="START CAMERA", image=self.icon_cameraon, command=self.camera_button)
                self.camera.stop()
                self.cam_canvas.delete("all")
            except Exception as e:
                print(f"Error stopping camera: {e}")