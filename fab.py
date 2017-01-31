from PIL import Image, ImageDraw
from population import Population
from person import Person
from developer import Developer
from urban_planner import UrbanPlanner
from land import Land
from surveyor import Surveyor

image = Image.new('RGBA', (800, 500), (0, 0, 0, 255))
painter = ImageDraw.Draw(image)

land = Land()

planner = UrbanPlanner((400, 200))

planner.createCity()
planner.drawCity(painter)

image.save('fab.png')
