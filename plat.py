from PIL import Image, ImageDraw

class Plat:
    def __init__(self, boundaries):
        self.boundaries = boundaries

    def draw(self, painter):
        vertexCount = len(self.boundaries)
        print(self.boundaries)

        for vertexId in range(vertexCount):
            start = self.boundaries[vertexId]
            end = self.boundaries[(vertexId + 1) % vertexCount]
            painter.line(start + end, fill = (255, 255, 255, 255)) 
