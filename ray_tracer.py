from gl import Raytracer
from figures import AABB, TRANSPARENT, Disk, Plane, Material, REFLECTIVE, OPAQUE
from lights import AmbientLight, DirectionalLight


width = 256*2
height = 256*2


rtx = Raytracer(width, height)

# brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16, matType = OPAQUE)
# stone = Material(diffuse = (0.4, 0.4, 0.3), spec = 8, matType = OPAQUE)
glass = Material(diffuse = (0.4, 0.4, 0.4), spec = 20, matType = TRANSPARENT)
mirror1 = Material(diffuse = (0.8, 0.8, 0.8), spec = 50, matType = REFLECTIVE)
mirror2 = Material(diffuse = (0.7, 0.8, 0.4), spec = 50, matType = REFLECTIVE)
# mirror3 = Material(diffuse = (0.7, 0.4, 0.6), spec = 70, matType = REFLECTIVE)
# mirror4 = Material(diffuse = (0.9, 0.1, 0.9), spec = 64, matType = REFLECTIVE)


# rt3 
floor = Material(diffuse = (0.64, 0.64, 0.64), spec = 64, matType = OPAQUE)
sides = Material(diffuse = (0.8, 0.8, 0.8), spec = 46, matType = OPAQUE)

# rtx.envMap = Texture("envs/bg-640x640.bmp")
# rtx.envMap = Texture("envs/parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.4 ))
rtx.lights.append( DirectionalLight(direction = (0,0,-1), intensity = 0.75 ))
rtx.lights.append( DirectionalLight(direction = (0,-1,0), intensity = 0.75 ))


# # up down
rtx.scene.append( Plane(position=(0, 5, 10), normal=(0,-1,0), material=floor) )
rtx.scene.append( Plane(position=(0, -5, -15), normal=(0,0.5,0), material=floor) )

# sides
rtx.scene.append( Plane(position=(-5, 0, -10), normal=(-1,0,0), material=sides) )
rtx.scene.append( Plane(position=(5, 0, -10), normal=(1,0,0), material=sides) )

# back
rtx.scene.append( Plane(position=(0, 0, -20), normal=(0,0,-1), material=sides) )

# aditional
rtx.scene.append( Disk(position=(0, -3, -10), normal=(0,1,0), radius=1, material=mirror1) )
# rtx.scene.append( AABB(position=(0, -2, -10), size=(0.5,1,1.5), material=mirror2) )
# rtx.scene.append(AABB(position=(-2, 2, -5), size=(2, 2, 2), material=mirror2))

rtx.glRender()
rtx.glFinish("outputs/output2.bmp")