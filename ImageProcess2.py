import pgzrun
from PIL import Image
import random

try:
    im = Image.open('images\\image2.jpg')
except:
    print("Error opening file.")

w, h = im.size
WIDTH = w
HEIGHT = h
px = im.load()
XY = []
RGB = []
key = 1
radius = 3


def update():
    global key
    if keyboard.k_1:
        key = 1
    elif keyboard.k_2:
        key = 2
    elif keyboard.k_3:
        key = 3
    elif keyboard.k_4:
        key = 4
    elif keyboard.k_5:
        key = 5
    elif keyboard.k_6:
        key = 6
    elif keyboard.escape:
        key = -1

    XY.clear()
    RGB.clear()

    for i in range(100):
        x = random.randint(0, w - 1)
        y = random.randint(0, h - 1)
        r, g, b = px[x, y]
        XY.append((x, y))
        RGB.append((r, g, b))


def draw():
    if key == -1:
        screen.clear()
    for i in range(100):
        x = XY[i][0]
        y = XY[i][1]
        box = Rect((x, y), (radius, radius))
        if key == 1:  # draw filled circle
            screen.draw.filled_circle(XY[i], radius, RGB[i])
        if key == 2:  # draw empty circle
            screen.draw.circle(XY[i], radius, RGB[i])
        if key == 3:  # draw line
            screen.draw.line((x,y), (x+radius, y+radius), RGB[i])
        if key == 4:  # draw X
            screen.draw.line((x - radius, y - radius), (x + radius, y + radius), RGB[i])
            screen.draw.line((x-radius, y+radius), (x+radius, y-radius), RGB[i])
        if key == 5:  # draw empty square
            screen.draw.rect(box, RGB[i])
        if key == 6:  # draw filled square
            screen.draw.filled_rect(box, RGB[i])


pgzrun.go()
