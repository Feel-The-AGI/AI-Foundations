import torch

# x  = torch.empty(5)
# print(x)


# 4D Matrix
# a = torch.empty(4, 3, 2, 3)
# print(a)


# Random numbers
# b = torch.rand(3, 3)
# print(b)


# zeros matrix
# c = torch.zeros(3, 3)
# print(c)


# ones matrix
# d = torch.ones(3, 3)
# print(d)


# check datatype
# e = torch.ones(4, 4)
# print(e.dtype)


# change datatype
# f = torch.ones(5, 5, dtype=torch.float64)
# print(f)


# check size of matrix
# g = torch.ones(6, 5, dtype=torch.int16)
# print(g.size())


# construct tensor from data eg. a list
# lst = [0,1,2,3,4,5,6,7,8,9]
# h = torch.tensor(lst)
# print(h)

# ==========================================================

# create 2 tensors with random values
# i = torch.rand(5, 5)
# j = torch.rand(5, 5)
# print(i, j, sep='\n')

# Lets add i and j
# way 1
# k = i + j
# print(k)

# way 2
# k = torch.add(i,j)
# print(k)

# way 3
# in-place addition
# j.add_(i) # every function with a trailing underscore does an inplace operation
# print(j)

# ==========================================================

# subtracting matrices
# l = torch.rand(4,4)
# m = torch.rand(4,4)

# way 1
# n = l - m
# print(n)

# way 2
# n = torch.sub(l,m)
# print(n)

# way 3
# inplace operation
# m.sub_(l)
# print(m)

# ==========================================================

# multiplying matrices
o = torch.rand(3,3)
p = torch.rand(3,3)

# way 1
q = o * p
print(q, end='\n')

# way 2
q = torch.mul(o,p)
print(q)

# way 3
p.mul_(o)
print(p)
