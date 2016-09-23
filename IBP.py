#    Author: Matthew Schiavi
#	 Last Edit: 07-12-16
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
import time

#start_time = time.time()
One = type(Abs(1)/Abs(1))

class IBP:

	def __init__(self):
		#super(IBP, self).__init__()
		#Creating object which contains Squares, inverse matrix for IBP creation, propagators,internal and external momenta.
		#Brew_time = time.time()
		self.Brew = Initialization()
		#print(Brew.External_Matrix())
		self.Props = self.Brew.get_props()
		#Ext_Mat_time = time.time()
		self.Ext_Mat = self.Brew.External_Matrix()
		#self.output = self.rep(Props,Brew.find_squares(),Brew.External_Matrix())
		#print("Ext_Mat_time:",'%.3f'%(time.time()-Ext_Mat_time) )
		#self.IBP_String = self.output_reader(self.output)
		#self.math_output = self.math_output(self.output)
		#print("Brew_time:",'%.3f'%(time.time()-Brew_time) )

	
	def Get_IBP(self,x,y):
		self.x = x
		self.y = y

		rep_time = time.time()
		self.output = self.rep(self.Props,self.Brew.find_squares(),self.Ext_Mat)
		print("rep_time:",'%.3f'%(time.time()-rep_time) )

		math_time = time.time()
		math = self.math_output(self.output)
		print("math_time:",'%.3f'%(time.time()-math_time) )
		
		return math


	def rep(self,Props,Squares,External_Matrix):
		DProps = []

		#Takes derivative of Propagator with respect to x input and multiplies by y
		for i in range(len(Props)):
			DProps.append((diff(Props[i],self.x,1)*self.y).expand())

		coeffs = [[0 for x in range(len(Squares))]for y in range(len(DProps))]
		temp = [[]for y in range(len(DProps))]

		#Gets the coefficient of the DProp terms with respect to the Squares. For instance if DProps is [2*k**2 - 2*k*p, 2*k**2 + 2*k*q, 2*k**2] 
		#and squares is [k*p, k**2, k*q] coeffs will be [[-2,2,0],[0,2,2],[0,2,0]]
		#print(DProps,"      DProps")
		#print(Squares,"     Squares")
		
		for i in range(len(DProps)):

			for j in range(len(Squares)):
				temp_arg = None
				if DProps[i] == 0:
					coeffs[i][j] == 0 
					continue

				if type(DProps[i].args[0]) is Integer:

					#print(DProps[i].args)
					if len(DProps[i].args) > 2:
						temp_arg = DProps[i].args[0]
						for a in range(len(DProps[i].args)):
							temp_arg = temp_arg*DProps[i].args[a]
						temp_arg = temp_arg/DProps[i].args[0]
						#print(temp_arg,"    temp_arg")
						#print(type(DProps[i].args))

					if temp_arg is not None:
						if type(temp_arg/Squares[j]) is Integer:
							coeffs[i][j] = temp_arg/Squares[j]
						else:
							coeffs[i][j] = 0
						del temp_arg
						continue

					if type(DProps[i].args[1]/Squares[j]) is One:

						coeffs[i][j]=(DProps[i].args[0])
					else:
						coeffs[i][j] = 0
			
				else:
					for k in range(len(DProps[i].args)):
						if type(DProps[i].args[k]/Squares[j]) is Integer:
							coeffs[i][j] = (DProps[i].args[k]/Squares[j])
							#print(DProps[i].args[k])
							#print(Squares[j])
							#print(DProps[i].args[k]/Squares[j])
		#print(coeffs,"        coeffs")
		
		# Some cleaning up storing thigns in the coeffs list
		for i in range(len(DProps)):
			#print(DProps[i],"     dprops")
			#print(transpose(Matrix(coeffs[i])).dot(Matrix(Squares)),"      dot stuff")
			#print(DProps[i] - transpose(Matrix(coeffs[i])).dot(Matrix(Squares)),"     difference")
			coeffs[i].append(DProps[i] - transpose(Matrix(coeffs[i])).dot(Matrix(Squares)))


		#print(coeffs,"         coeffs")
		# More math stuff storing things in temp list
		for i in range(len(coeffs)):
			temp[i] = transpose(Matrix(coeffs[i]))*External_Matrix
			#print(External_Matrix)
			#print(coeffs[i],"      coeffs")
			#print(temp[i],"        temp")
		output = []
		#Creating the IBP output. Ladders is an object which represents creation and annihilation operators. The first arguement is which propagator 
		# it will effect and the second is if it is creation ('+') or annihilation ('-'). indicies is just the "a" term from the propagators. 
		
		for i in range(len(temp)):
			for j in range(len(temp[i])):
				if j < (len(temp[i])-1):
					#output[i].append([temp[i][j],ladders(j + 1,'-'),ladders(i + 1,'+'),indicies(i + 1)])
					output.append([temp[i][j],ladders(j + 1,'-'),ladders(i + 1,'+'),Symbol("a"+str(i+1))])
				else:
					#output[i].append([temp[i][j],1,ladders(i + 1,'+'),indicies(i + 1)])
					output.append([temp[i][j],1,ladders(i + 1,'+'),Symbol("a"+str(i+1))])

		output.append([diff(self.x,self.y)*Symbol('d')])


		return output



	def math_output(self,ini_output):
		fin_output = 0
		op_count = 0
		zero_count = 0
		sym_bro = []
		IBP_OPS = []

		#print(ini_output,"        ini_output")

		for i in range(len(ini_output) - 1):
			if ini_output[i][0] != 0 and len(ini_output[i]) != 1:
				if ini_output[i][1] != 1:
					
					sym_bro.append(ini_output[i][1])
					op_count += 1
				if ini_output[i][2] != 1:
					
					sym_bro.append(ini_output[i][2])
					op_count += 1
			elif ini_output[i][0] == 0:
				zero_count += 1

		sym = symbols("I:"+str(op_count))
		x = 0
		for i in range(len(ini_output) - 1):
			if ini_output[i][0] != 0 and len(ini_output[i]) != 1:
				if ini_output[i][1] != 1:
					ini_output[i][1] = sym[x]
					x += 1
				if ini_output[i][2] != 1:
					ini_output[i][2] = sym[x]
					x += 1 

		
		for i in range(len(ini_output) - 1):
			if ini_output[i][0] != 0:
				

				if ini_output[i][1] != 1 or ini_output[i][2] != 1:



					for j in range(len(sym)):
						if sym[j] == ini_output[i][1]:
							op_1 = j
						if sym[j] == ini_output[i][2]:
							op_2 = j
						if sym[j] != ini_output[i][1] and ini_output[i][1] == 1:
							op_1 = -1

						if sym[j] != ini_output[i][2] and ini_output[i][2] == 1:
							op_1 = -1

					if sym_bro[op_1] == 1 or sym_bro[op_2] == 1:
						continue
					if op_1 == -1 or op_2 == -1:
						continue


					if sym_bro[op_1].get_index() == sym_bro[op_2].get_index():

						if sym_bro[op_1].get_op() != sym_bro[op_2].get_op():
						
							ini_output[i][1] = 1
							ini_output[i][2] = 1
							
							del op_1
							del op_2 
					else:
						del op_1
						del op_2 
						


		for i in range(len(ini_output)-1):
			if ini_output[i][0] != 0:
				fin_output = fin_output + ini_output[i][0]*ini_output[i][1]*ini_output[i][2]*ini_output[i][3]
		fin_output = fin_output - ini_output[len(ini_output) - 1][0]
		fin_output = fin_output * -1


		print("========================================================================================================")
		IBP_OPS.append(fin_output)
		IBP_OPS.append(sym_bro)
		return IBP_OPS


	def read_IBP(self):
		return self.IBP_String
	def get_output(self):
		return self.output
	def get_math_output(self):
		return self.math_output

#x = Symbol('p')
#y = Symbol('k')
#IBP = IBP(x,y)
#print(IBP.get_math_output())