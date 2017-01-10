from PIL import Image, ImageDraw
import random

def clamp(a, b, c):
    return max(b, min(a, c))

def drawDrop(img, pos, rad, rgb):
    for x in range(max(0, pos[0] - rad), min(img.size[0] - 1, pos[0] + rad)):
        for y in range(max(0, pos[1] - rad), min(img.size[1] - 1, pos[1] + rad)):
            if(random.uniform(0, 1) < 0.05):
                img.putpixel((int(x), int(y)), rgb)

def drawRandomRect(img):
    x = img.size[1] / 2
    y = 0

    r = 105
    g = 220
    b = 220

    for i in range(100000):
        drawDrop(img, (int(x), int(y)), 10, (int(r), int(g), int(b)))
        x = clamp(x + random.uniform(-1, 1) * 5, 0, img.size[0] - 1)
        y = clamp(y + random.uniform(-1, 1) * 5, 0, img.size[1] - 1)
        
        # attract to centre
        """attr = 5000
        attrstr = 1

        if(random.random() < (abs(x + img.size[0]/2) / attr)):
            if(x > img.size[0] / 2):
                x -= random.uniform(0, attrstr)
            else:
                x += random.uniform(0, attrstr)
        
        if(random.random() < (abs(y + img.size[1]/2) / attr)):
            if(y > img.size[1] / 2):
                y -= random.uniform(0, attrstr)
            else:
                y += random.uniform(0, attrstr)
"""
        r = clamp(r + random.uniform(-1, 1) * 0.3, 0, 255)
        g = clamp(g + random.uniform(-1, 1) * 0.3, 0, 255)
        b = clamp(b + random.uniform(-1, 1) * 0.3, 0, 255)

img = Image.new('RGBA', (800, 600), (0, 0, 0, 255))
#draw = ImageDraw.Draw(img)

drawRandomRect(img)

#del draw

img.save('test.png')

