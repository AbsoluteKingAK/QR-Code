import pyqrcode
from pyqrcode import QRCode
import png

s="www.google.com"

url=pyqrcode.create(s)

url.svg("qrcode.svg",scale=8)
url.png("qrcode.png",scale=8)