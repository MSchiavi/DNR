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
from representation import *
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
		self.rep(Props,Brew.find_squares(),Brew.External_Matrix())


	def rep(self,Props,Squares,External_Matrix):
		DProps = []

		#Takes derivative of Propagator with respect to x input and multiplies by y
		for i in range(len(Props)):
			DProps.append((diff(Props[i],self.x,1)*self.y).expand())

		coeffs = [[0 for x in range(len(Squares))]for y in range(len(DProps))]
		temp = [[]for y in range(len(DProps))]

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

		# Some cleaning up storing thigns in the coeffs list
		for i in range(len(DProps)):
			coeffs[i].append(DProps[i] - transpose(Matrix(coeffs[i])).dot(Matrix(Squares)))
		
		# More math stuff storing thing sin temp list
		for i in range(len(coeffs)):
			temp[i] = transpose(Matrix(coeffs[i]))*External_Matrix
		
		output = [[] for y in range(len(temp))]

		#Creating the IBP output. Ladders is an object which represents creation and annihilation operators. The first arguement is which propagator 
		# it will effect and the second is if it is creation ('+') or annihilation ('-'). indicies is just the "a" term from the propagators. 
		print temp

		for i in range(len(temp)):
			for j in range(len(temp[i])):
				if j < (len(temp[i])-1):
					output[i].append([temp[i][j],ladders(j + 1,'-'),ladders(i + 1,'+'),indicies(i + 1)])
				else:
					output[i].append([temp[i][j],1,ladders(i + 1,'+'),indicies(i + 1)])

		output.append([diff(self.x,self.y)*Symbol('d')])


		print output

		readable = ""

		for i in range(len(output) - 1 ):

			for j in range(len(output[i])):
				if output[i][j][0] != 0:
					if output[i][j][0] == 1:
						
						readable = readable + "" + " - a("+ str(output[i][j][3].get_index())+")" + "Y("+str(output[i][j][1].get_index())+ "," + output[i][j][1].get_op()+ ")" + "Y("+ str(output[i][j][2].get_index())+ "," + output[i][j][2].get_op()+ ")"

					elif type(output[i][j][0]) is Integer and output[i][j][0] > 1:

						readable = readable + "" + " - " + str(output[i][j][0])  + "a("+ str(output[i][j][3].get_index())+")" + "Y("+str(output[i][j][1].get_index())+ "," + output[i][j][1].get_op()+ ")" + "Y("+ str(output[i][j][2].get_index())+ "," + output[i][j][2].get_op()+ ")" 
						#this will have to be coded at some point
					else:
						if output[i][j][0].args[0] == 1:
							readable = readable + "" + " - a("+ str(output[i][j][3].get_index())+ ")" + str(output[i][j][0]) + "Y("+ str(output[i][j][2].get_index())+ "," + output[i][j][2].get_op()+ ")" 
						elif output[i][j][0].args[0] == -1:
							readable = readable + "" + " + a("+ str(output[i][j][3].get_index())+ ")" + str(-1*output[i][j][0]) + "Y("+ str(output[i][j][2].get_index())+ "," + output[i][j][2].get_op()+ ")" 


		readable = readable + " + " + str(output[3][0])
		print readable
k = Symbol('k')
y = Symbol('k')
IBP = IBP(k,y)