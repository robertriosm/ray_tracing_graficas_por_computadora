
from experiments import vector_by_const
from rmath import dot_product, magnitud_vector, normalizaVector, suma_o_resta_vectores
from math import pi, atan2, acos

import numpy as np


WHITE = (1,1,1)
BLACK = (0,0,0)

OPAQUE = 0
REFLECTIVE = 1
TRANSPARENT = 2

class Intersect(object):
    def __init__(self, distance, point, normal, sceneObj, textCoords):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.sceneObj = sceneObj
        self.textCoords = textCoords

class Material(object):
    def __init__(self, diffuse = WHITE, spec = 1.0, ior = 1.0, matType = OPAQUE, texture = None):
        self.diffuse = diffuse
        self.spec = spec
        self.ior = ior
        self.matType = matType
        self.texture = texture


class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        L = suma_o_resta_vectores(self.center, orig, True)
        tca = dot_product(L, dir)
        d = (magnitud_vector(L) ** 2 - tca ** 2) ** 0.5


        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d ** 2) ** 0.5

        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None
        
        # P = O + t0 * D
        P = suma_o_resta_vectores(orig, vector_by_const(dir, t0))
        normal = suma_o_resta_vectores(P, self.center, True)
        normal = normalizaVector(normal) 

        u = atan2(normal[2], normal[0])/ (2 * pi) + 0.5
        v = acos(-normal[1])/pi
        uvs  = (u, v)

        return Intersect(distance = t0,
                         point = P,
                         normal = normal,
                         sceneObj = self,
                         textCoords = uvs)


# quitarle numpy:
class Plane(object):
    def __init__(self, position, normal, material) -> None:
        self.position = position
        self.normal = normalizaVector(normal)
        self.material = material
    
    def ray_intersect(self, orig, dir):
        denom = dot_product(dir, self.normal) # here!!
        #((planePos - origRayo) o normal) / (direccionrayo o normal) 

        if abs(denom) > 0.0001:
            num = dot_product(np.subtract(self.position, orig), self.normal)
        
            t = num / denom
        
            if t > 0:
                P = np.add(orig, t * np.array(dir))
                return Intersect(distance = t,
                                 point = P,
                                 normal = self.normal,
                                 sceneObj = self,
                                 textCoords = None)
        return None 
                            

class AABB(object): # axis aligned bounding box
    def __init__(self, position, size, material) -> None:
        self.position = position
        self.size = size
        self.material = material

        self.planes = []

        halfSizes = [0,0,0]

        halfSizes[0] = halfSizes[0] / 2
        halfSizes[1] = halfSizes[1] / 2
        halfSizes[2] = halfSizes[2] / 2


        # sides
        self.planes.append(Plane(position=np.add(position, (halfSizes[0], 0, 0)), normal=(1,0,0), material=material))
        self.planes.append(Plane(position=np.subtract(position, (-halfSizes[0], 0, 0)), normal=(-1,0,0), material=material))

        #up and down
        self.planes.append(Plane(position=np.add(position, (0, halfSizes[1], 0)), normal=(0,1,0), material=material))
        self.planes.append(Plane(position=np.subtract(position, (0, halfSizes[1], 0)), normal=(0,-1,0), material=material))

        #front back
        self.planes.append(Plane(position=np.add(position, (0, 0, halfSizes[2])), normal=(0,0,1), material=material))
        self.planes.append(Plane(position=np.subtract(position, (0, 0, halfSizes[2])), normal=(0,0,-1), material=material))

        # infinite?
        self.boundsMin = [0,0,0]
        self.boundsMax = [0,0,0]

        #margen de error
        epsilon = 0.001

        for i in range(3):
            self.boundsMin[i] = self.position[i] - (epsilon + halfSizes[i])
            self.boundsMax[i] = self.position[i] + (epsilon + halfSizes[i])

    
    def ray_intersect(self, orig, dir):
        intersect = None
        t = float('inf')

        for plane in self.planes:
            planeInter = plane.ray_intersect(orig, dir)

            if planeInter is not None:
                planePoint = planeInter.point

                if (self.boundsMin[0] <= planePoint[0] <= self.boundsMax[0]) and (self.boundsMin[1] <= planePoint[1] <= self.boundsMax[1]) and (self.boundsMin[2] <= planePoint[2] <= self.boundsMax[2]):
                    if planeInter.distance < t:
                        t = planeInter.distance
                        intersect = planeInter

                    # tex coords

                    u,v = 0,0

                    if abs(plane.normal[0]) > 0:
                        u = (planeInter.point[1] - self.boundsMin[1]) / (self.boundsMax[1] - self.boundsMin[1])
                        v = (planeInter.point[2] - self.boundsMin[2]) / (self.boundsMax[2] - self.boundsMin[2])
                    elif abs(plane.normal[1]) > 0:
                        u = (planeInter.point[0] - self.boundsMin[0]) / (self.boundsMax[0] - self.boundsMin[0])
                        v = (planeInter.point[2] - self.boundsMin[2]) / (self.boundsMax[2] - self.boundsMin[2])
                    elif abs(plane.normal[2]) > 0:
                        u = (planeInter.point[0] - self.boundsMin[0]) / (self.boundsMax[0] - self.boundsMin[0])
                        v = (planeInter.point[1] - self.boundsMin[1]) / (self.boundsMax[1] - self.boundsMin[1])

        if intersect is None:
            return None
        
        return Intersect(
            distance=t,
            point=intersect.point,
            normal=intersect.normal,
            texcoords=(u, v),
            sceneObj=self,
        )

class Disk(object):
    def __init__(self, position, radius, normal, material) -> None:
        self.plane = Plane(position, normal, material)
        self.material = material
        self.radius = radius
    
    def ray_intersect(self, orig, dir):
        intersect = self.plane.ray_intersect(orig, dir)

        if intersect is None:
            return None

        contact = np.subtract(intersect.point, self.plane.position)
        contact = normalizaVector(contact)

        if contact > self.radius:
            return None
        
        return Intersect(distance=intersect.distance,
                         point=intersect.point,
                         normal=intersect.normal,
                         sceneObj=self,
                         textCoords=None)