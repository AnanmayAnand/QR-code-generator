import qrcode
from PIL import Image
import matplotlib.pyplot as plt
import io

# URL to LinkedIn profile
linkedin_url = "https://www.linkedin.com/in/ananmay-anand-581b00219/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(linkedin_url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img_path = "linkedin_qr_code.png"
img.save(img_path)

print(f"QR code saved as {img_path}")

# Display the QR code image using Matplotlib
plt.imshow(img, cmap='Greys')
plt.axis('off')  # Turn off axis numbers and ticks
plt.show()