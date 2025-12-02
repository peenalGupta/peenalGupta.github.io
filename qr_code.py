# xvgerqgp

import qrcode
from PIL import Image

# REPLACE THIS with your actual website URL after you host it
website_url = "https://your-website-url.com" 

# Create QR Code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(website_url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="#2563eb", back_color="white") # Uses the 'Tech Blue' from your site

# Save the image
img.save("Peenal_Gupta_Visiting_Card_QR.png")
print("QR Code generated successfully as 'Peenal_Gupta_Visiting_Card_QR.png'")