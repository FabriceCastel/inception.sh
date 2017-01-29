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

population = Population()
developer = Developer((50, 50))
surveyor = Surveyor((300, 200))
planner = UrbanPlanner((400, 200), land, population, surveyor, developer)
people = [planner, developer, surveyor]
for i in range(10):
    people.append(Person((300, 300)))

population.add(people)

planner.createCity()

plats = planner.getPlats()

for plat in plats:
    plat.draw(painter)

image.save('fab.png')
