from point import Point
from road import Road
from agent import Agent

class RoadBuilder(Agent):
    def __init__(self, position):
        super().__init__(position)

    def build(self):
        roads = [
            Road(Point(0, 0), Point(150, 0)),
            Road(Point(0, 40), Point(150, 40)),
            Road(Point(0, 100), Point(150, 100)),
            Road(Point(0, 0), Point(0, 100)),
            Road(Point(100, 0), Point(100, 100)),
            Road(Point(150, 0), Point(150, 100))]
        return roads;
