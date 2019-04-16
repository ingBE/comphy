import random

listname=[] # Creating empty list

for i in range(1,101):
	listname.append( random.randint( 0, 100 ) ) #a Adding elements to a list

# quick sort function
def quick_sorted(arr):
	if len(arr) > 1:
		pivot = arr[len(arr)-1]
		left, mid, right = [], [], []
		for i in range(len(arr)-1):
			if arr[i] < pivot:
				left.append(arr[i])
			elif arr[i] > pivot:
				right.append(arr[i])
			else:
				mid.append(arr[i])
		mid.append(pivot)
		return quick_sorted(left) + mid + quick_sorted(right)
	else:
		return arr

print(listname)
print('\n')
print(quick_sorted(listname))
