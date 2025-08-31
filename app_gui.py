import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np

from proses_gambar import apply_frequency_filter

class ImageFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Filter Gambar Domain Frekuensi")
        self.root.geometry("1000x600")

        self.image_path = None
        self.original_image_cv = None

        # Main layout
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.pack(side=tk.TOP, fill=tk.X)

        # Picture frame
        image_frame = ttk.Frame(self.root, padding="10")
        image_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Widget conrol
        self.btn_select = ttk.Button(control_frame, text="Pilih Gambar...", command=self.select_image)
        self.btn_select.pack(side=tk.LEFT, padx=5, pady=5)

        # Filter Tyope
        self.filter_type = tk.StringVar(value="low")
        ttk.Label(control_frame, text="Tipe Filter:").pack(side=tk.LEFT, padx=(20, 5), pady=5)
        ttk.Radiobutton(control_frame, text="Low-pass (Blur)", variable=self.filter_type, value="low").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(control_frame, text="High-pass (Tepi)", variable=self.filter_type, value="high").pack(side=tk.LEFT, padx=5)

        # Slider Radius
        ttk.Label(control_frame, text="Radius Filter:").pack(side=tk.LEFT, padx=(20, 5), pady=5)
        self.radius_slider = ttk.Scale(control_frame, from_=1, to=200, orient=tk.HORIZONTAL, length=200)
        self.radius_slider.set(30)
        self.radius_slider.pack(side=tk.LEFT, padx=5)

        # Filter apply button
        self.btn_apply = ttk.Button(control_frame, text="Terapkan Filter", command=self.apply_filter_and_display)
        self.btn_apply.pack(side=tk.LEFT, padx=20, pady=5)

        # Original; image
        self.panel_original = ttk.Label(image_frame, text="Gambar Asli Akan Tampil di Sini", relief="solid", anchor=tk.CENTER)
        self.panel_original.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Fltered image
        self.panel_filtered = ttk.Label(image_frame, text="Gambar Hasil Filter Akan Tampil di Sini", relief="solid", anchor=tk.CENTER)
        self.panel_filtered.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def select_image(self):
        # input image
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
        if not path:
            return
        
        self.image_path = path
        self.original_image_cv = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
        
        self.display_image(self.original_image_cv, self.panel_original)
        self.panel_filtered.config(image=None, text="Gambar Hasil Filter Akan Tampil di Sini")
        self.panel_filtered.image = None


    def apply_filter_and_display(self):
        if self.image_path is None:
            messagebox.showerror("Error", "Silakan pilih gambar terlebih dahulu!")
            return
            
        filter_type = self.filter_type.get()
        radius = int(self.radius_slider.get())

        _, filtered_image = apply_frequency_filter(self.image_path, filter_type, radius)
        
        if filtered_image is not None:
            self.display_image(filtered_image, self.panel_filtered)

    def display_image(self, img_cv, panel):
        img_pil = Image.fromarray(img_cv.astype(np.uint8))

        w, h = img_pil.size
        max_size = 450
        if w > max_size or h > max_size:
            ratio = min(max_size / w, max_size / h)
            img_pil = img_pil.resize((int(w * ratio), int(h * ratio)), Image.LANCZOS)
            
        img_tk = ImageTk.PhotoImage(image=img_pil)
        
        panel.config(image=img_tk, text="")
        panel.image = img_tk


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageFilterApp(root)
    root.mainloop()