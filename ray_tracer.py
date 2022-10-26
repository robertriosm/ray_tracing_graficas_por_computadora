from gl import Raytracer
from figures import AABB, TRANSPARENT, Disk, Material, REFLECTIVE, OPAQUE, Sphere, Triangle
from lights import AmbientLight, DirectionalLight
from texture import Texture

width = 800
height = 800

rtx = Raytracer(width, height)

# materials
dragonballtexture = Material(diffuse = (1, 0.6, 0.2), spec = 80, matType = REFLECTIVE)
podium = Material(diffuse = (0.4,0.4,0.4), spec = 64, matType=TRANSPARENT)
star = Material(diffuse = (1, 0, 0), spec = 32, matType = OPAQUE)
carpet = Material(diffuse = (0.6,0.2,0.2), matType= OPAQUE)

# env
rtx.envMap = Texture("envs/darkskybg.bmp")

# lights
rtx.lights.append( AmbientLight(intensity = 0.25 ))
rtx.lights.append( DirectionalLight(direction = (0,-1,0), intensity = 0.5 ))
rtx.lights.append( DirectionalLight(direction = (0,0,-1), intensity = 0.25 ))


# scene objects
rtx.scene.append(Sphere(center=(0, 2, -10), radius=0.5,material=dragonballtexture)) #1
rtx.scene.append(AABB(position=(0, 2-3.5, -10), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(0, 2-0.499, -10),radius=0.5, normal=(0,0.5,0), material=carpet))
#star
rtx.scene.append(Triangle(vertices=((0, 1.75, -10+0.501), (-0.25, 0.25+1.75, -10+0.501), (0.25, 0.25+1.75, -10+0.501)), material=star)) 
rtx.scene.append(Triangle(vertices=((0, 1.75, -10+0.501), (-0.2, -0.15+1.75, -10+0.501), (0, 0.5+1.75, -10+0.501)), material=star))
rtx.scene.append(Triangle(vertices=((0, 1.75, -10+0.501), (0.2, -0.15+1.75, -10+0.501), (0, 0.5+1.75, -10+0.501)), material=star))


rtx.scene.append(Sphere(center=(2, 1, -9), radius=0.5,material=dragonballtexture)) #2
rtx.scene.append(AABB(position=(2, 1-3.5, -9), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(2, 1-0.499, -9),radius=0.5, normal=(0,0.5,0), material=carpet))
# star
rtx.scene.append(Triangle(vertices=((2, 1, -9+0.501), (-0.25+2, 0.25+1, -9+0.501), (0.25+2, 0.25+1, -9+0.501)), material=star)) 
rtx.scene.append(Triangle(vertices=((2, 1, -9+0.501), (-0.2+2, -0.15+1, -9+0.501), (0+2, 0.5+1, -9+0.501)), material=star))
rtx.scene.append(Triangle(vertices=((2, 1, -9+0.501), (0.2+2, -0.15+1, -9+0.501), (0+2, 0.5+1.75, -9+0.501)), material=star))


rtx.scene.append(Sphere(center=(2, -1, -7), radius=0.5,material=dragonballtexture)) #3
rtx.scene.append(AABB(position=(2, -1-3.5, -7), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(2, -1-0.499, -7),radius=0.5, normal=(0,0.5,0), material=carpet))
# rtx.scene.append(Triangle(vertices=((-2, 2, -10), (-3, 4, -10), (-4, 4, -11)), material=star))


rtx.scene.append(Sphere(center=(0, -2, -6), radius=0.5,material=dragonballtexture)) #4
rtx.scene.append(AABB(position=(0, -2-3.5, -6), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(0, -2-0.499, -6),radius=0.5, normal=(0,0.5,0), material=carpet))
# rtx.scene.append(Triangle(vertices=((-2, 2, -10), (-3, 4, -10), (-4, 4, -11)), material=star))


rtx.scene.append(Sphere(center=(-2, -1, -7), radius=0.5,material=dragonballtexture)) #5
rtx.scene.append(AABB(position=(-2, -1-3.5, -7), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(-2, -1-0.499, -7),radius=0.5, normal=(0,0.5,0), material=carpet))
# rtx.scene.append(Triangle(vertices=((-2, 2, -10), (-3, 4, -10), (-4, 4, -11)), material=star))


rtx.scene.append(Sphere(center=(-2, 1, -9), radius=0.5,material=dragonballtexture)) #6
rtx.scene.append(AABB(position=(-2, 1-3.5, -9), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(-2, 1-0.499, -9),radius=0.5, normal=(0,0.5,0), material=carpet))
# rtx.scene.append(Triangle(vertices=((-2, 2, -10), (-3, 4, -10), (-4, 4, -11)), material=star))


rtx.scene.append(Sphere(center=(0, 0, -8), radius=0.5,material=dragonballtexture)) #7
rtx.scene.append(AABB(position=(0, 0-3.5, -8), size=(1,6,1), material=podium))
rtx.scene.append(Disk(position=(0, 0-0.499, -8),radius=0.5, normal=(0,0.5,0), material=carpet))
# rtx.scene.append(Triangle(vertices=((-2, 2, -10), (-3, 4, -10), (-4, 4, -11)), material=star))

# rtx.scene.append(Plane(position=(0, -15, 0), normal=(0,0.1,0), material=carpet))

rtx.glRender()
rtx.glFinish("outputs/outputt2.bmp")