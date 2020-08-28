import pyqrcode
import png
from pyqrcode import QRCode

QRstring = "http://192.168.1.72/"

url = pyqrcode.create(QRstring)

url.png('./qr.png', scale=8)