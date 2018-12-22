from pickle import *

h = dumps((1, 2, 3))
k = h
print(loads(k)[1])
