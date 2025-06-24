# 📸 QR Code Generator with Custom Colors and Logo

This is a simple yet powerful Python script that generates **custom QR codes** with personalized colors and the option to **embed a logo** in the center. Perfect for creating branded QR codes for websites, events, or products.

## ✨ Features

- ✅ Generate QR codes from any text or URL
- 🎨 Customize foreground and background colors
- 🖼️ Option to add a logo in the center
- 💾 Save as high-quality `.png` image
- 🐍 Built with pure Python (`qrcode` + `Pillow`)

---

## 🛠️ Requirements

- Python 3.7+
- Required libraries:

```bash
pip install qrcode[pil]
```


## 🚀 How to Use
1. Clone the repository:

```
git clone https://github.com/genesisvaca/QR-Code-Generator.git
cd QR-Code-Generator
```
2. Edit the logo path (optional):

In qr_generator.py, change the logo path to match your logo file location:

````
logo = Image.open(r"C:\Your\Path\To\logo.png")
````

3. Run the script:

````
python qr_generator.py
````
4. Follow the prompts:

Enter the text or URL you want to encode

Enter the desired output file name (e.g. my_qr.png)

## 🖼️ Example Output
<div align="center"> <img src="preview.png" alt="QR code example with logo" width="300"/> </div>
Preview with purple QR color, white background, and embedded logo.

## 📂 Project Structure
````
QR-Code-Generator/
├── qr_generator.py         # Main Python script
├── logo.png                # (Optional) Logo file used in center of QR
├── preview.png             # Example QR code image
└── README.md               # This file
````

## 📬 Contact
Created with ❤️ by Génesis Vaca Palma

📧 Email: genesisvacapalma@gmail.com

