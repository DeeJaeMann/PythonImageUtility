from PIL import Image
im = Image.open("profile2.jpeg")
im.rotate(45).show()