class minHeap:

	def __init__(self, array):
		self.array = array
		for i in range(len(array)-1,-1,-1):
			self.siftDown(i)
			
	def __str__(self):
		return str(self.array)

	def siftUp(self,i=None):
		if i == None:
			i = len(self.array)-1
		while (i):
			parent = (i-1)//2
			if self.array[i] < self.array[parent]:
				self.array[i],self.array[parent] = self.array[parent],self.array[i]
				i = parent
			else:
				break

	def siftDown(self,i=0):
		oldi = -1
		while (i != oldi and (i*2)+1 < len(self.array)):
			oldi = i
			for child in [(2*i)+1,(2*i)+2]:
				if child < len(self.array) and self.array[i] > self.array[child]:
					i = child
			self.array[i],self.array[oldi] = self.array[oldi],self.array[i]

	def insert(self,num):
		self.array.append(num)
		self.siftUp()

	def remove(self,):
		if len(self.array)>1: 
			self.array[0] = self.array[-1]
			self.array = self.array[:-1]
			self.siftDown()
		else:
			self.array.pop()
