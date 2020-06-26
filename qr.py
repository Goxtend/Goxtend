from PIL import Image
import pyqrcode
import os
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog


def background_white(logo):
    logo_width, logo_height = logo.size
    pixdata = np.asarray(logo)
    pixdata = pixdata.copy()
    for y in range(logo_height):
        for x in range(logo_width):
            if pixdata[x, y][3] == 0:
                pixdata[x, y] = (255, 255, 255, 255)

    array = np.array(pixdata, dtype=np.uint8)    
    logo = Image.fromarray(array)

    return logo


def generate_qr_code(path_url, logo_url,
                    target_name='qr_code.png',
                    scale_factor=1/3):
    url = pyqrcode.QRCode(path_url, error = 'H')
    url.png(target_name, scale=10)
    img = Image.open(target_name)
    img = img.convert("RGBA")
    logo = Image.open(logo_url)

    width, height = img.size
    logo_size = width * scale_factor
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))

    logo = logo.resize((xmax - xmin, ymax - ymin))
    
    if logo_url.endswith('.png'):
        logo = background_white(logo)

    # put the logo in the qr code
    img.paste(logo, (xmin, ymin, xmax, ymax))
    img.save(target_name)
    img.show()


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QR-Code Generator")
        self.root.minsize(width=500, height=100)
        
        ttk.Label(self.root, text="Output Filename").grid(row=0)
        self.target_name_var = tk.StringVar()
        self.target_name_var.set('qr_code.png')
        self.target_name_entry = ttk.Entry(self.root,
                                        width=50,
                                        textvariable=self.target_name_var)
        self.target_name_entry.grid(row=0, column=1)

        ttk.Label(self.root, text="URL").grid(row=1)
        self.url_var = tk.StringVar()
        self.url_entry = ttk.Entry(self.root,
                                    width=50,
                                    textvariable=self.url_var)
        self.url_entry.grid(row=1, column=1)

        self.logo_url_var = tk.StringVar()
        self.logo_url_entry = ttk.Entry(self.root,
                                        width=50,
                                        textvariable=self.logo_url_var)
        self.logo_url_entry.grid(row=2, column=1)
        logo_btn = ttk.Button(self.root,
                            text="Select Logo",
                            command=self.select_logo)
        logo_btn.grid(row=2, column=0)

        generate_btn = ttk.Button(self.root,
                                text="Generate",
                                command=self.generate_qr_code)
        generate_btn.grid(row=3, columnspan=2)

    def run(self):
        self.root.mainloop()
    
    def select_logo(self):
        file_name = filedialog.askopenfilename(initialdir=os.getcwd())
        self.logo_url_var.set(file_name)
    
    def generate_qr_code(self):
        url = self.url_var.get()
        logo_url = self.logo_url_var.get()
        target_name = self.target_name_var.get()
        
        generate_qr_code(url, logo_url, target_name)


if __name__ == '__main__':
    window = Window()
    window.run()
