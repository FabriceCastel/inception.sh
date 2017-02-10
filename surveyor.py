from agent import Agent
from plat import Plat
from block import Block
from point import Point

class Surveyor(Agent):
    def __init__(self, position):
        #call parents innit so if changes need to made they only need to be made
        #on the parent level
        super().__init__(position)
        self.R = 0
        self.B = 200
        self.G = 20


    def initializePlats(self, block):
        """Initializes Plats for a given Block.
        
        @param Surveyor se1lf: Surveyor self
        @param Block block: a Block instance
        @rtype: None
        """

        bounds = block.bounds 
        eastToWest = bounds[1].x - bounds[0].x
        northToSouth = bounds[3].y - bounds[0].y
        if eastToWest < northToSouth:
            platWidth = self.findPlatWidth(northToSouth)
            platPositions = self.setPlatBounds(platWidth, bounds[0].y, bounds[3].y)
            for platPosition in platPositions:
                block.plats.append(Plat([Point(platPosition[0], bounds[0].y),\
                                            Point(platPosition[1], bounds[0].y),\
                                            Point(platPosition[1], bounds[3].y),\
                                            Point(platPosition[0], bounds[3].y)]))
        else:
            platWidth = self.findPlatWidth(eastToWest) 
            platPositions = self.setPlatBounds(platWidth, bounds[0].x, bounds[1].x)
            for platPosition in platPositions:
                block.plats.append(Plat([Point(bounds[0].x, platPosition[0]),\
                                            Point(bounds[1].x, platPosition[0]),\
                                            Point(bounds[1].x, platPosition[1]),\
                                            Point(bounds[0].x, platPosition[1])]))
    
    def setPlatBounds(self, platWidth, startPos, endPos):
        platPos = startPos - platWidth
        platEndPos = startPos
        platPositions = []
        while platPos < endPos - platWidth:
            platPos = platPos + platWidth       
            platEndPos = platPos + platWidth
            platPositions.append([platPos, platEndPos])
        print(platPositions)
        return platPositions

    def findPlatWidth(self, longSide):
        """
        @param Surveyor self: 
        @param float|int longSide: the longer side
        """ 
        platWidth = longSide
        while 40 < platWidth: 
            platWidth = platWidth / 2
        return platWidth
        
if __name__ == "__main__":
    block1 = Block([Point(0, 0), Point(5, 0), Point(5, 200), Point(0, 200)])
    surveyor1 = Surveyor((0, 0))
    surveyor1.initializePlats(block1)
    plats = [plat.bounds for plat in block1.plats]
    print(block1.plats)
    block2 = Block([Point(0, 0), Point(500, 0), Point(500, 10), Point(0, 10)])
    surveyor2 = Surveyor((0, 0))
    surveyor2.initializePlats(block2)
    plats = [plat.bounds for plat in block2.plats]
    print(block2.plats)



 
