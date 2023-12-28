import qrcode
from pyzbar.pyzbar import decode

from PIL import Image

LinkedIN = qrcode.make("https://www.linkedin.com/in/saurav-kumar-92bb521a8/")
LinkedIN.save("linkedIn.png")

d = decode(Image.open("linkedIn.png"))
print(d[0].data.decode("ascii"))