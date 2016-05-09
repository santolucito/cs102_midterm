l = [4,3,7,9,5]
def sort(x):
	for i in range (0,len(x)) :
		minimum = i
		for j in range(i,len(x) ):
			if x[j] < x[minimum]:
				minimum = j
		tmp = x[i]
		x[i] = x[minimum]
		x[minimum] = tmp
		print (x)
		#swap minimum with first unsorted position
	return x

print (sort(l))
