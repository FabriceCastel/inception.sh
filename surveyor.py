from agent import Agent
from plat import Plat

class Surveyor(Agent):
    def __init__(self, position):
        #call parents innit so if changes need to made they only need to be made
        #on the parent level
        super().__init__(position)
        self.R = 0
        self.B = 200
        self.G = 20


    def initializePlats(self, land):
        plats = []
        
        width = 50
        rows = 4
        columns = 3
        for r in range(rows):
            for c in range(columns):
                if ((r == 0 or r == rows - 1) or (c == 0 or c == columns - 1)):
                    plats.append(Plat([\
                        (c * width, r * width),\
                        ((c+1) * width, r * width),\
                        ((c+1) * width, (r+1) * width),\
                        (c * width, (r+1) * width)]))

        return plats
            
