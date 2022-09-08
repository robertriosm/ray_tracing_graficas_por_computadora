from gl import Raytracer, V3
from figures import *
from lights import *

width = 300
height = 300

# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3))
# stone = Material(diffuse = (0.4, 0.4, 0.4))
grass = Material(diffuse = (0.3, 1, 0.3))
snow = Material(diffuse = (0.8, 0.8, 0.8))
carbon = Material(diffuse = (0.3, 0.3, 0.3))

rtx = Raytracer(width, height)

rtx.lights.append(AmbientLight( ))
rtx.lights.append(DirectionalLight(direction = (0,0,-1)))

#cuerpo
rtx.scene.append(Sphere(V3(0,-2,-10), 2.5, snow))
rtx.scene.append(Sphere(V3(0,1,-10), 2, snow))
rtx.scene.append(Sphere(V3(0,3,-10), 1.5, snow))

#botones
rtx.scene.append(Sphere(V3(0,-1.8,-7.5), 0.3, carbon))
rtx.scene.append(Sphere(V3(0,1,-8), 0.3, carbon))
rtx.scene.append(Sphere(V3(0,-0.1,-8), 0.3, carbon))

# cara
rtx.scene.append(Sphere(V3(-0.75,2.7,-8), 0.1, carbon))
rtx.scene.append(Sphere(V3(-0.25,2.5,-8), 0.1, carbon))
rtx.scene.append(Sphere(V3(0.25,2.5,-8), 0.1, carbon))
rtx.scene.append(Sphere(V3(0.75,2.7,-8), 0.1, carbon))
rtx.scene.append(Sphere(V3(0,3,-8.5), 0.3, brick))


rtx.glRender()

rtx.glFinish("snowman.bmp")