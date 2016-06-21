from sympy import poly
from sympy.abc import x,k,P
from sympy import *

p = poly(x ** 5 + 2 * x ** 4 - x ** 3 - 2 * x ** 2 + x + 1,x)
temp = poly(diff(p,Symbol('y'),1),Symbol('y'))
print(temp)
print(temp.args)
print(len(temp.args))
for i in range(len(temp.args)):
	print(temp.args[i])