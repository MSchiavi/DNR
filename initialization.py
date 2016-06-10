from math import *
from sympy import Symbol

class Initialization(object):

	meh = [(Symbol('p')-Symbol('k'))**2,(Symbol('q')-Symbol('k'))**2,(Symbol('k'))**2]

	def __init__(self, Propagators):
		super(Initialization, self).__init__()
		self.Propagators = Propagators
		print(self.meh)
		print(self.meh[0].expand())
	#def find_squares(self):





Initialize = Initialization("potato")