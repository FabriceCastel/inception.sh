from agent import Agent
import random 
from plat import Plat
from block import Block


class Surveyor(Agent):
    def __init__(self, position):
        #call parents innit so if changes need to made they only need to be made
        #on the parent level
        super().__init__(position)
        self.R = 0
        self.B = 200
        self.G = 20


    def constructPlats(self, block):
        """Given a Block instance, return a list of Plat instances that each
        contain its bounds in clock-wise order.
        
        @param Surveyor self: Surveyor self
        @param Block block: a Block instance
        @rtype: Plat
        
        >>> block = Block([(10, 10), (50, 10), (50, 20), (10, 20)])
        >>> surveyor = Surveyor((0, 0))
        >>> surveyor.constructPlats(block)
        >>> block.Plats
        >>> block = Block([(50, 50), (60, 50), (60, 0), (50, 0)])
        >>> surveyor = Surveyor((0, 0))
        >>> surveyor.constructPlats(block)
        >>> block.Plats
        >>> block = Block([(50, 50), (60, 50), (60, 40), (50, 40)])
        >>> surveyor = Surveyor((0, 0))
        >>> surveyor.constructPlats(block)
        >>> block.Plats
 
        """
        northWest = block.bounds[0]
        northEast = block.bounds[1]
        southEast = block.bounds[2]
        southWest = block.bounds[3]
        
        width = abs(northWest[0] - northEast[0])
        height = abs(northWest[1] - southEast[1])

        if width > height:
            platBounds = []
            if width  >= 15:
                blockLeft = 0
                platNE = northWest
                platSE = southWest
                platNW = 0
                platSW = 0
                lastPlat = random.randint(15, 25)
                while blockLeft < width - lastPlat: 
                    platWidth = random.randint(15, 25)
                    platNW  = platNE
                    platSW = platSE
                    platNE = platNW + platWidth
                    platSE = platSW + platWidth
                    platBounds.append(Plat([platNW, platNE, platSE, platSW]))
                    blockLeft = blockLeft + platWidth
                platNW = platNE
                platSW = plateSE
                platNE = platNW + lastPlat
                platSE = platSW + lastPlat
                platBounds.append(Plat([platNW, platNE, platSE, platSW]))
                block.Plats = platBounds
            else:
                block.Plats = Plat([northWest, northEast, southEast, southWest])


        if width < height:
            platBounds = []
            if height  >= 15:
                blockLeft = 0
                platNW = southWest 
                platNE = southEast
                platSW = 0
                platSE = 0
                lastPlat = random.randint(15, 25)
                while blockLeft < height - lastPlat: 
                    platHeight = random.randint(15, 25)
                    platSW  = platNW
                    platSE = platNE
                    platNW = platSW + platHeight
                    platNE = platSE + platHeight
                    platBounds.append(Plat([platNW, platNE, platSE, platSW]))
                    blockLeft = blockLeft + platHeight
                platSW = platNW
                platSE = plateNE
                platNW = platSW + lastPlat
                platNE = platSE + lastPlat
                platBounds.append(Plat([platNW, platNE, platSE, platSW]))
                block.Plats = platBounds
            else:
                block.Plats = Plat([northWest, northEast, southEast, southWest])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
        

    


        
