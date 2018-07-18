
'''
this is comment section
'''
class DynamicArray(object):
	"""docstring for DynamicArray"""
	def __init__(self):
		super(DynamicArray, self).__init__()
		self.len = 0;
		self.capacity = 16;
		self.arr = range(self.capacity)

	def __str__(self):
		if self.len == 0:
			return "[]"
		else:
			s = "["
			for i in range(0, self.len-1):
				s = s + str(self.arr[i]) + ", "
			s = s + str(self.arr[self.len]) + "]"
			return s

	def add(self, obj):
		print("len %d and capcity %d" %(self.len, self.capacity))
		if(self.len+1 >= self.capacity):
			self.capacity = self.capacity*2
			print("capacity : %d" %(self.capacity))
			newarr = range(self.capacity)
			for x in xrange(0,self.len-1):
				print("adding the %d " %(self.arr[x]))
				newarr[x] = self.arr[x]
			self.arr = newarr
		self.len = self.len + 1
		self.arr[self.len] = obj

	def removeAt(self, index):
		if(index >= self.len | index < 0):
			print("array index out of bounds")
		else:
			data = self.arr[index]
			newarr = range(self.len-1)
			j =0
			for x in xrange(0, self.len):
				if(x == index):
					j = x -1
					#self.len = self.len-1

				else:
					newarr[j] = self.arr[x]
					j = j+1

			self.arr = newarr
			self.len = j


	def indexOf(self, obj):
		for x in xrange(0, self.len):
			if self.arr[x] == obj:
				return x
		return -1

	def size(self):
		return self.len


	
d = DynamicArray()
for x in xrange(10,20):
	d.add(x)
print(d)
d.removeAt(3)	
print(d)
		