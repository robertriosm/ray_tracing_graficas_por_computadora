
from gl import Raytracer
from figures import AABB, TRANSPARENT, Disk, Material, REFLECTIVE, Sphere, Triangle
from lights import AmbientLight, DirectionalLight, PointLight
from texture import Texture

width = 800
height = 800

rtx = Raytracer(width, height)

# materials and textures
podium = Material(diffuse = (0.41,0.42,0.73), spec = 64, ior = 3.1416, matType = TRANSPARENT)
red = Material(diffuse = (0.83,0.22,0.37), matType = TRANSPARENT, ior = 2.42)

star1 = Material(texture= Texture("materials/star1.bmp"), matType=REFLECTIVE)
star2 = Material(texture= Texture("materials/star2.bmp"), matType=REFLECTIVE)
star3 = Material(texture= Texture("materials/star3.bmp"), matType=REFLECTIVE)
star4 = Material(texture= Texture("materials/star4.bmp"), matType=REFLECTIVE)
star5 = Material(texture= Texture("materials/star5.bmp"), matType=REFLECTIVE)
star6 = Material(texture= Texture("materials/star6.bmp"), matType=REFLECTIVE)
star7 = Material(texture= Texture("materials/star7.bmp"), matType=REFLECTIVE)

# env
rtx.envMap = Texture("envs/darkskybg.bmp")

# lights
rtx.lights.append( AmbientLight(intensity = 0.25 ))
rtx.lights.append( DirectionalLight(direction = (0,-1,-1), intensity = 0.30 ))
rtx.lights.append( DirectionalLight(direction = (0,-.6,0), intensity = 0.45 ))
rtx.lights.append( PointLight(point = (0, 1.5, -6), color=(0.54,0.26,0.31)))
rtx.lights.append( PointLight(point = (2, 2.5, -3), color=(0.31,0.26,0.54)))

# scene objects

#dragon balls
rtx.scene.append(Sphere(center=(0, 2, -10), radius=0.5,material=star1)) #1
rtx.scene.append(AABB(position=(0, 2-3.5, -10), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(0, 2-0.499, -10),radius=0.5, normal=(0,0.5,0), material=red))
#triangle
rtx.scene.append(Triangle(vertices=((0, 1, -10+0.501), (-0.5, 1.25, -10+0.501), (0.5, 1.25, -10+0.501)), material=red))


rtx.scene.append(Sphere(center=(2, 1, -9), radius=0.5,material=star2)) #2
rtx.scene.append(AABB(position=(2, 1-3.5, -9), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(2, 1-0.499, -9),radius=0.5, normal=(0,0.5,0), material=red))


rtx.scene.append(Sphere(center=(2, -1, -7), radius=0.5,material=star3)) #3
rtx.scene.append(AABB(position=(2, -1-3.5, -7), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(2, -1-0.499, -7),radius=0.5, normal=(0,0.5,0), material=red))


rtx.scene.append(Sphere(center=(0, -2, -6), radius=0.5,material=star4)) #4
rtx.scene.append(AABB(position=(0, -2-3.5, -6), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(0, -2-0.499, -6),radius=0.5, normal=(0,0.5,0), material=red))


rtx.scene.append(Sphere(center=(-2, -1, -7), radius=0.5,material=star5)) #5
rtx.scene.append(AABB(position=(-2, -1-3.5, -7), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(-2, -1-0.499, -7),radius=0.5, normal=(0,0.5,0), material=red))


rtx.scene.append(Sphere(center=(-2, 1, -9), radius=0.5,material=star6)) #6
rtx.scene.append(AABB(position=(-2, 1-3.5, -9), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(-2, 1-0.499, -9),radius=0.5, normal=(0,0.5,0), material=red))


rtx.scene.append(Sphere(center=(0, 0, -8), radius=0.5,material=star7)) #7
rtx.scene.append(AABB(position=(0, 0-3.5, -8), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(0, 0-0.499, -8),radius=0.5, normal=(0,0.5,0), material=red))


rtx.glRender()
rtx.glFinish("outputs/outputfinal.bmp")