import arma_mod as a


pls =[1,2,3,0,5,0,3]
plss=[7,8,9,0,0,12,4]
row3=[0,1,1,10,1,1,21]
row4 = [2,0,2,0,2,2,34]
row5 = [3,3,3,0,3,3,32]
row6 = [4,0,4,0,4,4,34]
col = [5,5,5,5,5,5]





#Mat = [[2,-4,5,-2,2,-3,-2,2,-3],
#		[4,-1,0,2,-4,5,-2,2,-3],
#		[-2,2,-3,2,-4,5,-2,2,-3],
#		[-8,3,-11,-2,2,-3,32,91,304],
#		[5,32,55,67,824,451,1000,4,-32],
#		[-931,78,98,21,32,45,888,-99,-54],
#		[7,-32,67,99,98,103,43,54,88],
#		[-32,-4,-9,10,133,43,88,103,32]]

#print(a.ltv(pls,len(pls)))

obj1 = a.Potato(pls,len(pls))
obj1.start()
obj1.addrow(plss,len(plss))
obj1.addrow(row3,len(row3))
obj1.addrow(row4,len(row4))
obj1.addrow(row5,len(row5))
obj1.addrow(row6,len(row6))
#obj1.addcol(col,len(col))
obj1.set_solution(col,len(col))
obj1.row_reduc()