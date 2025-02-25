# This code creates qr code of the given link

import qrcode
print("Enter the link")
link = input()
qr = qrcode.make(link)
qr.show()