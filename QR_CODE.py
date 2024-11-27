# Creating a QR Code:

import qrcode as qr

# Imported "qrcode" module with alias (assigned with a short-form as "qr")
# In the arguments of the "make()" we need to put that URL link for which our QR Code is generated.

img = qr.make("https://www.linkedin.com/in/shivam-jha-044339175/")    # This link will generate a QR Code using "make()" function.

img.save("SJ_LinkedIn.png")   # It will save the generated QR Code image in png format.
