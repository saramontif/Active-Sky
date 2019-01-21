import pyqrcode

url = pyqrcode.create('http://uca.edu/8787/?x=123')
url.png('url.png')


