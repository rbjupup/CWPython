from PIL import Image
im=Image.open("D:\\test.bmp")
print(im.format,' ',im.size,' ',im.mode)