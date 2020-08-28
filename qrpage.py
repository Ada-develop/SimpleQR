#Importing tools:

import pyqrcode
import png
from pyqrcode import QRCode

#Initialize string for QR representation

QRstring = "https://github.com/Ada-develop"

#Creating QR of a string

url = pyqrcode.create(QRstring)

#Converting QR to .png format

url.png('./qr.png', scale=8)