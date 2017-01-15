from agent import Agent

class Surveyor(Agent):
    def __init__(self, position):
        #call parents innit so if changes need to made they only need to be made
        #on the parent level
        super().__init__(position)
        self.R = 0
        self.B = 200
        self.G = 20


    def findPlate(self, land):
        pass


        
