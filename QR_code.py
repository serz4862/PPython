import qrcode
# from pyzbar.pyzbar import decode

# from PIL import Image
features = qrcode.QRCode(version =1, box_size = 40,border = 4)


features.add_data("https://www.linkedin.com/in/saurav-kumar-92bb521a8/")
features.make(fit= True)
generate_image = features.make_image(fill_color = "blue",back_color = "yellow")
generate_image.save("image.png")


# d = decode(Image.open("linkedIn.png"))
# print(d[0].data.decode("ascii"))