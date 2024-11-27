# QR-Code
Created a QR code project using Python.  

It involves creating a program that generates a QR code image by encoding data like a URL, text, or contact information into a visual pattern that can be scanned by a smartphone camera using a Python library like "qrcode", allowing users to quickly access the encoded information when scanned.  

Basic steps to create a QR code using Python:  

1. Import the library: import qrcode.  
2. Create a QR code object: qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECTION_L).
3. Add data to encode: qr.add_data("any URL").
4. Generate the QR code image: qr.make(fit=True).
5. Create a PIL image: img = qr.make_image(fill_color="black", back_color="white").
6. Save the image: img.save("my_qr_code.png").


I have used two QR_CODE files, in which:
1. QR_CODE.py -> imported qrcode module, then generated the link's qr-code and saved it to the object "img".
2. QR_CODE_2.py -> imported libraries like qrcode and PIL to handle image processing and qr code generation. Added some functionalities in the QR code like version, box_size, error connection.

Generated 2 QR code images in "png" format of my LinkedIn profile.  

Here is my LinkedIn URL: "https://www.linkedin.com/in/shivam-jha-044339175/".
