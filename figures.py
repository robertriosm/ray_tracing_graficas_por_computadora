
from experiments import vector_by_const

from rmath import dot, normalize_vector, subtract, add

WHITE = (1,1,1)
BLACK = (0,0,0)

class Intersect(object):
    def __init__(self, distance, point, normal, sceneObj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.sceneObj = sceneObj

class Material(object):
    def __init__(self, diffuse = WHITE):
        self.diffuse = diffuse


class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        L = subtract([self.center[0], self.center[1], self.center[2]], [orig[0], orig[1], orig[2]])
        
        # L = np.subtract(self.center, orig)
        tca = dot(L, [dir[0], dir[1], dir[2]])
        d = (normalize_vector(L) ** 2 - tca ** 2) ** 0.5

        # tca = np.dot(L, dir)
        # d = (np.linalg.norm(L) ** 2 - tca ** 2) ** 0.5

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

        # P = np.add(orig, vector_by_const([dir[0],dir[1],dir[2]], t0))
        # normal = np.subtract(P, self.center)
        # normal = normal / np.linalg.norm(normal)

        P = add([orig[0],orig[1],orig[2]], vector_by_const([dir[0],dir[1],dir[2]], t0))
        normal = subtract(P, [self.center[0], self.center[1], self.center[2]])
        normal = vector_by_const(normal, 1/normalize_vector(normal)) 

        return Intersect(distance = t0,
                         point = P,
                         normal = normal,
                         sceneObj = self)