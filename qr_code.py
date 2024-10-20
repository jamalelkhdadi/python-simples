import qrcode


img = qrcode.make("https://exemple.com")
img.save("qr.png","PNG")
