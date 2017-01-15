from PIL import Image, ImageDraw

class Agent:

    def __init__(self, position):
        self.position = position
        self.radius = 10
        self.R = 255
        self.B = 0
        self.G = 0

    def draw(self, painter): 
        painter.ellipse((self.position[0] - self.radius, self.position[1] - self.radius,\
                        self.position[0]  + self.radius, self.position[1] + self.radius),\
                        fill = (self.R, self.G, self.B, 255))        
