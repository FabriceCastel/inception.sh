from agent import Agent

class Developer(Agent):
    def __init__(self, position):
        #call parents innit so if changes need to made they only need to be made
        #on the parent level
        super().__init__(position)
        self.R = 0
        self.B = 50
        self.G = 200

     def develop(self, land):
         pass

