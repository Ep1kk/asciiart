from PIL import Image, ImageOps
import math


result = []


def shading(skip, color):
    asciicolor = math.floor(color / 9)

    if skip == True:
        result.append("\n")

    if skip == False:

        if asciicolor == 0:
            result.append(" ")
        if asciicolor == 1:
            result.append("_")
        if asciicolor == 2:
            result.append(".")
        if asciicolor == 3:
            result.append(",")
        if asciicolor == 4:
            result.append("-")
        if asciicolor == 5:
            result.append("=")
        if asciicolor == 6:
            result.append("+")
        if asciicolor == 7:
            result.append(":")
        if asciicolor == 8:
            result.append(";")
        if asciicolor == 9:
            result.append("c")
        if asciicolor == 10:
            result.append("b")
        if asciicolor == 11:
            result.append("a")
        if asciicolor == 12:
            result.append("!")
        if asciicolor == 13:
            result.append("?")
        if asciicolor == 14:
            result.append("1")
        if asciicolor == 15:
            result.append("2")
        if asciicolor == 16:
            result.append("3")
        if asciicolor == 17:
            result.append("4")
        if asciicolor == 18:
            result.append("5")
        if asciicolor == 19:
            result.append("6")
        if asciicolor == 20:
            result.append("7")
        if asciicolor == 21:
            result.append("8")
        if asciicolor == 22:
            result.append("9")
        if asciicolor == 23:
            result.append("$")
        if asciicolor == 24:
            result.append("W")
        if asciicolor == 25:
            result.append("#")
        if asciicolor == 26:
            result.append("@")
        if asciicolor == 27:
            result.append("N")


def imageselect(path):
    img = Image.open(path)
    width, height = img.size
    imgsmall = img.resize((64, 64), resample=0)
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
imageselect(chosen)

print("".join(map(str, result)))
