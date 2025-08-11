#QR code Generator in python
import qrcode as qr
img=qr.make(" http://bit.ly/wscubechannel")
img.save("wscube_youtube.png")

#border color change qrcode
import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=10)
qr.add_data("sahooanilkumar075@gmail.com")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("Anil_web.png")

import tkinter
m = tkinter.Tk()
'''
widgets are added here
'''
m.mainloop()
