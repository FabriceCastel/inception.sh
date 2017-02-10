from agent import Agent
from developer import Developer
from surveyor import Surveyor
from road_builder import RoadBuilder
from point import Point
from block import Block

class UrbanPlanner(Agent):
    def __init__(self, position):
        #call parents innit so if changes need to made they only need to be made
        #on the parent level
        super().__init__(position) 
        self.roadBuilder = RoadBuilder(position)
        self.surveyor = Surveyor(position)
        self.blocks = []
        self.roads = []
    
    def createCity(self):
        roads = self.roadBuilder.build()
        blocks = self.findBlocks(roads)
        for block in blocks:
            self.surveyor.initializePlats(block)

        self.roads += roads
        self.blocks += blocks
    
    def drawCity(self,imgDraw):
        scale = 4
        for road in self.roads:
            imgDraw.line((road.start.x*scale, road.start.y*scale, road.end.x*scale, road.end.y*scale), fill = (255, 100, 100, 255))
        for block in self.blocks:
            for i in range(len(block.bounds)):
                start = block.bounds[i]
                end = block.bounds[(i + 1) % len(block.bounds)]
                imgDraw.line((start.x*scale, start.y*scale, end.x*scale, end.y*scale), fill = (255, 255, 255, 200))
        for block in self.blocks:
            for plat in block.plats:
                for i in range(len(plat.bounds)):
                    start = plat.bounds[i]
                    end = plat.bounds[(i + 1) % len(plat.bounds)]
                    imgDraw.line((start.x*scale, start.y*scale, end.x*scale, end.y*scale), fill = (255, 255, 255, 200))

    def findBlocks(self, roads):
        # Assumes roads form perfect grid with strictly
        # vertical and horizontal roads
        # This also assumes that all horizontal roads
        # intersect the vertical roads and vice-versa
        p = 2 # padding

        vertical = list(\
            filter(lambda r: r.start.x == r.end.x,\
                sorted(roads, key = lambda r: min(r.start.x, r.end.x))))
        horizontal = list(\
            filter(lambda r: r.start.y == r.end.y,\
                sorted(roads, key = lambda r: min(r.start.y, r.end.y))))
        
        vpairs = list(zip(vertical[:-1], vertical[1:]))
        hpairs = list(zip(horizontal[:-1], horizontal[1:]))

        return [item for sublist in list(map(lambda vpair:\
                list(map(lambda hpair:\
                        Block([Point(vpair[0].start.x + p, hpair[0].start.y + p),\
                               Point(vpair[0].start.x + p, hpair[1].start.y - p),\
                               Point(vpair[1].start.x - p, hpair[1].start.y - p),\
                               Point(vpair[1].start.x - p, hpair[0].start.y + p)]),\
                    hpairs)),\
                vpairs)) for item in sublist]
                                

    def assessNeeds(self, population):
        pass
    
    def hireDeveloper(self, plat):
        pass
