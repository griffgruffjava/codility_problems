
def cyclic_shift(A, K):
	shift = len(A) % K
	new_array = []
	counter = 0
	for i in A:
		temp = A[(shift+counter)%shift]
		counter	= counter + 1
		new_array.append(temp)
	print new_array
	 
A = [3, 8, 9, 7, 6] 
K = 3
print len(A)
print cyclic_shift(A,K)





