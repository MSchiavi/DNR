#    Author: Matthew Schiavi
#	 Last Edit: 07-19-16
#
#	Takes an IBP and converts it to a readable string i.e. the I operators are turned into Y(index,op)
#	Some things may be missing in the string. I have found the things that are missing are irrelevent for what this is doing. 
#
#
#
from IBP import IBP
from initialization import *
import time
from sympy import Symbol
start_time = time.time()


_start = Initialization()



#Example of IBP output
# -I2*I3*a2 + I4*a2*q**2 - a2
def Read_IBP(IBP):
	print("                             ")
	print("===========================Starting readable output=====================================")
	print(IBP[0],"              Actual IBP")
	print(IBP[0].args)
	print(IBP[0].args[0].args)
	op_found = False
	op_pos = -5
	sym = symbols("I:"+str(len(IBP[1])))
	ibp_str = ""
	temp = ""

	for i in range(len(IBP[0].args)):

		for j in range(len(IBP[0].args[i].args)):

			for k in range(len(IBP[1])):

				if IBP[0].args[i].args[j] == sym[k]:

					op_found = True
					op_pos = k 
			if op_found == True and op_pos != -5:
				temp = temp + "Y(" + str(IBP[1][op_pos].get_index()) + "," + str(IBP[1][op_pos].get_op()) + ")"
				op_found = False
				op_pos = -5

			temp = temp + str(IBP[0].args[i].args[j])
		ibp_str = ibp_str + " + " + temp
		temp = ""

				


	ibp_str = ibp_str.replace("+ -1","- ")
	ibp_str = ibp_str.replace("0","")
	for i in range(len(IBP[1])):
		ibp_str = ibp_str.replace("I"+str(i),"")
	return ibp_str









Internal = _start.get_internal()
External = _start.get_external()

#print(Internal)
#print(External)

for i in range(len(External)):
	for j in range(len(Internal)):
		_IBP = IBP(External[i],Internal[j])
		print(External[i],Internal[j])
		print(_IBP.get_math_output())
		print(Read_IBP(_IBP.get_math_output()))
		del _IBP

for i in range(len(Internal)):
	for j in range(len(Internal)):
		_IBP = IBP(Internal[i],Internal[j])
		print(Internal[i],Internal[j])
		print(_IBP.get_math_output())
		print(Read_IBP(_IBP.get_math_output()))
		del _IBP
print("Run time:",'%.3f'%(time.time()-start_time) )

























