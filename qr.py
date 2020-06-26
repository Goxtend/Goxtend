from PIL import Image
import pyqrcode
import numpy as np


TARGET_NAME = 'qr_code.png'


def background_white(logo):
    pixdata = np.asarray(logo)
    pixdata = pixdata.copy()
    for y in range(logo_height):
        for x in range(logo_width):
            if pixdata[x, y][3] == 0:
                pixdata[x, y] = (255, 255, 255, 255)

    array = np.array(pixdata, dtype=np.uint8)    
    logo = Image.fromarray(array)

    return logo


def generate_qr_code(path_url, logo_url, scale_factor = 1/3):
    url = pyqrcode.QRCode(path_url, error = 'H')
    url.png(TARGET_NAME, scale=10)
    img = Image.open(TARGET_NAME)
    img = img.convert("RGBA")
    logo = Image.open(logo_url)

    width, height = img.size
    logo_size = width * scale_factor
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))

    logo = logo.resize((xmax - xmin, ymax - ymin))
    logo_width, logo_height = logo.size
    
    if logo_url.endswith('.png'):
        logo = background_white(logo)

    # put the logo in the qr code
    img.paste(logo, (xmin, ymin, xmax, ymax))
    img.save(TARGET_NAME)
    img.show()


if __name__ == '__main__':
    generate_qr_code('https://goxtend.github.io/Goxtend?card=antik',
                    'antik_logo.jpg')
