from PIL import Image, ImageDraw

class Plat:
    def __init__(self, bounds):
        self.bounds = bounds

    def draw(self, painter):
        vertexCount = len(self.bounds)
        print(self.bounds)

        for vertexId in range(vertexCount):
            start = self.bounds[vertexId]
            end = self.bounds[(vertexId + 1) % vertexCount]
            painter.line(start + end, fill = (255, 255, 255, 255)) 
