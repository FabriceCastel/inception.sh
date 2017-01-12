from PIL import Image, ImageDraw
import random
from math import sqrt

img = Image.new('RGBA', (800, 500), (0, 0, 0, 255))
painter = ImageDraw.Draw(img)


class CircleBuilding():
    
    def __init__(self, center, radius, painter):
        self.center = center
        self.radius = radius 
        self.painter = painter

    def draw(self):
        self.painter.ellipse((self.center[0] - self.radius, self.center[1] - self.radius,\
                             self.center[0] + self.radius, self.center[1] + self.radius),\
                             fill = (55, 255, 255, 255))

    def distanceTo(self, other):
        return sqrt(abs((other.center[0] - self.center[0]))**2 + abs((other.center[1] -\
                    self.center[1])**2))
    
    def intersects(self, other):
        return not self.distanceTo(other) >= (other.radius + self.radius)

buildings = []

for i in range(10):
    while True: 
        buildingRadius = random.randrange(70, 80)
        buildingCenter = (random.randrange(buildingRadius, img.size[0] - buildingRadius),\
                          random.randrange(buildingRadius, img.size[1] - buildingRadius))
        building = CircleBuilding(buildingCenter, buildingRadius, painter)
        valid = True        

        for b in buildings: 
            if building.intersects(b):
                valid = False         

        if valid == True:
            buildings.append(building)
            building.draw()
            break

img.save('test.png')
