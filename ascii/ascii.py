from PIL import Image, ImageOps
import math

shades = [" ", "_", ".", ",", "-", "=", "+", ":", ";", "c", "b", "a", "!", "?",
          "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "$", "W", "#", "@", " "]
result = []


def shading(skip, color):
    asciicolor = math.floor(color / 9)

    if skip == True:
        result.append("\n")

    if skip == False:
        result.append(shades[asciicolor])


def imageselect(path, DimX, DimY):
    img = Image.open(path)
    width, height = img.size
    imgsmall = img.resize((int(DimX), int(DimY)), resample=0)
    imggs = ImageOps.grayscale(imgsmall)
    hsvimg = imggs.convert("HSV")

    width = imgsmall.width
    height = imgsmall.height

    coordinates = x, y = 0, 0

    for i in ("-" * ((width * height) - width)):
        color = hsvimg.getpixel(coordinates)
        shading(False, color[2])

        if int(x) == int(width) - 1:
            x = 0
            y = y + 1
            shading(True, 0)

        x = x + 1
        coordinates = x, y


print("Write the path to the file you want to be turned into ascii art (include file extension)(can be local path):")
chosen = input("")

print("Select the X size that you want your image to be compressed too:")
dimchoseX = input("")

print("Select the Y size that you want your image to be compressed too:")
dimchoseY = input("")


imageselect(chosen, dimchoseX, dimchoseY)

tosave = ("".join(map(str, result)))

print(tosave)

print("would you like to save this file? (y/n)")
Answer = input("")
if (Answer == "y") or (Answer == "Y"):
    print("what would you like to name this file (do not include file extension)")
    name = input("")
    file = open(name + ".txt", "w")
    file.write(tosave)
