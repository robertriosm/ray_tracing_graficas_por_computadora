from gl import Raytracer
from figures import AABB, TRANSPARENT, Disk, Plane, Material, REFLECTIVE, OPAQUE, Triangle
from lights import AmbientLight, DirectionalLight
from texture import Texture

width = 800
height = 800


rtx = Raytracer(width, height)

brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16, matType = OPAQUE)
stone = Material(diffuse = (0.4, 0.4, 0.3), spec = 8, matType = OPAQUE)
glass = Material(diffuse = (0.4, 0.4, 0.4), spec = 20, matType = TRANSPARENT)
mirror1 = Material(diffuse = (0.8, 0.8, 0.8), spec = 50, matType = REFLECTIVE)
mirror2 = Material(diffuse = (0.7, 0.8, 0.4), spec = 50, matType = REFLECTIVE)
# mirror3 = Material(diffuse = (0.7, 0.4, 0.6), spec = 70, matType = REFLECTIVE)
# mirror4 = Material(diffuse = (0.9, 0.1, 0.9), spec = 64, matType = REFLECTIVE)


# rt3 
floor = Material(diffuse = (0.64, 0.64, 0.64), spec = 64, matType = OPAQUE)
sides = Material(diffuse = (0.8, 0.8, 0.8), spec = 46, matType = OPAQUE)

rtx.envMap = Texture("envs/bg-640x640.bmp")
# rtx.envMap = Texture("envs/parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.6 ))
rtx.lights.append( DirectionalLight(direction = (0,0,-1), intensity = 0.75 ))
rtx.lights.append( DirectionalLight(direction = (0,1,0), intensity = 0.75 ))
rtx.lights.append( DirectionalLight(direction = (0,-1,0), intensity = 0.75 ))


# # # up down
# rtx.scene.append( Plane(position=(0, 5, 10), normal=(0,-1,0), material=floor) )
# rtx.scene.append( Plane(position=(0, -5, -15), normal=(0,0.5,0), material=floor) )

# # sides
# rtx.scene.append( Plane(position=(-5, 0, -10), normal=(-1,0,0), material=sides) )
# rtx.scene.append( Plane(position=(5, 0, -10), normal=(1,0,0), material=sides) )

# # back
# rtx.scene.append( Plane(position=(0, 0, -30), normal=(0,0,-1), material=sides) )

# aditional
# rtx.scene.append(Disk(position=(0, -3, -10), normal=(0,1,0), radius=1, material=mirror2) )
# rtx.scene.append(Disk(position=(0, -1, -10), normal=(0,1,0), radius=1, material=mirror1) )
rtx.scene.append(AABB(position=(-2, 2, -10), size=(2, 2, 2), material=glass))
rtx.scene.append(Triangle(vertices=((-2, -2, 10), (1, 4, 0), (2, 1.5, 3.5)), material=mirror1))
rtx.scene.append(Triangle(vertices=((2, 2, 10), (0, 4, 10), (-2, 3, 3)), material=mirror2))
rtx.scene.append(Triangle(vertices=((-3, -20, 100), (30, 4, -20), (20, 130, 35)), material=brick))
rtx.scene.append(Triangle(vertices=((-0.3, -0.2, 0.1), (0.1, 0.4, -0.2), (0.2, -0.5, 0.5)), material=glass))
# rtx.scene.append(Piramid(position=(-2, 2, -5), normal=(1, 3, 2), material=mirror2))


rtx.glRender()
rtx.glFinish("outputs/outputa.bmp")