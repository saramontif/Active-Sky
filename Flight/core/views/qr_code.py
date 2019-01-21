import pyqrcode
from django.conf import settings
url = pyqrcode.create('http://6fd221c3.ngrok.io/phone_scan')
url.png('url.png')


