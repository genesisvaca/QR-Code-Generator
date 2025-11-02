# 📸 QR Code Generator with Custom Colors and Logo

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-64C9CF?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Library-qrcode%20%7C%20Pillow-FEC89A?style=for-the-badge" alt="Libraries Badge">
  <img src="https://img.shields.io/badge/Focus-CLI%20Tool%20%7C%20Image%20Generation-84A59D?style=for-the-badge" alt="Focus Badge">
  <img src="https://img.shields.io/badge/Type-Utility%20Script-9B5DE5?style=for-the-badge" alt="Type Badge">
  <img src="https://img.shields.io/badge/Status-Completed-FD6F96?style=for-the-badge" alt="Status Badge">
</p>


This is a simple yet powerful Python script that generates **custom QR codes** with personalized colors and the option to **embed a logo** in the center. Perfect for creating branded QR codes for websites, events, or products.

## ✨ Features

- ✅ Generate QR codes from any text or URL
- 🎨 Customize foreground and background colors
- 🖼️ Option to add a logo in the center
- 💾 Save as high-quality `.png` image
- 🐍 Built with pure Python (`qrcode` + `Pillow`)

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

## 📂 Project Structure
````
QR-Code-Generator/
├── qr_generator.py         # Main Python script
├── logo.png                # (Optional) Logo file used in center of QR
├── preview.png             # Example QR code image
└── README.md               # This file
````

## 

Created with ❤️ by **Génesis Vaca Palma**
📧 [genesisvacapalma@gmail.com](mailto:genesisvacapalma@gmail.com)  

📍 Based in Madrid, Spain  
🌐 [GitHub Profile](https://github.com/genesisvaca)
