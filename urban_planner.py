from agent import Agent
from developer import Developer
from surveyor import Surveyor

class UrbanPlanner(Agent):
    def __init__(self, position, land, population, surveyor, developer):
        #call parents innit so if changes need to made they only need to be made
        #on the parent level
        super().__init__(position)
        self.R = 0
        self.B = 200
        self.G = 20
        self.surveyor = surveyor
        self.developer = developer
        self.population = population
        self.plats = []
        self.land = land

    def getPlats(self):
        return self.plats

    def createCity(self):
        plats = self.surveyor.initializePlats(self.land)
        self.plats += plats

    def assessNeeds(self, population):
        pass
    
    def hireDeveloper(self, plat):
        pass
