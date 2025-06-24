import qrcode
from PIL import Image

def generate_qr_code(text, file_name):
    # QR Configuration
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=20,      # Size of the QR code squares
        border=4          # Larger border for a more professional look
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Create the QR image with custom colors
    img = qr.make_image(fill_color="#800080", back_color="#FFFFFF")  # Purple foreground, white background

    # Add a logo or icon to the center (optional)
    logo_size = 100  # Logo size
    logo = Image.open(r"C:\Users\jesus\Desktop\Generador_QR\logo.png")  # Path to your logo image
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)  # Resize with high-quality resampling

    # Calculate position to center the logo in the QR code
    pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)

    # Paste the logo onto the center of the QR
    img.paste(logo, pos)

    # Save the final image
    img.save(file_name)
    print(f"QR code saved as {file_name}")

# Run the generator from terminal
if __name__ == "__main__":
    text = input("Enter the text or URL to generate the QR code: ")
    file_name = input("Enter the file name to save the QR code (include .png): ")
    generate_qr_code(text, file_name)