import numpy

def getEquidistantPoints(p1, p2, parts):
    return zip(numpy.linspace(p1[0], p2[0], parts+1),
               numpy.linspace(p1[1], p2[1], parts+1))
pts = list(getEquidistantPoints((0,0), (100,100), 20))
print(pts)