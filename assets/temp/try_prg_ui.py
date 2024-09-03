# import tkinter as tk
# from tkinter import ttk, Menu

# def open_camera():
#     print("Open Camera button clicked")

# def capture_and_detect():
#     print("Capture & Detect button clicked")

# def confirmation():
#     print("Confirmation button clicked")

# def save_image():
#     print("Save Image button clicked")

# root = tk.Tk()
# root.title("Camera Detection Interface")
# root.geometry("800x600")

# # Creating a menu bar
# menu_bar = Menu(root)
# root.config(menu=menu_bar)

# # Adding file menu
# file_menu = Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)

# # Adding view menu
# view_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="View", menu=view_menu)

# # Adding help menu
# help_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Help", menu=help_menu)

# # Adding tab control
# tab_control = ttk.Notebook(root)
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)

# tab_control.add(tab1, text='Detect')
# tab_control.add(tab2, text='Measure')
# tab_control.pack(expand=1, fill="both")

# # Configuring grid layout for tab1
# tab1.grid_rowconfigure(0, weight=1)
# tab1.grid_rowconfigure(1, weight=4)
# tab1.grid_rowconfigure(2, weight=1)
# tab1.grid_columnconfigure(0, weight=1)
# tab1.grid_columnconfigure(1, weight=1)
# tab1.grid_columnconfigure(2, weight=1)
# tab1.grid_columnconfigure(3, weight=1)

# # Adding labels for image frames
# label1 = tk.Label(tab1, text="CAMERA LIVE")
# label1.grid(row=0, column=0, columnspan=2, sticky='n')
# label2 = tk.Label(tab1, text="DETECTED IMAGE")
# label2.grid(row=0, column=2, columnspan=2, sticky='n')

# # Adding frames for images
# frame1 = tk.Frame(tab1, bd=2, relief=tk.SUNKEN, bg='black')
# frame1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
# frame2 = tk.Frame(tab1, bd=2, relief=tk.SUNKEN, bg='black')
# frame2.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky='nsew')

# # Adding buttons
# button1 = tk.Button(tab1, text="OPEN CAMERA", command=open_camera, bg="grey", fg="black")
# button1.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

# button2 = tk.Button(tab1, text="CAPTURE & DETECTkkkkkkkkkkkkkkkkkkkkkkk", command=capture_and_detect, bg="grey", fg="black")
# button2.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

# button3 = tk.Button(tab1, text="CONFIRMATION", command=confirmation, bg="grey", fg="black")
# button3.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')

# button4 = tk.Button(tab1, text="SAVE IMAGE", command=save_image, bg="grey", fg="black")
# button4.grid(row=2, column=3, padx=10, pady=10, sticky='nsew')

# root.mainloop()


# import tkinter as tk
# from tkinter import ttk, Menu

# def open_camera():
#     print("Open Camera button clicked")

# def capture_and_detect():
#     print("Capture & Detect button clicked")

# def confirmation():
#     print("Confirmation button clicked")

# def save_image():
#     print("Save Image button clicked")

# root = tk.Tk()
# root.title("Camera Detection Interface")
# root.geometry("800x600")

# # Creating a menu bar
# menu_bar = Menu(root)
# root.config(menu=menu_bar)

# # Adding file menu
# file_menu = Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)

# # Adding view menu
# view_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="View", menu=view_menu)

# # Adding help menu
# help_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Help", menu=help_menu)

# # Adding tab control
# tab_control = ttk.Notebook(root)
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)

# tab_control.add(tab1, text='Detect')
# tab_control.add(tab2, text='Measure')
# tab_control.pack(expand=1, fill="both")

# # Configuring grid layout for tab1
# tab1.grid_rowconfigure(0, weight=1)
# tab1.grid_rowconfigure(1, weight=4)
# tab1.grid_rowconfigure(2, weight=1)
# tab1.grid_columnconfigure(0, weight=1)
# tab1.grid_columnconfigure(1, weight=1)
# tab1.grid_columnconfigure(2, weight=1)
# tab1.grid_columnconfigure(3, weight=1)

# # Adding labels for image frames
# label1 = tk.Label(tab1, text="CAMERA LIVE")
# label1.grid(row=0, column=0, columnspan=2, sticky='n')
# label2 = tk.Label(tab1, text="DETECTED IMAGE")
# label2.grid(row=0, column=2, columnspan=2, sticky='n')

# # Adding a frame container for the image frames to ensure equal size
# frame_container = tk.Frame(tab1)
# frame_container.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

# # Configure grid in the frame container
# frame_container.grid_rowconfigure(0, weight=1)
# frame_container.grid_columnconfigure(0, weight=1)
# frame_container.grid_columnconfigure(1, weight=1)

# # Adding frames for images inside the container
# frame1 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
# frame1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
# frame2 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
# frame2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# # Adding buttons
# button1 = tk.Button(tab1, text="OPEN CAMERA", command=open_camera, bg="grey", fg="black")
# button1.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

# button2 = tk.Button(tab1, text="CAPTURE & DETECTkkkkkkkkkkkkkkkkkkkkk", command=capture_and_detect, bg="grey", fg="black")
# button2.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

# button3 = tk.Button(tab1, text="CONFIRMATION", command=confirmation, bg="grey", fg="black")
# button3.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')

# button4 = tk.Button(tab1, text="SAVE IMAGE", command=save_image, bg="grey", fg="black")
# button4.grid(row=2, column=3, padx=10, pady=10, sticky='nsew')

# root.mainloop()


# import tkinter as tk
# from tkinter import ttk, Menu

# def open_camera():
#     print("Open Camera button clicked")

# def capture_and_detect():
#     print("Capture & Detect button clicked")

# def confirmation():
#     def save_value():
#         input_value = input_entry.get()
#         print(f"Input value saved: {input_value}")
#         confirmation_window.destroy()

#     # Create a new window
#     confirmation_window = tk.Toplevel(root)
#     confirmation_window.title("Confirmation")
#     confirmation_window.geometry("300x150")

#     # Create a label and entry widget
#     input_label = tk.Label(confirmation_window, text="Input Number")
#     input_label.pack(pady=10)

#     input_entry = tk.Entry(confirmation_window)
#     input_entry.pack(pady=5)

#     # Create a save button
#     save_button = tk.Button(confirmation_window, text="save", command=save_value)
#     save_button.pack(pady=10)

# def save_image():
#     print("Save Image button clicked")

# root = tk.Tk()
# root.title("Camera Detection Interface")
# root.geometry("800x600")

# # Creating a menu bar
# menu_bar = Menu(root)
# root.config(menu=menu_bar)

# # Adding file menu
# file_menu = Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)

# # Adding view menu
# view_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="View", menu=view_menu)

# # Adding help menu
# help_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Help", menu=help_menu)

# # Adding tab control
# tab_control = ttk.Notebook(root)
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)

# tab_control.add(tab1, text='Detect')
# tab_control.add(tab2, text='Measure')
# tab_control.pack(expand=1, fill="both")

# # Configuring grid layout for tab1
# tab1.grid_rowconfigure(0, weight=1)
# tab1.grid_rowconfigure(1, weight=1)
# tab1.grid_rowconfigure(2, weight=4)
# tab1.grid_rowconfigure(3, weight=1)
# tab1.grid_columnconfigure(0, weight=1)
# tab1.grid_columnconfigure(1, weight=1)
# tab1.grid_columnconfigure(2, weight=1)
# tab1.grid_columnconfigure(3, weight=1)

# # Adding colored boxes with labels
# box_hello = tk.Label(tab1, bg='blue', width=2, height=1)
# box_hello.grid(row=0, column=0, padx=5, pady=5, sticky='e')
# label_hello = tk.Label(tab1, text="hello")
# label_hello.grid(row=0, column=1, padx=5, pady=5, sticky='w')

# box_hai = tk.Label(tab1, bg='orange', width=2, height=1)
# box_hai.grid(row=0, column=2, padx=5, pady=5, sticky='e')
# label_hai = tk.Label(tab1, text="hai")
# label_hai.grid(row=0, column=3, padx=5, pady=5, sticky='w')

# box_hehe = tk.Label(tab1, bg='red', width=2, height=1)
# box_hehe.grid(row=0, column=4, padx=5, pady=5, sticky='e')
# label_hehe = tk.Label(tab1, text="hehe")
# label_hehe.grid(row=0, column=5, padx=5, pady=5, sticky='w')

# # Adding labels for image frames
# label1 = tk.Label(tab1, text="CAMERA LIVE")
# label1.grid(row=1, column=0, columnspan=2, sticky='n')
# label2 = tk.Label(tab1, text="DETECTED IMAGE")
# label2.grid(row=1, column=2, columnspan=2, sticky='n')

# # Adding a frame container for the image frames to ensure equal size
# frame_container = tk.Frame(tab1)
# frame_container.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

# # Configure grid in the frame container
# frame_container.grid_rowconfigure(0, weight=1)
# frame_container.grid_columnconfigure(0, weight=1)
# frame_container.grid_columnconfigure(1, weight=1)

# # Adding frames for images inside the container
# frame1 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
# frame1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
# frame2 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
# frame2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# # Adding buttons
# button1 = tk.Button(tab1, text="OPEN CAMERA", command=open_camera, bg="grey", fg="black")
# button1.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

# button2 = tk.Button(tab1, text="CAPTURE & DETECT", command=capture_and_detect, bg="grey", fg="black")
# button2.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')

# button3 = tk.Button(tab1, text="CONFIRMATION", command=confirmation, bg="grey", fg="black")
# button3.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

# button4 = tk.Button(tab1, text="SAVE IMAGE", command=save_image, bg="grey", fg="black")
# button4.grid(row=3, column=3, padx=10, pady=10, sticky='nsew')

# root.mainloop()



# import tkinter as tk
# from tkinter import ttk, Menu

# def open_camera():
#     print("Open Camera button clicked")

# def capture_and_detect():
#     print("Capture & Detect button clicked")

# def confirmation():
#     def save_value():
#         input_value = input_entry.get()
#         print(f"Input value saved: {input_value}")
#         confirmation_window.destroy()

#     # Create a new window
#     confirmation_window = tk.Toplevel(root)
#     confirmation_window.title("Confirmation")
#     confirmation_window.geometry("300x150")

#     # Create a label and entry widget
#     input_label = tk.Label(confirmation_window, text="Input Number")
#     input_label.pack(pady=10)

#     input_entry = tk.Entry(confirmation_window)
#     input_entry.pack(pady=5)

#     # Create a save button
#     save_button = tk.Button(confirmation_window, text="save", command=save_value)
#     save_button.pack(pady=10)

# def save_image():
#     print("Save Image button clicked")

# root = tk.Tk()
# root.title("Camera Detection Interface")
# root.geometry("800x600")

# # Creating a menu bar
# menu_bar = Menu(root)
# root.config(menu=menu_bar)

# # Adding file menu
# file_menu = Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)

# # Adding view menu
# view_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="View", menu=view_menu)

# # Adding help menu
# help_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Help", menu=help_menu)

# # Adding tab control
# tab_control = ttk.Notebook(root)
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)

# tab_control.add(tab1, text='Detect')
# tab_control.add(tab2, text='Measure')
# tab_control.pack(expand=1, fill="both")

# # Configuring grid layout for tab1
# tab1.grid_rowconfigure(0, weight=1)
# tab1.grid_rowconfigure(1, weight=1)
# tab1.grid_rowconfigure(2, weight=4)
# tab1.grid_rowconfigure(3, weight=1)
# tab1.grid_columnconfigure(0, weight=1)
# tab1.grid_columnconfigure(1, weight=1)
# tab1.grid_columnconfigure(2, weight=1)
# tab1.grid_columnconfigure(3, weight=1)

# # Adding colored boxes with labels in a single row
# box_hello = tk.Label(tab1, bg='blue', width=2, height=1)
# box_hello.grid(row=0, column=0, sticky='e')
# label_hello = tk.Label(tab1, text="hello")
# label_hello.grid(row=0, column=1, sticky='w')

# box_hai = tk.Label(tab1, bg='orange', width=2, height=1)
# box_hai.grid(row=0, column=2, sticky='e')
# label_hai = tk.Label(tab1, text="hai")
# label_hai.grid(row=0, column=3, sticky='w')

# box_hehe = tk.Label(tab1, bg='red', width=2, height=1)
# box_hehe.grid(row=0, column=4, sticky='e')
# label_hehe = tk.Label(tab1, text="hehe")
# label_hehe.grid(row=0, column=5, sticky='w')

# # Adding labels for image frames
# label1 = tk.Label(tab1, text="CAMERA LIVE")
# label1.grid(row=1, column=0, columnspan=2, sticky='n')
# label2 = tk.Label(tab1, text="DETECTED IMAGE")
# label2.grid(row=1, column=2, columnspan=2, sticky='n')

# # Adding a frame container for the image frames to ensure equal size
# frame_container = tk.Frame(tab1)
# frame_container.grid(row=2, column=0, columnspan=4, padx=10, pady=5, sticky='nsew')

# # Configure grid in the frame container
# frame_container.grid_rowconfigure(0, weight=1)
# frame_container.grid_columnconfigure(0, weight=1)
# frame_container.grid_columnconfigure(1, weight=1)

# # Adding frames for images inside the container
# frame1 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
# frame1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
# frame2 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
# frame2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# # Adding buttons
# button1 = tk.Button(tab1, text="OPEN CAMERA", command=open_camera, bg="grey", fg="black")
# button1.grid(row=3, column=0, padx=10, pady=5, sticky='nsew')

# button2 = tk.Button(tab1, text="CAPTURE & DETECT", command=capture_and_detect, bg="grey", fg="black")
# button2.grid(row=3, column=1, padx=10, pady=5, sticky='nsew')

# button3 = tk.Button(tab1, text="CONFIRMATION", command=confirmation, bg="grey", fg="black")
# button3.grid(row=3, column=2, padx=10, pady=5, sticky='nsew')

# button4 = tk.Button(tab1, text="SAVE IMAGE", command=save_image, bg="grey", fg="black")
# button4.grid(row=3, column=3, padx=10, pady=5, sticky='nsew')

# root.mainloop()


# import tkinter as tk
# from tkinter import ttk

# # Fungsi untuk mendapatkan indeks tab yang terbuka
# def get_current_tab():
#     current_tab = notebook.select()
#     tab_index = notebook.index(current_tab)
#     print(f"Tab yang terbuka adalah tab {tab_index + 1}")

# # Membuat jendela utama
# root = tk.Tk()
# root.title("Notebook Example")

# # Membuat objek Notebook
# notebook = ttk.Notebook(root)
# notebook.pack(padx=10, pady=10)

# # Menambahkan beberapa tab ke dalam notebook
# tab1 = tk.Frame(notebook, width=300, height=200, bg='white')
# tab2 = tk.Frame(notebook, width=300, height=200, bg='white')
# tab3 = tk.Frame(notebook, width=300, height=200, bg='white')

# notebook.add(tab1, text='Tab 1')
# notebook.add(tab2, text='Tab 2')
# notebook.add(tab3, text='Tab 3')

# # Menambahkan tombol untuk mengecek tab yang terbuka
# btn = tk.Button(root, text="Cek Tab Sekarang", command=get_current_tab)
# btn.pack(pady=10)

# # Menjalankan loop utama
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk

# # Fungsi untuk mendapatkan indeks tab yang terbuka
# def get_current_tab(event):
#     current_tab = notebook.select()
#     tab_index = notebook.index(current_tab)
#     print(f"Tab yang terbuka adalah tab {tab_index + 1}")

# # Membuat jendela utama
# root = tk.Tk()
# root.title("Notebook Example")

# # Membuat objek Notebook
# notebook = ttk.Notebook(root)
# notebook.pack(padx=10, pady=10)

# # Menambahkan beberapa tab ke dalam notebook
# tab1 = tk.Frame(notebook, width=300, height=200, bg='white')
# tab2 = tk.Frame(notebook, width=300, height=200, bg='white')
# tab3 = tk.Frame(notebook, width=300, height=200, bg='white')

# notebook.add(tab1, text='Tab 1')
# notebook.add(tab2, text='Tab 2')
# notebook.add(tab3, text='Tab 3')

# # Bind event perubahan tab ke fungsi get_current_tab
# notebook.bind("<<NotebookTabChanged>>", get_current_tab)

# # Menjalankan loop utama
# root.mainloop()



# import tkinter as tk
# from tkinter import ttk, Menu

# def open_camera():
#     print("Open Camera button clicked")

# def capture_and_detect():
#     print("Capture & Detect button clicked")

# def confirmation():
#     def save_value():
#         input_value = input_entry.get()
#         print(f"Input value saved: {input_value}")
#         confirmation_window.destroy()

#     # Create a new window
#     confirmation_window = tk.Toplevel(root)
#     confirmation_window.title("Confirmation")
#     confirmation_window.geometry("300x150")

#     # Create a label and entry widget
#     input_label = tk.Label(confirmation_window, text="Input Number")
#     input_label.pack(pady=10)

#     input_entry = tk.Entry(confirmation_window)
#     input_entry.pack(pady=5)

#     # Create a save button
#     save_button = tk.Button(confirmation_window, text="save", command=save_value)
#     save_button.pack(pady=10)

# def save_image():
#     print("Save Image button clicked")

# root = tk.Tk()
# root.title("Camera Detection Interface")
# root.geometry("800x600")

# # Creating a menu bar
# menu_bar = Menu(root)
# root.config(menu=menu_bar)

# # Adding file menu
# file_menu = Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)

# # Adding view menu
# view_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="View", menu=view_menu)

# # Adding help menu
# help_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Help", menu=help_menu)

# # Adding tab control
# tab_control = ttk.Notebook(root)
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)

# tab_control.add(tab1, text='Detect')
# tab_control.add(tab2, text='Measure')
# tab_control.pack(expand=1, fill="both")

# # Configuring grid layout for tab1
# tab1.grid_rowconfigure(0, weight=1)
# tab1.grid_rowconfigure(1, weight=1)
# tab1.grid_rowconfigure(2, weight=4)
# tab1.grid_rowconfigure(3, weight=1)
# tab1.grid_columnconfigure(0, weight=1)
# tab1.grid_columnconfigure(1, weight=1)
# tab1.grid_columnconfigure(2, weight=1)
# tab1.grid_columnconfigure(3, weight=1)

# # Adding colored boxes with labels in a single row
# box_hello = tk.Label(tab1, bg='blue', width=2, height=1)
# box_hello.grid(row=0, column=0, sticky='e')
# label_hello = tk.Label(tab1, text="hello")
# label_hello.grid(row=0, column=1, sticky='w')

# box_hai = tk.Label(tab1, bg='orange', width=2, height=1)
# box_hai.grid(row=0, column=2, sticky='e')
# label_hai = tk.Label(tab1, text="hai")
# label_hai.grid(row=0, column=3, sticky='w')

# box_hehe = tk.Label(tab1, bg='red', width=2, height=1)
# box_hehe.grid(row=0, column=4, sticky='e')
# label_hehe = tk.Label(tab1, text="hehe")
# label_hehe.grid(row=0, column=5, sticky='w')

# # Adding labels for image frames
# label1 = tk.Label(tab1, text="CAMERA LIVE")
# label1.grid(row=1, column=0, columnspan=2, sticky='n')
# label2 = tk.Label(tab1, text="DETECTED IMAGE")
# label2.grid(row=1, column=2, columnspan=2, sticky='n')

# # Adding a frame container for the image frames to ensure equal size
# frame_container = tk.Frame(tab1)
# frame_container.grid(row=2, column=0, columnspan=4, padx=10, pady=5, sticky='nsew')

# # Configure grid in the frame container
# frame_container.grid_rowconfigure(0, weight=1)
# frame_container.grid_columnconfigure(0, weight=1)
# frame_container.grid_columnconfigure(1, weight=1)

# # Adding frames for images inside the container
# frame1 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
# frame1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
# frame2 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
# frame2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# # Adding buttons
# button1 = tk.Button(tab1, text="OPEN CAMERA", command=open_camera, bg="grey", fg="black")
# button1.grid(row=3, column=0, padx=10, pady=5, sticky='nsew')

# button2 = tk.Button(tab1, text="CAPTURE & DETECT", command=capture_and_detect, bg="grey", fg="black")
# button2.grid(row=3, column=1, padx=10, pady=5, sticky='nsew')

# button3 = tk.Button(tab1, text="CONFIRMATION", command=confirmation, bg="grey", fg="black")
# button3.grid(row=3, column=2, padx=10, pady=5, sticky='nsew')

# button4 = tk.Button(tab1, text="SAVE IMAGE", command=save_image, bg="grey", fg="black")
# button4.grid(row=3, column=3, padx=10, pady=5, sticky='nsew')

# # Configuring grid layout for tab2
# tab2.grid_rowconfigure(0, weight=1)
# tab2.grid_rowconfigure(1, weight=4)
# tab2.grid_rowconfigure(2, weight=1)
# tab2.grid_columnconfigure(0, weight=4)
# tab2.grid_columnconfigure(1, weight=1)

# # Adding a frame for the large image
# frame3 = tk.Frame(tab2, bd=2, relief=tk.SUNKEN, bg='black')
# frame3.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky='nsew')

# # Adding a frame for the measurement information
# frame4 = tk.Frame(tab2, bd=2, relief=tk.SUNKEN)
# frame4.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# # Adding labels to the measurement information frame
# measure_label = tk.Label(frame4, text="Measure Surface")
# measure_label.grid(row=0, column=0, sticky='w')
# h_label = tk.Label(frame4, text="H: xxxx")
# h_label.grid(row=1, column=0, sticky='w')
# w_label = tk.Label(frame4, text="W: xxxx")
# w_label.grid(row=2, column=0, sticky='w')
# status_label = tk.Label(frame4, text="Status: xx")
# status_label.grid(row=3, column=0, sticky='w')

# # Adding buttons
# button5 = tk.Button(tab2, text="BUTTON 1", bg="grey", fg="black")
# button5.grid(row=2, column=1, padx=5, pady=5, sticky='nsew')

# button6 = tk.Button(tab2, text="BUTTON 2", bg="grey", fg="black")
# button6.grid(row=2, column=2, padx=5, pady=5, sticky='nsew')

# button7 = tk.Button(tab2, text="BUTTON 3", bg="grey", fg="black")
# button7.grid(row=3, column=1, padx=5, pady=5, sticky='nsew')

# button8 = tk.Button(tab2, text="BUTTON 4", bg="grey", fg="black")
# button8.grid(row=3, column=2, padx=5, pady=5, sticky='nsew')

# root.mainloop()


# import tkinter as tk
# from tkinter import ttk, Menu

# def open_camera():
#     print("Open Camera button clicked")

# def capture_and_detect():
#     print("Capture & Detect button clicked")

# def confirmation():
#     def save_value():
#         input_value = input_entry.get()
#         print(f"Input value saved: {input_value}")
#         confirmation_window.destroy()

#     # Create a new window
#     confirmation_window = tk.Toplevel(root)
#     confirmation_window.title("Confirmation")
#     confirmation_window.geometry("300x150")

#     # Create a label and entry widget
#     input_label = tk.Label(confirmation_window, text="Input Number")
#     input_label.pack(pady=10)

#     input_entry = tk.Entry(confirmation_window)
#     input_entry.pack(pady=5)

#     # Create a save button
#     save_button = tk.Button(confirmation_window, text="save", command=save_value)
#     save_button.pack(pady=10)

# def save_image():
#     print("Save Image button clicked")

# root = tk.Tk()
# root.title("Camera Detection Interface")
# root.geometry("800x600")

# # Creating a menu bar
# menu_bar = Menu(root)
# root.config(menu=menu_bar)

# # Adding file menu
# file_menu = Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)

# # Adding view menu
# view_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="View", menu=view_menu)

# # Adding help menu
# help_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Help", menu=help_menu)

# # Adding tab control
# tab_control = ttk.Notebook(root)
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)

# tab_control.add(tab1, text='Detect')
# tab_control.add(tab2, text='Measure')
# tab_control.pack(expand=1, fill="both")

# # Configuring grid layout for tab1
# tab1.grid_rowconfigure(0, weight=1)
# tab1.grid_rowconfigure(1, weight=1)
# tab1.grid_rowconfigure(2, weight=4)
# tab1.grid_rowconfigure(3, weight=1)
# tab1.grid_columnconfigure(0, weight=1)
# tab1.grid_columnconfigure(1, weight=1)
# tab1.grid_columnconfigure(2, weight=1)
# tab1.grid_columnconfigure(3, weight=1)

# # Adding colored boxes with labels in a single row
# box_hello = tk.Label(tab1, bg='blue', width=2, height=1)
# box_hello.grid(row=0, column=0, sticky='e')
# label_hello = tk.Label(tab1, text="hello")
# label_hello.grid(row=0, column=1, sticky='w')

# box_hai = tk.Label(tab1, bg='orange', width=2, height=1)
# box_hai.grid(row=0, column=2, sticky='e')
# label_hai = tk.Label(tab1, text="hai")
# label_hai.grid(row=0, column=3, sticky='w')

# box_hehe = tk.Label(tab1, bg='red', width=2, height=1)
# box_hehe.grid(row=0, column=4, sticky='e')
# label_hehe = tk.Label(tab1, text="hehe")
# label_hehe.grid(row=0, column=5, sticky='w')

# # Adding labels for image frames
# label1 = tk.Label(tab1, text="CAMERA LIVE")
# label1.grid(row=1, column=0, columnspan=2, sticky='n')
# label2 = tk.Label(tab1, text="DETECTED IMAGE")
# label2.grid(row=1, column=2, columnspan=2, sticky='n')

# # Adding a frame container for the image frames to ensure equal size
# frame_container = tk.Frame(tab1)
# frame_container.grid(row=2, column=0, columnspan=4, padx=10, pady=5, sticky='nsew')

# # Configure grid in the frame container
# frame_container.grid_rowconfigure(0, weight=1)
# frame_container.grid_columnconfigure(0, weight=1)
# frame_container.grid_columnconfigure(1, weight=1)

# # Adding frames for images inside the container
# frame1 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
# frame1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
# frame2 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
# frame2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# # Adding buttons
# button1 = tk.Button(tab1, text="OPEN CAMERA", command=open_camera, bg="grey", fg="black")
# button1.grid(row=3, column=0, padx=10, pady=5, sticky='nsew')

# button2 = tk.Button(tab1, text="CAPTURE & DETECT", command=capture_and_detect, bg="grey", fg="black")
# button2.grid(row=3, column=1, padx=10, pady=5, sticky='nsew')

# button3 = tk.Button(tab1, text="CONFIRMATION", command=confirmation, bg="grey", fg="black")
# button3.grid(row=3, column=2, padx=10, pady=5, sticky='nsew')

# button4 = tk.Button(tab1, text="SAVE IMAGE", command=save_image, bg="grey", fg="black")
# button4.grid(row=3, column=3, padx=10, pady=5, sticky='nsew')

# # Configuring grid layout for tab2
# tab2.grid_rowconfigure(0, weight=1)
# tab2.grid_rowconfigure(1, weight=4)
# tab2.grid_rowconfigure(2, weight=1)
# tab2.grid_rowconfigure(3, weight=1)
# tab2.grid_columnconfigure(0, weight=4)
# tab2.grid_columnconfigure(1, weight=1)

# # Adding a frame for the large image
# frame3 = tk.Frame(tab2, bd=2, relief=tk.SUNKEN, bg='black')
# frame3.grid(row=0, column=0, rowspan=3, padx=10, pady=10, sticky='nsew')

# # Adding a frame for the measurement information
# frame4 = tk.Frame(tab2, bd=2, relief=tk.SUNKEN)
# frame4.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky='nsew')

# # Adding labels to the measurement information frame
# measure_label = tk.Label(frame4, text="Measure Surface")
# measure_label.grid(row=0, column=0, sticky='w')
# h_label = tk.Label(frame4, text="H: xxxx")
# h_label.grid(row=1, column=0, sticky='w')
# w_label = tk.Label(frame4, text="W: xxxx")
# w_label.grid(row=2, column=0, sticky='w')
# status_label = tk.Label(frame4, text="Status: xx")
# status_label.grid(row=3, column=0, sticky='w')

# # Adding buttons with equal size
# button_frame = tk.Frame(tab2)
# button_frame.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
# button_frame.grid_rowconfigure(0, weight=1)
# button_frame.grid_columnconfigure(0, weight=1)
# button_frame.grid_columnconfigure(1, weight=1)

# button5 = tk.Button(button_frame, text="BUTTON 1", bg="grey", fg="black")
# button5.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

# button6 = tk.Button(button_frame, text="BUTTON 2", bg="grey", fg="black")
# button6.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

# button7 = tk.Button(button_frame, text="BUTTON 3", bg="grey", fg="black")
# button7.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

# button8 = tk.Button(button_frame, text="BUTTON 4", bg="grey", fg="black")
# button8.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

# root.mainloop()



# import tkinter as tk
# from tkinter import ttk, Menu

# def open_camera():
#     print("Open Camera button clicked")

# def capture_and_detect():
#     print("Capture & Detect button clicked")

# def confirmation():
#     def save_value():
#         input_value = input_entry.get()
#         print(f"Input value saved: {input_value}")
#         confirmation_window.destroy()

#     # Create a new window
#     confirmation_window = tk.Toplevel(root)
#     confirmation_window.title("Confirmation")
#     confirmation_window.geometry("300x150")

#     # Create a label and entry widget
#     input_label = tk.Label(confirmation_window, text="Input Number")
#     input_label.pack(pady=10)

#     input_entry = tk.Entry(confirmation_window)
#     input_entry.pack(pady=5)

#     # Create a save button
#     save_button = tk.Button(confirmation_window, text="save", command=save_value)
#     save_button.pack(pady=10)

# def save_image():
#     print("Save Image button clicked")

# root = tk.Tk()
# root.title("Camera Detection Interface")
# root.geometry("800x600")

# # Creating a menu bar
# menu_bar = Menu(root)
# root.config(menu=menu_bar)

# # Adding file menu
# file_menu = Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)

# # Adding view menu
# view_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="View", menu=view_menu)

# # Adding help menu
# help_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Help", menu=help_menu)

# # Adding tab control
# tab_control = ttk.Notebook(root)
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)

# tab_control.add(tab1, text='Detect')
# tab_control.add(tab2, text='Measure')
# tab_control.pack(expand=1, fill="both")

# # Configuring grid layout for tab1
# tab1.grid_rowconfigure(0, weight=1)
# tab1.grid_rowconfigure(1, weight=1)
# tab1.grid_rowconfigure(2, weight=4)
# tab1.grid_rowconfigure(3, weight=1)
# tab1.grid_columnconfigure(0, weight=1)
# tab1.grid_columnconfigure(1, weight=1)
# tab1.grid_columnconfigure(2, weight=1)
# tab1.grid_columnconfigure(3, weight=1)
# tab1.grid_columnconfigure(4, weight=1)
# tab1.grid_columnconfigure(5, weight=1)

# # Adding colored boxes with labels in a single row
# box_hello = tk.Label(tab1, bg='blue', width=2, height=1)
# box_hello.grid(row=0, column=0, sticky='e')
# label_hello = tk.Label(tab1, text="hello")
# label_hello.grid(row=0, column=1, sticky='w')

# box_hai = tk.Label(tab1, bg='orange', width=2, height=1)
# box_hai.grid(row=0, column=2, sticky='e')
# label_hai = tk.Label(tab1, text="hai")
# label_hai.grid(row=0, column=3, sticky='w')

# box_hehe = tk.Label(tab1, bg='red', width=2, height=1)
# box_hehe.grid(row=0, column=4, sticky='e')
# label_hehe = tk.Label(tab1, text="hehe")
# label_hehe.grid(row=0, column=5, sticky='w')

# # Adding labels for image frames
# label1 = tk.Label(tab1, text="CAMERA LIVE")
# label1.grid(row=1, column=0, columnspan=2, sticky='n')
# label2 = tk.Label(tab1, text="DETECTED IMAGE")
# label2.grid(row=1, column=2, columnspan=2, sticky='n')

# # Adding a frame container for the image frames to ensure equal size
# frame_container = tk.Frame(tab1)
# frame_container.grid(row=2, column=0, columnspan=6, padx=10, pady=5, sticky='nsew')

# # Configure grid in the frame container
# frame_container.grid_rowconfigure(0, weight=1)
# frame_container.grid_columnconfigure(0, weight=1)
# frame_container.grid_columnconfigure(1, weight=1)

# # Adding frames for images inside the container
# frame1 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
# frame1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
# frame2 = tk.Frame(frame_container, bd=2, relief=tk.SUNKEN, bg='black')
# frame2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# # Adding buttons
# button1 = tk.Button(tab1, text="OPEN CAMERA", command=open_camera, bg="grey", fg="black")
# button1.grid(row=3, column=0, padx=10, pady=5, sticky='nsew')

# button2 = tk.Button(tab1, text="CAPTURE & DETECT", command=capture_and_detect, bg="grey", fg="black")
# button2.grid(row=3, column=1, padx=10, pady=5, sticky='nsew')

# button3 = tk.Button(tab1, text="CONFIRMATION", command=confirmation, bg="grey", fg="black")
# button3.grid(row=3, column=2, padx=10, pady=5, sticky='nsew')

# button4 = tk.Button(tab1, text="SAVE IMAGE", command=save_image, bg="grey", fg="black")
# button4.grid(row=3, column=3, padx=10, pady=5, sticky='nsew')

# # Configuring grid layout for tab2
# tab2.grid_rowconfigure(0, weight=1)
# tab2.grid_rowconfigure(1, weight=4)
# tab2.grid_rowconfigure(2, weight=1)
# tab2.grid_rowconfigure(3, weight=1)
# tab2.grid_columnconfigure(0, weight=4)
# tab2.grid_columnconfigure(1, weight=1)

# # Adding a frame for the large image
# frame3 = tk.Frame(tab2, bd=2, relief=tk.SUNKEN, bg='black')
# frame3.grid(row=0, column=0, rowspan=3, padx=10, pady=10, sticky='nsew')

# # Adding a frame for the measurement information
# frame4 = tk.Frame(tab2, bd=2, relief=tk.SUNKEN)
# frame4.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky='nsew')

# # Adding labels to the measurement information frame
# measure_label = tk.Label(frame4, text="Measure Surface")
# measure_label.grid(row=0, column=0, sticky='w')
# h_label = tk.Label(frame4, text="H: xxxx")
# h_label.grid(row=1, column=0, sticky='w')
# w_label = tk.Label(frame4, text="W: xxxx")
# w_label.grid(row=2, column=0, sticky='w')
# status_label = tk.Label(frame4, text="Status: xx")
# status_label.grid(row=3, column=0, sticky='w')

# # Adding buttons with equal size
# button_frame = tk.Frame(tab2)
# button_frame.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
# button_frame.grid_rowconfigure(0, weight=1)
# button_frame.grid_columnconfigure(0, weight=1)
# button_frame.grid_columnconfigure(1, weight=1)

# button5 = tk.Button(button_frame, text="BUTTON 1", bg="grey", fg="black")
# button5.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

# button6 = tk.Button(button_frame, text="BUTTON 2", bg="grey", fg="black")
# button6.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

# button7 = tk.Button(button_frame, text="BUTTON 3", bg="grey", fg="black")
# button7.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

# button8 = tk.Button(button_frame, text="BUTTON 4", bg="grey", fg="black")
# button8.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

# root.mainloop()






# import tkinter as tk
# from tkinter import ttk

# def open_judgement_window():
#     def add_judgement():
#         judgement = judgement_entry.get()
#         object_number = object_number_entry.get()
#         judgement_list.insert(tk.END, f"Judge '{judgement}' Object Number '{object_number}'")
    
#     def finish_judgement():
#         # Here you can add code to handle the finish event
#         print("Judgement finished")
#         judgement_window.destroy()

#     # Create a new window
#     judgement_window = tk.Toplevel(root)
#     judgement_window.title("Judgement Window")
#     judgement_window.geometry("400x300")

#     # Image Name label
#     image_name_label = tk.Label(judgement_window, text="Image Name: xxxxx", font=("Arial", 12, "bold"))
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
#     add_button = tk.Button(judgement_window, text="Add", command=add_judgement)
#     add_button.grid(row=3, column=0, padx=10, pady=10, sticky='e')
#     finish_button = tk.Button(judgement_window, text="Finish", command=finish_judgement)
#     finish_button.grid(row=3, column=1, padx=10, pady=10, sticky='w')

#     # Added Judgement listbox
#     judgement_list_label = tk.Label(judgement_window, text="Added Judgement:")
#     judgement_list_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
#     judgement_list = tk.Listbox(judgement_window, width=50, height=10)
#     judgement_list.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# # Main window
# root = tk.Tk()
# root.title("Main Window")
# root.geometry("400x200")

# # Button to open the judgement window
# open_judgement_button = tk.Button(root, text="Open Judgement Window", command=open_judgement_window)
# open_judgement_button.pack(pady=20)

# root.mainloop()






import tkinter as tk
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Contoh Status Window")

# Mengikat event WM_DELETE_WINDOW dengan fungsi on_closing
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
