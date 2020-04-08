import numpy
import theano.tensor as T
from theano import function

x = T.dscalar('x')
y = T.dscalar('y')
z = x + y 
f = function([x, y], z)
f(5, 7)


x = T.dmatrix('x')
y = T.dmatrix('y')
z = x + y
f = function([x, y], z)
f([[30, 50], [2, 3]], [[60, 70], [3, 4]])


a = tensor.dmatrix('a')
sig = 1 / (1 + tensor.exp(-a)) 
log = theano.function([a], sig)
print(log([[0, 1], [-1, -2]]))
