#    Author: Matthew Schiavi
#	 Last Edit: 07-12-16
#
#	Generates IBP relationships based off of Internal, External, and Propagators which are defined in the input file.
#
#
#
#
from IBP import IBP
from initialization import *
import time
from sympy import Symbol
start_time = time.time()


_start = Initialization()
Internal = _start.get_internal()
External = _start.get_external()

print(Internal)
print(External)

for i in range(len(External)):
	for j in range(len(Internal)):
		_IBP = IBP(External[i],Internal[j])
		print(External[i],Internal[j])
		print(_IBP.get_math_output())

		print(_IBP.get_math_output()[1][2].get_index())
		print(_IBP.get_math_output()[1][2].get_op())

		print(_IBP.get_math_output()[1][3].get_index())
		print(_IBP.get_math_output()[1][3].get_op())

		print(_IBP.get_math_output()[1][4].get_index())
		print(_IBP.get_math_output()[1][4].get_op())

		#print(_IBP.get_math_output()[1][3].get_index())
		#print(_IBP.get_math_output()[1][3].get_op())

		#print(_IBP.get_math_output()[1][4].get_index())
		#print(_IBP.get_math_output()[1][4].get_op())

		#print(_IBP.get_math_output()[1][5].get_index())
		#print(_IBP.get_math_output()[1][5].get_op())

		#print(_IBP.get_math_output()[1][6].get_index())
		#print(_IBP.get_math_output()[1][6].get_op())

		#print(_IBP.get_math_output()[1][9].get_index())
		#print(_IBP.get_math_output()[1][9].get_op())

		#print(_IBP.get_math_output()[1][10].get_index())
		#print(_IBP.get_math_output()[1][10].get_op())

		#print(_IBP.get_math_output()[1][11].get_index())
		#print(_IBP.get_math_output()[1][11].get_op())
		del _IBP

for i in range(len(Internal)):
	for j in range(len(Internal)):
		_IBP = IBP(Internal[i],Internal[j])
		print(Internal[i],Internal[j])
		print(_IBP.get_math_output())

		print(_IBP.get_math_output()[1][2].get_index())
		print(_IBP.get_math_output()[1][2].get_op())

		print(_IBP.get_math_output()[1][3].get_index())
		print(_IBP.get_math_output()[1][3].get_op())

		print(_IBP.get_math_output()[1][4].get_index())
		print(_IBP.get_math_output()[1][4].get_op())

		print(_IBP.get_math_output()[1][7].get_index())
		print(_IBP.get_math_output()[1][7].get_op())

		print(_IBP.get_math_output()[1][8].get_index())
		print(_IBP.get_math_output()[1][8].get_op())

		print(_IBP.get_math_output()[1][9].get_index())
		print(_IBP.get_math_output()[1][9].get_op())

		#print(_IBP.get_math_output()[1][12].get_index())
		#print(_IBP.get_math_output()[1][12].get_op())

		#print(_IBP.get_math_output()[1][13].get_index())
		#print(_IBP.get_math_output()[1][13].get_op())

		#print(_IBP.get_math_output()[1][16].get_index())
		#print(_IBP.get_math_output()[1][16].get_op())

		#print(_IBP.get_math_output()[1][17].get_index())
		#print(_IBP.get_math_output()[1][17].get_op())
		
		del _IBP









print("Run time:",'%.3f'%(time.time()-start_time) )

