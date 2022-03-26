import math
d, h, w = map(int, input().split())

a = (d*d)/(h*h+w*w)
a = math.sqrt(a)

print('%d %d'%(h*a, w*a))