import pyqrcode 
import png 
from pyqrcode import QRCode 
  
def creat_qr(sendto,fromwho): 
  s = "SMSTO:"+sendto+":"+fromwho+" invited you to chat on PyChat.\n\nYou can download PyChat with the link below : \n\nbit.ly/2CCrEQH"
  url = pyqrcode.create(s)
  url.png('myqr.png', scale = 6)

creat_qr("09113187038","mohammad hossein")