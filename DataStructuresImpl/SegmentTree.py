class SegmentTree:
	def __init__(self,val, L, R, left=None, right=None):
		self.val = val
		self.L = L 
		self.R = R 
		self.left = left
		self.right = right

	@staticmethod
	def build(L, R, arr):
		if L == R:
			return SegmentTree(arr[L],L,R, None, None)
		else:
			M = (L + R) // 2
			left = SegmentTree.build(L, M, arr)
			right = SegmentTree.build(M+1, R, arr)
			val = left.val + right.val
			return SegmentTree(val, L, R, left, right)

	def update(self, val, index):
		if L == R: 
			self.val = val
		else:
			M = (self.L + self.R) // 2
			#L - M - Left
			#R - (M + 1) - Right
			if index <= M:
				self.left.update(val,index)
			else:
				self.right.update(val,index)

	def queryRange(self,L,R):
		if L > R:
			return 0
		elif L == self.L and R == self.R:
			return self.val
		else:
			M = (self.L + self.R) // 2
			leftVal = self.left.queryRange(L,M) if self.left else 0
			rightVal = self.right.queryRange(M+1,R) if self.right else 0
			return leftVal + rightVal


#Expected Segment Tree for [1,3,5,2,1]
#Each Node: (L,R,Val)

# 			 (0,4,12)
#			/		 \
# 		(0,2,9) 	 (3,4,3)
#		/	  \		  /	  \
# 	 (0,1,4) (2,2,5) (3,3,2) (4,4,1)
#	   /  \
# (0,0,1) (1,1,3)
#

arr = [1,3,5,2,1]
head = SegmentTree.build(0,4, arr)
assert head.queryRange(0,4) == 12, "Incorrect Query Range: answer is 11"
assert head.queryRange(0,3) == 11, "Incorrect Query Range: answer is 12"
assert head.queryRange(2,2) == 5, "Incorrect Query Range: answer is 5"
assert head.queryRange(3,4) == 3, "Incorrect Query Range: answer is 3"
