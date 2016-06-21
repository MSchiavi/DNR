from math import *
from sympy import *
from InputReader import *

One = type(Abs(1)/Abs(1))
class Initialization(object):
	#creaters reader object from InputReader which reads input file
	#for internal external and props given in sympy objects
	_Reader = Reader("input.DAT")
	#,_Reader = Reader("working.DAT")
	inputs = _Reader.Input_filereader()
	print("************************************************************************")
	print(inputs,"       Inputed parameters")
	print("************************************************************************")
	Internal = inputs[0]
	Externla = inputs[1]
	Propagators = inputs[2]
	def __init__(self):
		super(Initialization, self).__init__()
		#print(self.Propagators)
	#find_squares is a method in the Initialization object which takes the inputed internal,external
	#and propagators and then finds the values at which are power of 2 or higher energies.
	#For example k**2 is a square or k*p is a square. Things that appear in terms such as
	#(k+p)**2 	
	def find_squares(self):
		temp = []
		coef = []
		Squares = []
		#First double loop loops over the internal momenta and then the propagators.
		#Stores the derivative of each prop with respect to internal in the temp array
		#The coef of those are then stored in coef array
		for i in range(len(self.Internal)):
			for j in range(len(self.Propagators)):
				temp.append(poly(diff(self.Propagators[j],self.Internal[i],1),self.Internal[i]))
				coef.append(poly(temp[j],self.Internal[i]).coeffs())
				coef[i]
		#This loop loops over the same things as before but then gets rid of any terms of 
		#degree 0. it then takes the coeffs of the first term and divides the derivative
		# term by that term which is then stored in temp
		for x in range(len(self.Internal)):
			for y in range(len(temp)):
				print(temp[y].args[0])
				if temp[y].args[0] == 0:
					print("hi")
					continue
				else:
					new_temp = small_O_n(temp[y],1)
					print(temp)
					print(new_temp)
					if new_temp.coeffs()[0] != 0:
						temp[y] = temp[y]/new_temp.coeffs()[0]
				for z in range(len(temp)):
					temp[z] = (temp[z] * self.Internal[x]).expand()
					for i in range(len(temp[z].args)):
						if type(temp[z].args[i]) is Integer:
							break	
						elif temp[z].args[i] is self.Internal[x]:
							break
						elif Abs(temp[z].args[i]) not in Squares:
							Squares.append(Abs(temp[z].args[i]).args[0])
			Squares = list(set(Squares))
		return Squares
	#This method will eventualy return the Matrix which contains the coefficients
	# of the squares in the expanded propagators, the external squared momenta,
	# and a row on bottom of just 0's if not col for external and 1 otherwise
	def External_Matrix(self):
		Squares = Matrix(self.find_squares())
		#print(Squares)

		temp = [[0 for x in range(len(Squares))]for y in range(len(self.Propagators))]


		for i in range(len(self.Propagators)):

			#print(self.Propagators[i].expand().args,"Propagators")

			for j in range(len(self.Propagators[i].expand().args)):
				for y in range(len(self.Internal)):
					if self.Propagators[i].expand().args[j] == self.Internal[y] or type(self.Propagators[i].expand().args[j]) == Integer:
						Singleton = [True,i]
				for k in range(len(Squares)):

					#print(self.Propagators[i].expand().args[j],Squares[k],i,k,self.Propagators[i].expand().args[j]/Squares[k])

					if type(self.Propagators[i].expand().args[j]/Squares[k]) is One or type(self.Propagators[i].expand().args[j]/Squares[k]) is Integer:
						#print("added",self.Propagators[i].expand().args[j]/Squares[k])
						temp[i][k] = (self.Propagators[i].expand().args[j]/Squares[k])
						
		if Singleton[0] == True:
			for i in range(len(Squares)):
				if Squares[i] == self.Propagators[Singleton[1]]:
					temp[Singleton[1]][i] = 1
				else:
					temp[Singleton[1]][i] = 0

		#print(temp,"Temp")

		TSquares = Matrix(temp)*Squares
		#print(TSquares,"TSquares is temp after dot with squares")

		External_Vec = Matrix(self.Propagators) - TSquares
		for i in range(len(External_Vec)):
			External_Vec[i] = External_Vec[i].expand()
		#print(External_Vec,"External_Vec after diff with props - temp")


		Final_Mat = Matrix(temp).col_insert(3,External_Vec)
		bot_row = [0 for x in range(len(temp)+1)]
		#print(bot_row)
		for i in range(len(temp)+1):
			if i < len(temp):
				bot_row[i] = 0
			else:
				bot_row[i] = 1
		Final_Mat = Final_Mat.row_insert(3,Matrix([bot_row]))

		#print(Final_Mat,"Final_Mat")

		Final_Mat_Inv = Final_Mat**-1

		#print(Final_Mat_Inv,"Final_Mat_Inv ")

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



Initialize = Initialization()
print(Initialize.External_Matrix())