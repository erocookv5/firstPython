import numpy as np 

# # Arrays and Matrices with Numpy:
# # Arrays are created by passing a list of m>=1 homogeneous elements.
# # If those elements are homogeneous lists of n>=1 length,
# # that will be a matrix having m rows and n columns. 
# a = np.array([[11,56, 31], [23, 79, 90]])
# print(len(a))
# print(a.shape) #matrix dimensions
# print(a.size) #cells in a matrix
# b = np.array([[11], [23]])
# print(len(b))
# print(b.shape) #matrix dimensions
# print(b.size) #cells in a matrix
# # reshape(x, y) creates a (x, y)dimensional matrix from another one of shape S, 
# # if you give consistent values to it. Otherwise, it returns a fatal error. 
# a = np.array([[11,56, 31], [23, 79, 90]]) # a.size = 6, a.shape = (2, 3)
# c = a.reshape(3, 2)
# print(c.size)
# print(c.shape)
# print(c)
# d = a.reshape(1, 6)
# print(d.size)
# print(d.shape)
# print(d)
# e = a.reshape(6, 1)
# print(e.size)
# print(e.shape)
# print(e)
# f = a.reshape(2, 4)
# print(f.size)
# print(f.shape)
# print(f)

# # How to transpose a matrix:
# a = np.array([[11,56, 31], [23, 79, 90]]) # a.size = 6, a.shape = (2, 3)
# print(a)
# h = a.transpose()
# print(h)
# # or equivalently:
# i = a.T
# print(i)
# # How to print a cell of a matrix:
# print(a[0,2]) # a[i,j], where i>=0 is the row index and j>=0 is the column index
# print(a[1,-1])
# # how to set the type for a matrix:
# a1 = np.array([[11,56, 31], [23, 79, 90]], float)
# print(a1)
# a2 = np.array([[11,56, 31], [23, 79, 90]], str)
# print(a2)
# # how to print only one or more rows of some matrices:
# print(a1[1], a2[0])

# # Zeros matrix, ones matrix, some value matrix:
# a = np.array([[11,56, 31], [23, 79, 90]]) # a.size = 6, a.shape = (2, 3)
# l = np.zeros((4,7)) # you pass your shape as a tuple
# print(l)
# l1 = np.zeros((4,7), int) # casting a type
# print(l1)
# m = np.ones((4,7)) # you pass your shape as a tuple
# print(l)
# m1 = np.ones((4,7), int) # casting a type
# print(m1)
# n = np.full((4, 7), 22) # size as a tuple, desired value
# print(n)
# n1 = np.full((4, 7), '22.5', float) # optional: casting a type 
# print(n1) # '22.5' is string, but n1 will contain only 22.5 
# p = np.random.random((4,7)) # a random matrix of shape (4,7), all the numbers are float and within [0, 1]
# print(p)
# p1 = np.random.randint(2,7,(4, 7)) # a random matrix of shape (4,7), all the numbers are int and within [2, 7]
# print(p1)

# # Indexing, an useful tool: 
# a = np.arange(0,120,4) # from start (0) to end (120), takes a number every step (5) and puts them in an array
# print(a, a.shape, a.size)
# b = a.reshape(10,3)
# print(b, b.shape, b.size)
# c = b[1:9:2] # from start row (1) to end row (9), takes a row every step (2), all columns (3 in total)
# print(c)
# d = a.reshape(3, 10)
# print(d)
# e = d[:, 1:8:3]  # from start column (1) to end column (8), takes a column every step (3), all rows (3 in total)
# print(e, e.shape, e.size)
# e1 = d[:, -1:-8:-3]  # from start column (-1) to end column (-8), takes a column every step (-3), all rows (3 in total)
# print(e1, e1.shape, e1.size)
# f = d[d%3 == 0] # takes all cells from matrix d respecting this condition
# print(f)
# # how to revert all rows of a matrix using negative indexing
# a = np.arange(0,120,4) # from start (0) to end (120), takes a number every step (5) and puts them in an array
# b = a.reshape(10,3) 
# c = b[:,::-1]
# print(len(b), b.shape, b.size, b)
# print(len(c), c.shape, c.size, c)
# How to take only all cells in a range or respecting a specific complex condition
# a = np.arange(0,120,4) # from start (0) to end (120), takes a number every step (5) and puts them in an array
# b = a.reshape(10,3)
# # all cell values 0<=x<=20 or x >=70  
# d = np.where(((b>= 0) & (b<=20) | (b>=70)), b, 'Nope') # values the condition. If true, it gives current cell value, otherwise 'Nope'
# print(d)
# e = np.where(((b>= 0) & (b<=20) | (b>=70))) # same operation but with default return values
# print(e) # every number different from 0 means True, 0 means False
# print(b[e]) # if an e cell value is True, then its relative b cell value is True too so it will be printed

# # Math operations on a single matrix or between two matrices of the same (m, n) dimensions
# a = np.arange(3,45,3) # from start (0) to end (120), takes a number every step (5) and puts them in an array
# b = a.reshape(7, 2)
# c = np.arange(2, 30, 2)
# d = c.reshape(7, 2)
# # print(b) 
# # print(d)
# s1 = b.sum() 
# s2 = b.sum(0) # outputs a sum for each column of b
# s3 = b.sum(1) # outputs a sum for each row of b
# s4 = b.cumsum() # cumulative sum: after putting all cells in one array only, for each element in that array,
# # it outputs the sum of that element with its previous elements (if any)
# s5 = b + d
# s6 = b - d
# p1 = b.prod() 
# p2 = b.prod(0) # outputs a product for each column of b
# p3 = b.prod(1) # outputs a product for each row of b
# p4 = b.cumprod() # cumulative product: after putting all cells in one array only, for each element in that array,
# # it outputs the product of that element with its previous elements (if any) 
# p5 = b * d
# p6 = b / d
# p7 = np.dot(b, d)
# print(s1, p1)  
# print(s2, p2) # please, pay attention to the length of these arrays
# print(s3, p3) # please, pay attention to the length of these arrays
# print(s4) # please, pay attention to the length of these arrays
# print(p4) # please, pay attention to the length of these arrays
# print(s5)
# print(s6)
# print(p5)
# print(p6)

# # Broadcasting: math operation between a (m, n) matrix and either a (m, 1) or (1, n) vector
# a = np.array([[1, 2, 3, 4], [11, 12, 13, 14], [21, 22, 23, 24]]) # a is (3, 4)dimensional
# b = np.array([2, 4, 6, 8]) # b is (1, 4)dimensional
# c = np.array([[5], [10], [15]]) # c is (3, 1)dimensional
# d = np.array([[1, 2, 3, 4, 5], [11, 12, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35]]) # d is (4, 5)dimensional
# print(a)
# print(b)
# print(c)
# s1 = a + b # there's difference too, of course
# s2 = a + c # there's difference too, of course
# p1 = a * b # there's division too, of course
# p2 = a * c # there's division too, of course
# p3 = np.dot(a, d) # dot product: you can do it only between an (m,n) and (n,q) matrix
# print(s1)
# print(s2)
# print(p1)
# print(p2)
# print(p3) 