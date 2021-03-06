#    Author: Matthew Schiavi
#	 Last Edit: 07-12-16
#
#	Based off of the Internal, External, and propagators which are inputed in the input file this generates the matrix to produce
#	IBPS
#
#
#




from math import *
from sympy import *
from InputReader import *
import sys

One = type(Abs(1)/Abs(1))
NegativeOne = type(-1*(Abs(1)/Abs(1)))
class Initialization(object):
	
	
	
	#creaters reader object from InputReader which reads input file
	#for internal external and props given in sympy objects
	try:
		inFile = sys.argv[1]
		Input = open(inFile)
		Contents = Input.read()
		print(Contents)
		Input.close()

	except IndexError:
		inFile = "input.DAT"

	_Reader = Reader(inFile)
	inputs = _Reader.Input_filereader()

	Internal = inputs[0]
	External = inputs[1]
	Propagators = inputs[2]
	def __init__(self):
		super(Initialization, self).__init__()
		#print(self.Propagators,"            Props")


	def get_props(self):
		return self.Propagators
	def get_internal(self):
		return self.Internal
	def get_external(self):
		return self.External

	#find_squares is a method in the Initialization object which takes the inputed internal,external
	#and propagators and then finds the values at which are power of 2 or higher energies.
	#For example k**2 is a square or k*p is a square. Things that appear in terms such as
	#(k+p)**2 	
	def find_squares(self):
		Squares = []
		#First double loop loops over the internal momenta and then the propagators.
		#Stores the derivative of each prop with respect to internal in the temp array
		#The coef of those are then stored in coef array
		for i in range(len(self.Internal)):
			temp = []
			coef = []
			for j in range(len(self.Propagators)):
				temp.append(poly(diff(self.Propagators[j],self.Internal[i],1),self.Internal[i]))
				coef.append(poly(temp[j],self.Internal[i]).coeffs())
		#This loop loops over the same things as before but then gets rid of any terms of 
		#degree 0. it then takes the coeffs of the first term and divides the derivative
		# term by that term which is then stored in temp
		#for x in range(len(self.Internal)):
			for y in range(len(temp)):
			#	print(temp[y].args[0])
				if temp[y].args[0] == 0:
					continue
				else:
					#print(temp[y],"   temp y")
					#print(self.Internal[i])
					new_temp = small_O_n(temp[y],1)
			#		print(temp,"    TEMP")
			#		print(new_temp,"      NEW TEMP")
					if new_temp.coeffs()[0] != 0:
						temp[y] = temp[y]/new_temp.coeffs()[0]
			#		print(temp,"     temp after division")
			#print(temp, "       FInal temp")
			for z in range(len(temp)):
				temp[z] = (temp[z] * self.Internal[i]).expand()
				for x in range(len(temp[z].args)):
					if type(temp[z].args[x]) is Integer:
						break	
					elif temp[z].args[x] is self.Internal[i]:
						break
					elif Abs(temp[z].args[x]) not in Squares:
						if temp[z].args[x] == 0:
							continue
						else:
							Squares.append(Abs(temp[z].args[x]).args[0])
			del temp
			del new_temp
			del coef
			Squares = list(set(Squares))
			#print(Squares, "      Squares")
		return Squares
	#This method will eventualy return the Matrix which contains the coefficients
	# of the squares in the expanded propagators, the external squared momenta,
	# and a row on bottom of just 0's if not col for external and 1 otherwise
	def External_Matrix(self):
		Squares = Matrix(self.find_squares())
		#print(Squares, "     Squares")
		Singleton=[]
		temp = [[0 for x in range(len(Squares))]for y in range(len(self.Propagators))]



		for i in range(len(self.Propagators)):

			#print(self.Propagators[i].expand().args,"             Propagators")
			#print(type(self.Propagators[i].expand().args[0]))
			#This looks for any singleton props like k**2 and loops over the different args of the props to indentify which is a good square or not
			# external momenta squares are bad squares. 
			for j in range(len(self.Propagators[i].expand().args)):
				for y in range(len(self.Internal)):
					if self.Propagators[i].expand().args[j] == self.Internal[y] or type(self.Propagators[i].expand().args[j]) == Integer or type(self.Propagators[i].expand().args[j]) == NegativeOne:
						Singleton.append([True,i])
						#print("true")
					else:
						Singleton.append([False,i])
				#This loop fills the matrix rows are the propagators in order of the input file and col is squares in order of the Squares list
				for k in range(len(Squares)):

					#print(self.Propagators[i].expand().args[j],Squares[k],i,k,self.Propagators[i].expand().args[j]/Squares[k],type(self.Propagators[i].expand().args[j]/Squares[k]))


				
						

					if type(self.Propagators[i].expand().args[j]/Squares[k]) is One or type(self.Propagators[i].expand().args[j]/Squares[k]) is Integer or type(self.Propagators[i].expand().args[j]/Squares[k]) is NegativeOne:
							#print(i,k)
							temp[i][k] = (self.Propagators[i].expand().args[j]/Squares[k]) 
							#print("added",self.Propagators[i].expand().args[j]/Squares[k])
		

			for x in range(len(Singleton)):
				if Singleton[x][0] == True:
					for i in range(len(Squares)):
						if Squares[i] == self.Propagators[Singleton[x][1]]:
							#print("hi")
							temp[Singleton[x][1]][i] = 1
						elif -1*Squares[i] == self.Propagators[Singleton[x][1]]:
							temp[Singleton[x][1]][i] = -1
						else:
							temp[Singleton[x][1]][i] = 0

		#print(temp,"       Temp")


		TSquares = Matrix(temp)*Squares
		#print(TSquares,"        TSquares")
		#print(Matrix(self.Propagators),"      Props")
		External_Vec = Matrix(self.Propagators) - TSquares
		for i in range(len(External_Vec)):
			External_Vec[i] = External_Vec[i].expand()
		#print(External_Vec,"             External_Vec after diff with props - temp")

		# insert after the last column
		Final_Mat = Matrix(temp).col_insert(Matrix(temp).shape[1],External_Vec)
		#print(Final_Mat,"           Final_Mat")
		bot_row = [0 for x in range(len(temp)+1)]
		#print(bot_row,"             bot_row")
		for i in range(Matrix(temp).shape[1] + 1):
			if i < Matrix(temp).shape[0]:
				bot_row[i] = 0
			else:
				bot_row[i] = 1
		Final_Mat = Final_Mat.row_insert(Final_Mat.shape[0],Matrix([bot_row]))

		#print(Final_Mat,"            Final_Mat")

		Final_Mat_Inv = Final_Mat**-1

		print(Final_Mat_Inv,"Final_Mat_Inv ")

		return Final_Mat_Inv

def union(a, b):
	return list(set(a) | set(b))

def small_O_n(p,n):	
	var = p.gen
	temp = p
	for i in range(len(p.terms())):
		if p.terms()[i][0][0] < n:
			temp = temp - poly(p.coeffs()[i]*var**p.terms()[i][0][0],var)
	return temp

def get_inFile(self):
	return self.inFile