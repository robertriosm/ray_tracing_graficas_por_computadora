
from gl import Raytracer
from figures import AABB, TRANSPARENT, Disk, Material, REFLECTIVE, Sphere, Triangle
from lights import AmbientLight, DirectionalLight
from texture import Texture

width = 1000
height = 1000

rtx = Raytracer(width, height)

# materials and textures
podium = Material(spec = 64, ior = 2.417, matType = TRANSPARENT)
gold = Material(diffuse = (1, 0.8, 0), spec = 32, matType = REFLECTIVE)
carpet = Material(diffuse = (0.6,0.2,0.2))

star1 = Material(texture= Texture("materials/star1.bmp"), matType=TRANSPARENT)
star2 = Material(texture= Texture("materials/star2.bmp"), matType=TRANSPARENT)
star3 = Material(texture= Texture("materials/star3.bmp"), matType=TRANSPARENT)
star4 = Material(texture= Texture("materials/star4.bmp"), matType=TRANSPARENT)
star5 = Material(texture= Texture("materials/star5.bmp"), matType=TRANSPARENT)
star6 = Material(texture= Texture("materials/star6.bmp"), matType=TRANSPARENT)
star7 = Material(texture= Texture("materials/star7.bmp"), matType=TRANSPARENT)

# env
rtx.envMap = Texture("envs/darkskybg.bmp")

# lights
rtx.lights.append( AmbientLight(intensity = 0.25 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.60 ))

# scene objects

#star
rtx.scene.append(Triangle(vertices=((0-3, 1.75, -10+0.501), (-0.25-3, 0.25+1.75, -10+0.501), (0.25-3, 0.25+1.75, -10+0.501)), material=gold)) 
rtx.scene.append(Triangle(vertices=((0-3, 1.75, -10+0.501), (-0.2-3, -0.15+1.75, -10+0.501), (0-3, 0.5+1.75, -10+0.501)), material=gold))
rtx.scene.append(Triangle(vertices=((0-3, 1.75, -10+0.501), (0.2-3, -0.15+1.75, -10+0.501), (0-3, 0.5+1.75, -10+0.501)), material=gold))

#dragon balls
rtx.scene.append(Sphere(center=(0, 2, -10), radius=0.5,material=star1)) #1
rtx.scene.append(AABB(position=(0, 2-3.5, -10), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(0, 2-0.499, -10),radius=0.5, normal=(0,0.5,0), material=carpet))

rtx.scene.append(Sphere(center=(2, 1, -9), radius=0.5,material=star2)) #2
rtx.scene.append(AABB(position=(2, 1-3.5, -9), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(2, 1-0.499, -9),radius=0.5, normal=(0,0.5,0), material=carpet))


rtx.scene.append(Sphere(center=(2, -1, -7), radius=0.5,material=star3)) #3
rtx.scene.append(AABB(position=(2, -1-3.5, -7), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(2, -1-0.499, -7),radius=0.5, normal=(0,0.5,0), material=carpet))


rtx.scene.append(Sphere(center=(0, -2, -6), radius=0.5,material=star4)) #4
rtx.scene.append(AABB(position=(0, -2-3.5, -6), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(0, -2-0.499, -6),radius=0.5, normal=(0,0.5,0), material=carpet))


rtx.scene.append(Sphere(center=(-2, -1, -7), radius=0.5,material=star5)) #5
rtx.scene.append(AABB(position=(-2, -1-3.5, -7), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(-2, -1-0.499, -7),radius=0.5, normal=(0,0.5,0), material=carpet))


rtx.scene.append(Sphere(center=(-2, 1, -9), radius=0.5,material=star6)) #6
rtx.scene.append(AABB(position=(-2, 1-3.5, -9), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(-2, 1-0.499, -9),radius=0.5, normal=(0,0.5,0), material=carpet))


rtx.scene.append(Sphere(center=(0, 0, -8), radius=0.5,material=star7)) #7
rtx.scene.append(AABB(position=(0, 0-3.5, -8), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(0, 0-0.499, -8),radius=0.5, normal=(0,0.5,0), material=carpet))



rtx.glRender()
rtx.glFinish("outputs/outputfinal.bmp")