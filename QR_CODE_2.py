# To add some functionalities in the QR_Code like version, box_size, error_correction:

import qrcode as qr    # qrcode is a library used for generating QR codes.
from PIL import Image   #  PIL (Python Imaging Library) is imported to handle image processing

sj = qr.QRCode(version = 1,
               error_correction = qr.constants.ERROR_CORRECT_H,
               box_size = 20, border = 4 )
# "sj" is the variable object in which, QRCode() function is used for "qr".
# Adding URL link as data to the object "sj":
sj.add_data(" https://www.linkedin.com/in/shivam-jha-044339175/ ")
# "add_data()" will add the url to the file.
sj.make(fit = True)  # Argument: " fit = True " will generate a QR Code using make(), only if there is data in the add_data(), otherwise it will get failed.
# To fill color in the image while making:
img = sj.make_image(fill_color = "white", back_color = "pink")
# To save generated QR Code image:
img.save("SJ_LinkedIn_2.png")  # Saved in .png format