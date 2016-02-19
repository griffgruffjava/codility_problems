
def cyclic_shift(A, K):
	shift = len(A) % K
	new_array = []
	counter = 0 
	for i in A:
		next = A[((len(A) - shift - 1) + counter)  % len(A)]
		counter	= counter + 1
		new_array.append(next)
	print new_array
	 
A = [3, 8, 9, 7, 6] 
K = 3
print len(A)
print cyclic_shift(A,K)





