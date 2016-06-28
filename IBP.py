#    Author: Matthew Schiavi
#	 Last Edit: 06-27-16
#
#	Generates IBP relationships based off of Internal, External, and Propagators which are defined in the input file.
#
#
#
#


from math import *
from sympy import *
from initialization import *
One = type(Abs(1)/Abs(1))

class IBP(object):

	def __init__(self,x,y):
		super(IBP, self).__init__()
		self.x = x
		self.y = y
		#Creating object which contains Squares, inverse matrix for IBP creation, propagators,internal and external momenta.
		Brew = Initialization()
		print(Brew.External_Matrix())
		Props = Brew.get_props()
		self.rep(Props,Brew.find_squares())


	def rep(self,Props,Squares):
		DProps = []
		coeffs = []

		#Takes derivative of Propagator with respect to x input and multiplies by y
		for i in range(len(Props)):
			DProps.append((diff(Props[i],self.x,1)*self.y).expand())

		coeffs = [[0 for x in range(len(Squares))]for y in range(len(DProps))]

		#Gets the coefficient of the DProp terms with respect to the Squares. For instance if DProps is [2*k**2 - 2*k*p, 2*k**2 + 2*k*q, 2*k**2] 
		#and squares is [k*p, k**2, k*q] coeffs will be [[-2,2,0],[0,2,2],[0,2,0]]

		for i in range(len(DProps)):

			for j in range(len(Squares)):
				if type(DProps[i].args[0]) is Integer:
					print(DProps[i].args)
					if type(DProps[i].args[1]/Squares[j]) is One:
						coeffs[i][j]=(DProps[i].args[0])
					else:
						coeffs[i][j] = 0
			
				else:
					for k in range(len(DProps[i].args)):
						if type(DProps[i].args[k]/Squares[j]) is Integer:
							coeffs[i][j] = (DProps[i].args[k]/Squares[j])



		print(Squares)
		print(coeffs)
		#print(self.x-Matrix(coeffs)*Matrix(Squares))
		
		



k = Symbol('k')
y = Symbol('k')
IBP = IBP(k,y)