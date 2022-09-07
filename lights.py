
from experiments import vector_by_const
from rmath import normalize
import numpy as np

DIR_LIGHT = 0
POINT_LIGHT = 1
AMBIENT_LIGHT = 2

class DirectionalLight(object):
    def __init__(self, direction = (0,-1,0), intensity = 1, color = (1,1,1)):
        normalized = np.linalg.norm(direction)
        mynormalized = normalize(direction)
        self.direction = direction / normalized
        # self.direction = vector_by_const(direction, 1/normalize(direction))
        self.intensity = intensity
        self.color = color
        self.lightType = DIR_LIGHT

class AmbientLight(object):
    def __init__(self, intensity = 0.1, color = (1,1,1)):
        self.intensity = intensity
        self.color = color
        self.lightType = AMBIENT_LIGHT