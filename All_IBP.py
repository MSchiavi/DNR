#    Author: Matthew Schiavi
#	 Last Edit: 07-19-16
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

_IBP=IBP()

for i in range(len(External)):
	for j in range(len(Internal)):
		print(_IBP.Get_IBP(External[i],Internal[j]))
		print(External[i],Internal[j])
		
		#print(_IBP.get_math_output()[1][0].get_index())
		#print(_IBP.get_math_output()[1][0].get_op())

		#print(_IBP.get_math_output()[1][1].get_index())
		#print(_IBP.get_math_output()[1][1].get_op())

		#print(_IBP.get_math_output()[1][4].get_index())
		#print(_IBP.get_math_output()[1][4].get_op())

		#print(_IBP.get_math_output()[1][5].get_index())
		#print(_IBP.get_math_output()[1][5].get_op())

		#print(_IBP.get_math_output()[1][6].get_index())
		#print(_IBP.get_math_output()[1][6].get_op())

		#print(_IBP.get_math_output()[1][7].get_index())
		#print(_IBP.get_math_output()[1][7].get_op())

		#print(_IBP.get_math_output()[1][8].get_index())
		#print(_IBP.get_math_output()[1][8].get_op())

		#print(_IBP.get_math_output()[1][9].get_index())
		#print(_IBP.get_math_output()[1][9].get_op())

		#print(_IBP.get_math_output()[1][10].get_index())
		#print(_IBP.get_math_output()[1][10].get_op())

		#print(_IBP.get_math_output()[1][11].get_index())
		#print(_IBP.get_math_output()[1][11].get_op())

		#print(_IBP.get_math_output()[1][12].get_index())
		#print(_IBP.get_math_output()[1][12].get_op())

		#print(_IBP.get_math_output()[1][13].get_index())
		#print(_IBP.get_math_output()[1][13].get_op())

		#print(_IBP.get_math_output()[1][14].get_index())
		#print(_IBP.get_math_output()[1][14].get_op())

		#print(_IBP.get_math_output()[1][15].get_index())
		#print(_IBP.get_math_output()[1][15].get_op())

		#print(_IBP.get_math_output()[1][18].get_index())
		#print(_IBP.get_math_output()[1][18].get_op())

		#print(_IBP.get_math_output()[1][19].get_index())
		#print(_IBP.get_math_output()[1][19].get_op())

		#print(_IBP.get_math_output()[1][20].get_index())
		#print(_IBP.get_math_output()[1][20].get_op())

		#print(_IBP.get_math_output()[1][21].get_index())
		#print(_IBP.get_math_output()[1][21].get_op())

		#print(_IBP.get_math_output()[1][22].get_index())
		#print(_IBP.get_math_output()[1][22].get_op())

		#print(_IBP.get_math_output()[1][23].get_index())
		#print(_IBP.get_math_output()[1][23].get_op())

		#print(_IBP.get_math_output()[1][24].get_index())
		#print(_IBP.get_math_output()[1][24].get_op())

		#print(_IBP.get_math_output()[1][25].get_index())
		#print(_IBP.get_math_output()[1][25].get_op())


for i in range(len(Internal)):
	for j in range(len(Internal)):
		print(_IBP.Get_IBP(External[i],Internal[j]))
		print(Internal[i],Internal[j])
		

		#print(_IBP.get_math_output()[1][2].get_index())
		#print(_IBP.get_math_output()[1][2].get_op())

		#print(_IBP.get_math_output()[1][3].get_index())
		#print(_IBP.get_math_output()[1][3].get_op())

		#print(_IBP.get_math_output()[1][4].get_index())
		#print(_IBP.get_math_output()[1][4].get_op())

		#print(_IBP.get_math_output()[1][7].get_index())
		#print(_IBP.get_math_output()[1][7].get_op())

		#print(_IBP.get_math_output()[1][8].get_index())
		#print(_IBP.get_math_output()[1][8].get_op())

		#print(_IBP.get_math_output()[1][9].get_index())
		#print(_IBP.get_math_output()[1][9].get_op())

		#print(_IBP.get_math_output()[1][12].get_index())
		#print(_IBP.get_math_output()[1][12].get_op())

		#print(_IBP.get_math_output()[1][13].get_index())
		#print(_IBP.get_math_output()[1][13].get_op())

		#print(_IBP.get_math_output()[1][16].get_index())
		#print(_IBP.get_math_output()[1][16].get_op())

		#print(_IBP.get_math_output()[1][17].get_index())
		#print(_IBP.get_math_output()[1][17].get_op())
		
		


#_IBP = IBP(Internal[1],Internal[0])
#print(Internal[1],Internal[0])
#print(_IBP.get_math_output())

#print(_IBP.get_math_output()[1][0].get_index())
#print(_IBP.get_math_output()[1][0].get_op())

#print(_IBP.get_math_output()[1][1].get_index())
#print(_IBP.get_math_output()[1][1].get_op())

#print(_IBP.get_math_output()[1][2].get_index())
#print(_IBP.get_math_output()[1][2].get_op())

#print(_IBP.get_math_output()[1][3].get_index())
#print(_IBP.get_math_output()[1][3].get_op())

#print(_IBP.get_math_output()[1][4].get_index())
#print(_IBP.get_math_output()[1][4].get_op())

#print(_IBP.get_math_output()[1][5].get_index())
#print(_IBP.get_math_output()[1][5].get_op())

#print(_IBP.get_math_output()[1][6].get_index())
#print(_IBP.get_math_output()[1][6].get_op())

#print(_IBP.get_math_output()[1][7].get_index())
#print(_IBP.get_math_output()[1][7].get_op())

#print(_IBP.get_math_output()[1][8].get_index())
#print(_IBP.get_math_output()[1][8].get_op())

#print(_IBP.get_math_output()[1][9].get_index())
#print(_IBP.get_math_output()[1][9].get_op())

#print(_IBP.get_math_output()[1][10].get_index())
#print(_IBP.get_math_output()[1][10].get_op())

#print(_IBP.get_math_output()[1][11].get_index())
#print(_IBP.get_math_output()[1][11].get_op())

#print(_IBP.get_math_output()[1][12].get_index())
#print(_IBP.get_math_output()[1][12].get_op())

#print(_IBP.get_math_output()[1][13].get_index())
#print(_IBP.get_math_output()[1][13].get_op())

#print(_IBP.get_math_output()[1][16].get_index())
#print(_IBP.get_math_output()[1][16].get_op())

#print(_IBP.get_math_output()[1][17].get_index())
#print(_IBP.get_math_output()[1][17].get_op())

#print(_IBP.get_math_output()[1][18].get_index())
#print(_IBP.get_math_output()[1][18].get_op())

#print(_IBP.get_math_output()[1][19].get_index())
#print(_IBP.get_math_output()[1][19].get_op())

#print(_IBP.get_math_output()[1][20].get_index())
#print(_IBP.get_math_output()[1][20].get_op())

#print(_IBP.get_math_output()[1][21].get_index())
#print(_IBP.get_math_output()[1][21].get_op())

#print(_IBP.get_math_output()[1][24].get_index())
#print(_IBP.get_math_output()[1][24].get_op())

#print(_IBP.get_math_output()[1][25].get_index())
#print(_IBP.get_math_output()[1][25].get_op())





print("Run time:",'%.3f'%(time.time()-start_time) )


