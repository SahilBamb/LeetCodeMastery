import random, time

def insertionSort(arr):
	if len(arr)<2:
		return arr
	for i in range(1,len(arr)):
		k = i - 1
		for j in range(i,0,-1):
			if arr[k] > arr[j]:
				arr[k],arr[j] = arr[j],arr[k]
				k -= 1
			else:
				break
	return arr


def mergeSort(arr,L=0,R=None):
	def merge(arr,L,R,M):
		sep = [None for _ in range(R-L+1)]
		p1 = L
		p2 = M+1
		p3 = 0
		while (p1<M+1 or p2<R+1):
			if p1>=M+1:
				val = arr[p2]
				p2+=1
			elif p2>=R+1:
				val = arr[p1]
				p1+=1
			elif arr[p1] < arr[p2]:
				val = arr[p1]
				p1+=1
			else:
				val = arr[p2]
				p2+=1

			sep[p3] = val
			p3+=1
		for i in range(L,R+1):
			arr[i] = sep[i-L]
		return 

	if len(arr)<2:
		return arr
	if R is None:
		R = len(arr)-1
	if L == R:
		return
	M = (R+L)//2
	mergeSort(arr,L,M)
	mergeSort(arr,M+1,R)
	merge(arr,L,R,M)
	return arr


#start with pivot
#put values less than to left
#put values greater than to right
def quickSort(arr,L=0,R=None):
	if len(arr)<2:
		return arr
	if R is None:
		R = len(arr)-1
	if (R-L+1)<=1:
		return 

	pivot = arr[R]
	p1 = L
	for i in range(L,R):
		if arr[i] < pivot:
			arr[p1],arr[i] = arr[i],arr[p1]
			p1+=1
	arr[p1],arr[R] = arr[R],arr[p1]

	quickSort(arr,L,p1-1)
	quickSort(arr,p1+1,R)
	return arr

def bucketSort(arr,minVal=0,maxVal=None):
	if len(arr) < 2:
		return arr
	if maxVal is None:
		maxVal = max(arr)

	temp = [0 for bucket in range(maxVal+1)]
	for num in arr:
		temp[num] += 1

	sortedArr = []
	for num in range(len(temp)):
		while (temp[num]):
			temp[num] -= 1
			sortedArr.append(num)
	return sortedArr

iterations = 100
listLength = 999

sorts = {'Insertion': insertionSort, 
		 'Merge': mergeSort, 
		 'Quick': quickSort,
		 'Bucket': bucketSort}

for name,specificSort in sorts.items():
	execution_time = 0
	for x in range(iterations):
		arr = [random.randint(0,999) for _ in range(random.randint(0,listLength))]
		sortedArray = sorted(arr)
		start_time = time.time()
		sortedByAlgo = specificSort(arr)
		end_time = time.time()
		execution_time += (end_time - start_time)
		assert  sortedArray == sortedByAlgo, "Incorrect found: \n" + str(sorted(arr)) +  ' !=\n' + str(specificSort(arr))
	pad = (15 - len(name)) * ' '
	print(f'{name} Sort took: {pad} {execution_time/iterations} seconds')
