#Librerias necesarias
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, master):
        #Ventana contenedora o principal
        self.master = master
        self.master.title("Visualizador de imágenes")
        self.zoom_factor_1 = 1.0
        self.zoom_factor_2 = 1.0
        self.active_image = 1
        self.drawing = False
        self.start_x = None
        self.start_y = None

        # Asociacion de evento rueda
        self.master.bind("<MouseWheel>", self.zoom_with_mouse_wheel)

        #Pb para abrir imagenes
        self.btn_open_1 = tk.Button(master, text="Abrir imagen 1", command=lambda: self.open_image(1))
        self.btn_open_1.pack(side="left", padx=(5, 10), pady=10)

        self.btn_open_2 = tk.Button(master, text="Abrir imagen 2", command=lambda: self.open_image(2))
        self.btn_open_2.pack(side="left", padx=(5, 10), pady=10)

        #Creacion del frame
        self.frame = tk.Frame(master)
        self.frame.pack()

        #Desplazamientos
        self.scrollbar_y = tk.Scrollbar(self.frame, orient="vertical")
        self.scrollbar_y.pack(side="right", fill="y")

        self.scrollbar_x = tk.Scrollbar(self.frame, orient="horizontal")
        self.scrollbar_x.pack(side="bottom", fill="x")

        # canvas para images
        self.canvas_1 = tk.Canvas(self.frame, yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)
        self.canvas_1.pack(side="left", expand=True, fill="both")

        self.canvas_2 = tk.Canvas(self.frame, yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)
        self.canvas_2.pack(side="left", expand=True, fill="both")

        #etiquetas
        self.label_1 = tk.Label(master, text="Imagen 1")
        self.label_1.pack(side="left", padx=5)

        self.label_2 = tk.Label(master, text="Imagen 2")
        self.label_2.pack(side="left", padx=5)

        # Botón para dibujar
        self.btn_draw = tk.Button(master, text="Dibujar", command=self.toggle_drawing)
        self.btn_draw.pack(side="top")

        # pb quit
        self.btn_exit = tk.Button(master, text="Salir", command=master.quit)
        self.btn_exit.pack(pady=10)

        self.image_1 = None
        self.image_2 = None

        self.mastil = self.canvas_1.create_line(0, 0, 0, 0, fill="black", width=2)

        self.bind_drawing_events()

    def toggle_drawing(self):
        self.drawing = not self.drawing
        if self.drawing:
            self.btn_draw.config(text="Detener dibujo")
        else:
            self.btn_draw.config(text="Dibujar")

    def start_drag(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def drag(self, event):
        if self.active_image == 1:
            self.canvas_1.scan_dragto(event.x - self.start_x, event.y - self.start_y, gain=1)
        else:
            self.canvas_2.scan_dragto(event.x - self.start_x, event.y - self.start_y, gain=1)
        self.start_x = event.x
        self.start_y = event.y

    def bind_drawing_events(self):
        self.canvas_1.bind("<B1-Motion>", self.toggle_drawing)
        self.canvas_2.bind("<B1-Motion>", self.toggle_drawing)

    def draw_circle(self, event):
        if self.drawing:
            x, y = event.x, event.y
            radius = 10
            if self.active_image == 1:
                self.canvas_1.create_oval(x-radius, y-radius, x+radius, y+radius, outline="red", width=2)
            else:
                self.canvas_2.create_oval(x-radius, y-radius, x+radius, y+radius, outline="red", width=2)

    def open_image(self, image_number):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png")])
        if file_path:
            if image_number == 1:
                self.image_1 = Image.open(file_path)
            elif image_number == 2:
                self.image_2 = Image.open(file_path)
            self.update_images()

    def update_images(self):
        self.canvas_1.delete("all")
        self.canvas_2.delete("all")

        if self.image_1 is not None:
            new_width_1 = int(self.image_1.width * self.zoom_factor_1)
            new_height_1 = int(self.image_1.height * self.zoom_factor_1)
            resized_image_1 = self.image_1.resize((new_width_1, new_height_1), Image.LANCZOS)
            photo_1 = ImageTk.PhotoImage(resized_image_1)
            self.canvas_1.create_image(0, 0, anchor="nw", image=photo_1)
            self.canvas_1.image = photo_1

        if self.image_2 is not None:
            new_width_2 = int(self.image_2.width * self.zoom_factor_2)
            new_height_2 = int(self.image_2.height * self.zoom_factor_2)
            resized_image_2 = self.image_2.resize((new_width_2, new_height_2), Image.LANCZOS)
            photo_2 = ImageTk.PhotoImage(resized_image_2)
            self.canvas_2.create_image(0, 0, anchor="nw", image=photo_2)
            self.canvas_2.image = photo_2

        self.update_mastil()  #Solucionar

    def update_mastil(self):
        x1, y1, x2, y2 = self.canvas_1.bbox("all")
        x_center = (x2 - x1) / 2 + x1
        y_bottom = y2
        self.canvas_1.coords(self.mastil, x_center, y_bottom, x_center, y_bottom + 50)

    def zoom_with_mouse_wheel(self, event):

        if event.delta > 0:
            if self.active_image == 1:
                self.zoom_factor_1 *= 1.1
            else:
                self.zoom_factor_2 *= 1.1
        else:
            if self.active_image == 1:
                self.zoom_factor_1 /= 1.1
            else:
                self.zoom_factor_2 /= 1.1
        self.update_images()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
