#helper swap function
def _swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]

#each algorithm should yield whenever it wants a frame to be rendered,
#and it should yield a list of indices to highlight

def quicksort(arr):
	return

def _merge(arr, start, mid, end):
	start2 = mid + 1
	if arr[mid] <= arr[start2]:
		return
	while start <= mid and start2 <= end:
		if arr[start] <= arr[start2]:
			start += 1
		else:
			value = arr[start2]
			index = start2
			while(index != start):
				arr[index] = arr[index - 1]
				index -= 1
			arr[start] = value
			start += 1
			mid += 1
			start2 += 1

def _mergesort_helper(arr, l, r):
	if l < r:
		m = l + (r - l) // 2
		yield from _mergesort_helper(arr, l, m)
		yield from _mergesort_helper(arr, m+1, r)
		_merge(arr, l, m, r)
		yield []

def mergesort(arr):
	yield []
	yield from _mergesort_helper(arr, 0, len(arr)-1)

def selection_nohighlight(arr):
	m = None
	m_i = None
	for i in range(len(arr)):
		m_i, m = min(enumerate(arr[i:],start=i), key = lambda en: en[1])
		_swap(arr,i,m_i)
		yield []

def selection(arr):
	for i in range(len(arr)-1,-1,-1):
		m = -1
		m_i = -1
		swap_needed = False
		for j in range(i+1):
			if arr[j] > m:
				m_i = j
				m = arr[j]
				swap_needed = True
			yield [j]
		if swap_needed:
			_swap(arr,i,m_i)
			yield[]

def bubble(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-1):
			if arr[j] > arr[j+1]:
				_swap(arr, j, j+1)
				yield [j,j+1]