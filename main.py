from PIL import Image, ImageDraw
import random
from functools import reduce

img = Image.new('RGBA', (800, 500), (0, 0, 0, 255))
painter = ImageDraw.Draw(img)


class Building():
    
    def __init__(self, northWest, southEast, painter):
        self.northWest = northWest
        self.southEast = southEast 
        self.painter = painter
        
    
    def draw(self):
        self.painter.rectangle(self.northWest + self.southEast, fill = (55, 255, 255, 255))

    def north_of(self, building):
        return self.southEast[1] <= building.northWest[1]

    def south_of(self, building):
        return self.northWest[1] >= building.southEast[1]

    def east_of(self, building):
        return self.northWest[0] >= building.southEast[0]

    def west_of(self, building):
        return self.southEast[0] <= building.northWest[0]

    def intersects(self, building):
        return not (self.north_of(building) or self.south_of(building)\
                    or self.east_of(building) or self.west_of(building)) 
                        
buildings = []

buildingSize = (60, 60)

for i in range(14):
    while True: 
        northWest = (random.randrange(img.size[0] - buildingSize[0]),\
                     random.randrange(img.size[1] - buildingSize[1]))
        southEast = (northWest[0] + buildingSize[0], northWest[1] + buildingSize[1])
        print("I'm a random building", northWest + southEast)
        print("I'm the buildings printed so far!", buildings)
        building = Building(northWest, southEast, painter)
        valid = True        

        for b in buildings: 
            if building.intersects(b):
                valid = False         

        print("Am I a valid building???", valid)        
        if valid == True:
            buildings.append(building)
            building.draw()
            break




img.save('test.png')

