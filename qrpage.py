import pyqrcode
import png
from pyqrcode import QRCode

def create_qr():
    while True:
        print("QR code creator !")
        print("(enter 'q' at any time to quit)")
        QRstring = input("Write here url that you want to convert to QR : ")
        if QRstring == 'q':
            break
        PngName = input("How you want to name your QR file? ")
        if PngName == 'q':
            break
        url = pyqrcode.create(QRstring)
        url.png('./'+ PngName +'.png', scale=8)

create_qr()