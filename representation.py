class ladders(object):

	def __init__(self,index,op):
		super(ladders, self).__init__()
		self.index = index
		self.op = op


	def get_index(self):
		return self.index

	def get_op(self):
		return self.op

class indicies(object):
	def __init__(self,index):
		super(indicies,self).__init__()
		self.index = index
	
	def get_index(self):
		return self.index