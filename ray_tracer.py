from gl import Raytracer, V3
from texture import Texture
from figures import AABB, TRANSPARENT, Disk, Plane, Sphere, Material, REFLECTIVE, OPAQUE
from lights import AmbientLight, DirectionalLight


width = 256
height = 256


rtx = Raytracer(width, height)

brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16, matType = TRANSPARENT)
stone = Material(diffuse = (0.4, 0.4, 0.3), spec = 8, matType = OPAQUE)
mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = TRANSPARENT)
mirror2 = Material(diffuse = (0.7, 0.8, 0.4), spec = 50, matType = REFLECTIVE)
mirror3 = Material(diffuse = (0.7, 0.4, 0.6), spec = 70, matType = REFLECTIVE)
mirror4 = Material(diffuse = (0.9, 0.1, 0.9), spec = 64, matType = REFLECTIVE)

# rtx.envMap = Texture("bg-640x640.bmp")
rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.25 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.9 ))

# rtx.scene.append( Sphere(V3(-3,2,-10), 1, mirror)  )
# rtx.scene.append( Sphere(V3(-3,-2,-10), 1, brick)  )

# rtx.scene.append( Sphere(V3(0,2,-10), 1, stone)  )
# rtx.scene.append( Sphere(V3(0,-2,-10), 1, mirror2)  )

# rtx.scene.append( Sphere(V3(3,2,-10), 1, mirror3)  )
# rtx.scene.append( Sphere(V3(3,-2,-10), 1, mirror4)  )

rtx.scene.append( Sphere(V3(0,0,-10), 1, stone)  )


# rt3 here =======================================
# # up down
# rtx.scene.append( Plane(position=(0, -5, -10), normal=(0,1,0), material=mirror3) )
# rtx.scene.append( Plane(position=(0, 5, -10), normal=(0,-1,0), material=mirror2) )

# # sides
# rtx.scene.append( Plane(position=(-5, 0, -10), normal=(1,0,0), material=mirror) )
# rtx.scene.append( Plane(position=(5, 0, -10), normal=(-1,0,0), material=mirror4) )

# # back
# rtx.scene.append( Plane(position=(0, 0, -20), normal=(0,0,1), material=brick) )

# # rtx.scene.append( Disk(position=(0, -3, -10), normal=(0,1,0), radius=3, material=mirror4) )

# rtx.scene.append( AABB(position=(0, 2, -10), size=(2,2,2), material=mirror2) )


rtx.glRender()
rtx.glFinish("output.bmp")