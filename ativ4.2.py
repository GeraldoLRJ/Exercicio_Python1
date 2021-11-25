import math
import numpy

x=float(input('Digite um angulo'))

x= numpy.deg2rad(x)

seno=math.sin(x)
cos=math.cos(x)
tang=math.tan(x)

print('Seno: ',seno,'\nCoseno: ', cos,'\nTangente: ', tang)