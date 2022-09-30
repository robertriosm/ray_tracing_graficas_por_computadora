
from experiments import vector_by_const
from rmath import multiply_vectors, normalizaVector, normalize_vector, dot, dot_product, subtract, suma_o_resta_vectores, vectors_product
import numpy as np

DIR_LIGHT = 0
POINT_LIGHT = 1
AMBIENT_LIGHT = 2


def reflectVector(normal, direction):
    reflect = 2 * dot_product(normal, direction)
    reflect = [n*reflect for n in normal]
    reflect = suma_o_resta_vectores(reflect, direction, True)
    return normalizaVector(reflect)

def reflactVector(normal, direction, ior):
    #Snell´s Law
    cosi = max(-1, min(1, dot_product(direction, normal)))
    etai = 1
    etat = ior

    if cosi < 0:
        cosi = -cosi
    else: 
        etai, etat = etat, etai
        normal = [n * -1 for n in normal]

    eta = etai / etat
    k = 1 - (eta**2) * (1-(cosi**2))

    if k < 0: #Total internal reflection
        return None

    R = suma_o_resta_vectores([eta *(d) for d in direction],  [(eta * cosi - k **0.5) * n for n in  normal])
    return R
    

def fresnel(normal, direction, ior):
    #Snell´s Law  
    cosi = max(-1, min(1, dot_product(direction, normal)))
    etai = 1
    etat = ior

    if cosi > 0:
        etai, etat = etat, etai
    
    sint = etai / etat * (max(0, 1 - cosi**2) ** 0.5)

    if sint >= 1: #Total internal reflection
        return 1
    
    cost = max(0, 1 - sint**2) ** 0.5
    cosi = abs(cosi)

    Rs = ((etat * cosi) - (etai * cosi)) / ((etat * cosi) + (etai * cost))
    Rp = ((etai * cosi) - (etat * cosi)) / ((etai * cosi) + (etat * cost))

    return (Rs**2 + Rp**2)/2

class DirectionalLight(object):
    def __init__(self, direction = (0,-1,0), intensity = 1, color = (1,1,1)):
        self.direction = vector_by_const(direction, 1/normalize_vector(direction))
        self.intensity = intensity
        self.color = color
        self.lightType = DIR_LIGHT

    def getDiffuseColor(self, intersect, raytracer):
        light_dir = np.array(self.direction) * -1
        intensity = np.dot(intersect.normal, light_dir) * self.intensity
        intensity = float(max(0, intensity))            
                                                        
        diffuseColor = np.array([intensity * self.color[0],
                                 intensity * self.color[1],
                                 intensity * self.color[2]])

        return diffuseColor
    
    def getSpecColor(self, intersect, raytracer):
        light_dir = np.array(self.direction) * -1
        reflect = reflectVector(intersect.normal, light_dir)

        view_dir = np.subtract( raytracer.camPosition, intersect.point)
        view_dir = normalizaVector(view_dir)

        spec_intensity = self.intensity * max(0,np.dot(view_dir, reflect)) ** intersect.sceneObj.material.spec
        specColor = np.array([spec_intensity * self.color[0],
                              spec_intensity * self.color[1],
                              spec_intensity * self.color[2]])

        return specColor
    
    def getShadowIntensity(self, intersect, raytracer):
        light_dir = np.array(self.direction) * -1

        shadow_intensity = 0
        shadow_intersect = raytracer.scene_intersect(intersect.point, light_dir, intersect.sceneObj)
        if shadow_intersect:
            shadow_intensity = 1

        return shadow_intensity
    
class PointLight(object):
    def __init__(self, point, constant = 1.0, linear = 0.1, quad = 0.05, color = (1,1,1)):
        self.point = point
        self.constant = constant
        self.linear = linear
        self.quad = quad
        self.color = color
        self.lightType = POINT_LIGHT

    def getDiffuseColor(self, intersect, raytracer):
        light_dir = np.subtract(self.point, intersect.point)
        light_dir = normalizaVector(light_dir)

        attenuation = 1.0
        intensity = np.dot(intersect.normal, light_dir) * attenuation
        intensity = float(max(0, intensity))            
                                                        
        diffuseColor = np.array([intensity * self.color[0],
                                 intensity * self.color[1],
                                 intensity * self.color[2]])

        return diffuseColor

    def getSpecColor(self, intersect, raytracer):
        light_dir = np.subtract(self.point, intersect.point)
        light_dir = normalizaVector(light_dir)

        reflect = reflectVector(intersect.normal, light_dir)

        view_dir = np.subtract( raytracer.camPosition, intersect.point)
        view_dir = normalizaVector(view_dir)

        attenuation = 1.0

        spec_intensity = attenuation * max(0,np.dot(view_dir, reflect)) ** intersect.sceneObj.material.spec
        specColor = np.array([spec_intensity * self.color[0],
                              spec_intensity * self.color[1],
                              spec_intensity * self.color[2]])

        return specColor

    def getShadowIntensity(self, intersect, raytracer):
        light_dir = np.subtract(self.point, intersect.point)
        light_dir = normalizaVector(light_dir)

        shadow_intensity = 0
        shadow_intersect = raytracer.scene_intersect(intersect.point, light_dir, intersect.sceneObj)
        if shadow_intersect:
            shadow_intensity = 1

        return shadow_intensity

class AmbientLight(object):
    def __init__(self, intensity = 0.1, color = (1,1,1)):
        self.intensity = intensity
        self.color = color
        self.lightType = AMBIENT_LIGHT
    
    def getDiffuseColor(self, intersect, raytracer):
        return np.array(self.color) * self.intensity

    def getSpecColor(self, intersect, raytracer):
        return np.array([0,0,0])

    def getShadowIntensity(self, intersect, raytracer):
        return 0