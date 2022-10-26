
from experiments import vector_add_const, vector_by_const, EPSILON
from rmath import add, angle_between, cross_product, dot, dot_product, magnitud_vector, norm_vector, normalize_vector, add_subtract
from math import pi, atan2, acos, fabs


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
        L = add_subtract(self.center, orig, True)
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
        P = add_subtract(orig, vector_by_const(dir, t0))
        normal = add_subtract(P, self.center, True)
        normal = norm_vector(normal) 

        u = atan2(normal[2], normal[0])/ (2 * pi) + 0.5
        v = acos(-normal[1])/pi
        uvs  = (u, v)

        return Intersect(distance = t0,
                         point = P,
                         normal = normal,
                         sceneObj = self,
                         textCoords = uvs)


class Plane(object):
    def __init__(self, position, normal, material) -> None:
        self.position = position
        self.normal = norm_vector(normal)
        self.material = material
    
    def ray_intersect(self, orig, dir):
        denom = dot_product(dir, self.normal) # here!!
        #((planePos - origRayo) o normal) / (direccionrayo o normal) 

        if abs(denom) > 0.0001:
            num = dot_product(add_subtract(self.position, orig, True), self.normal)
            # heeeeeeeeeereeeeeeee
            t = num / denom
        
            if t > 0:
                P = add_subtract(orig, vector_by_const(dir, t)) # esta

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

        halfSizes[0] = size[0] / 2
        halfSizes[1] = size[1] / 2
        halfSizes[2] = size[2] / 2


        # sides
        self.planes.append(Plane(position=add_subtract(position, (halfSizes[0], 0, 0)),
                                 normal=(1,0,0), 
                                 material=material))
        self.planes.append(Plane(position=add_subtract(position, (halfSizes[0], 0, 0), True), 
                                 normal=(-1,0,0), 
                                 material=material))

        #up and down
        self.planes.append(Plane(position=add_subtract(position, (0, halfSizes[1], 0)), 
                                 normal=(0,1,0), 
                                 material=material))
        self.planes.append(Plane(position=add_subtract(position, (0, halfSizes[1], 0), True), 
                                 normal=(0,-1,0), 
                                 material=material))

        #front back
        self.planes.append(Plane(position=add_subtract(position, (0, 0, halfSizes[2])), 
                                 normal=(0,0,1), 
                                 material=material))
        self.planes.append(Plane(position=add_subtract(position, (0, 0, halfSizes[2]), True), 
                                 normal=(0,0,-1), 
                                 material=material))

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
        t = float("inf")

        for plane in self.planes:
            planeInter = plane.ray_intersect(orig, dir)

            if planeInter is not None:
                planePoint = planeInter.point

                
                if self.boundsMin[0] <= planePoint[0] <= self.boundsMax[0]:
                    if self.boundsMin[1] <= planePoint[1] <= self.boundsMax[1]:
                        if self.boundsMin[2] <= planePoint[2] <= self.boundsMax[2]:
                            if planeInter.distance < t:
                                t = planeInter.distance
                                intersect = planeInter

                            # Tex coords

                            u, v = 0, 0

                            # Las uvs de las caras de los lados
                            if abs(plane.normal[0]) > 0:
                                # Mapear uvs para el eje x, usando las coordenadas de Y y Z
                                u = (planeInter.point[1] - self.boundsMin[1]) / (self.size[1])
                                v = (planeInter.point[2] - self.boundsMin[2]) / (self.size[2])

                            elif abs(plane.normal[1]) > 0:
                                # Mapear uvs para el eje y, usando las coordenadas de X y Z
                                u = (planeInter.point[0] - self.boundsMin[0]) / (self.size[0])
                                v = (planeInter.point[2] - self.boundsMin[2]) / (self.size[2])

                            elif abs(plane.normal[2]) > 0:
                                # Mapear uvs para el eje z, usando las coordenadas de X y Y
                                u = (planeInter.point[0] - self.boundsMin[0]) / (self.size[0])
                                v = (planeInter.point[1] - self.boundsMin[1]) / (self.size[1])


        if intersect is None:
            return None

        return Intersect(
            distance=t,
            point=intersect.point,
            normal=intersect.normal,
            sceneObj=self,
            textCoords=(u, v))


class Disk(object):
    def __init__(self, position, radius, normal, material) -> None:
        self.plane = Plane(position, normal, material)
        self.material = material
        self.radius = radius
    
    def ray_intersect(self, orig, dir):
        intersect = self.plane.ray_intersect(orig, dir)

        if intersect is None:
            return None

        contact = add_subtract(intersect.point, self.plane.position, True)
        contact = normalize_vector(contact)

        if contact > self.radius:
            return None
        
        return Intersect(distance=intersect.distance,
                         point=intersect.point,
                         normal=intersect.normal,
                         sceneObj=self,
                         textCoords=None)
                    

    
class Triangle(object):
    def __init__(self, vertices, material, t = 0.0) -> None:
        
        self.vertices = vertices # ((a,b,c), (a,b,c), (a,b,c))

        self.v0_v1 = add_subtract(self.vertices[1], self.vertices[0], True)
        self.v0_v2 = add_subtract(self.vertices[2], self.vertices[0], True)

        self.n = cross_product(self.v0_v2, self.v0_v2)

        self.material = material

        self.t = t


    def ray_intersect(self, orig, dir):

        # ray direction

        pvector = cross_product(dir,self.v0_v2)

        det = dot_product(self.v0_v1,pvector)

        if det < 0.0001:
            return None
        
        inverse_det = 1/det

        tvec = add_subtract(orig, self.vertices[0], True)

        u = dot_product(tvec, pvector) * inverse_det

        if u < 0 or u > 1:
            return None

        qvec = cross_product(tvec, self.v0_v1)

        v = dot_product(dir, qvec) * inverse_det

        if v < 0 or u+v > 1:
            return None

        point = add_subtract(orig, vector_by_const(dir,self.t))

        # point = dot_product(self.v0_v2, qvec) * inverse_det
        
        return Intersect(
            distance=self.t,
            point=point,
            normal=self.n,
            textCoords=None,
            sceneObj=self)


        """


        ray_direction = dot_product(self.n,dir)

        if fabs(ray_direction) < EPSILON:
            return None
        

        d = -(dot_product(self.n, self.vertices[0]))


        self.t = -(dot_product(self.n, orig) + d) / ray_direction
        
        if self.t < 0:
            return None

        # point = orig + self.t * dir

        point = add_subtract(orig, vector_by_const(dir,self.t))


        # CHECK IF RAY IS INSIDE TRIANGLE VERTICES
         
        # vertex 0


        a = add_subtract(self.vertices[1],self.vertices[0], True)
        a_point = add_subtract(point, self.vertices[0])
        c = cross_product(a, a_point)

        if dot_product(self.n, c) < 0:
            return None
        
        

        # b = add_subtract(self.vertices[2],self.vertices[0], True)
        # c = add_subtract(point, self.vertices[0], True)

        # if angle_between(a,b) <= angle_between(a,c):
        #     return None

        # if dot_product(self.n, ) < 0:
        #     return None

        # vertex 1

        a = add_subtract(self.vertices[2],self.vertices[1], True)
        a_point = add_subtract(point, self.vertices[1])
        c = cross_product(a, a_point)

        if dot_product(self.n, c) < 0:
            return None

        # a = add_subtract(self.vertices[0],self.vertices[1], True)
        # b = add_subtract(self.vertices[2],self.vertices[1], True)
        # c = add_subtract(point, self.vertices[1], True)

        # if angle_between(b,a) <= angle_between(b,c):
        #     return None

        # vertex 2

        a = add_subtract(self.vertices[0],self.vertices[2], True)
        a_point = add_subtract(point, self.vertices[2])
        c = cross_product(a, a_point)

        if dot_product(self.n, c) < 0:
            return None

        # a = add_subtract(self.vertices[0],self.vertices[2], True)
        # b = add_subtract(self.vertices[1],self.vertices[2], True)
        # c = add_subtract(point, self.vertices[2], True)

        # if angle_between(a,b) <= angle_between(a,c):
        #     return None

        return Intersect(
            distance=self.t,
            point=point,
            normal=self.n,
            textCoords=None,
            sceneObj=self)

        """