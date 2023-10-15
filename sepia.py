import image

#img= image.Image()
win=image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,100)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p=img.getPixel(col,row)
        R= p.getRed()
        G= p.getGreen()
        B= p.getBlue()
        newR = 0.393*R + 0.769*G + 0.189*B
        newG = 0.349*R + 0.686*G + 0.168*B
        newB = 0.272*R + 0.534*G + 0.131*B
        newpixel= image.Pixel(newR,newG,newB)
        img.setPixel(col, row, newpixel)
        
img.draw(win)
win.exitonclick()

""" from PIL import Image

def sepia(image_path:str)->Image:
    img = Image.open(image_path)
    width, height = img.size

    pixels = img.load() # create the pixel map

    for py in range(height):
        for px in range(width):
            r, g, b = img.getpixel((px, py))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255:
                tr = 255

            if tg > 255:
                tg = 255

            if tb > 255:
                tb = 255

            pixels[px, py] = (tr,tg,tb)

    return img """