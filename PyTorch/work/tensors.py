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
# o = torch.rand(3,3)
# p = torch.rand(3,3)

# way 1
# q = o * p
# print(q, end='\n')

# way 2
# q = torch.mul(o,p)
# print(q, end='\n')

# way 3
# p.mul_(o)
# print(p, end='\n')

# ==========================================================

# dividing matrices
# r = torch.rand(2,2)
# s = torch.rand(2,2)

# way 1
# t = r / s
# print(t)

# way 2
# t = torch.div(r,s)
# print(t)

# way 3
# inplace division
# r.div_(s)
# print(r)



# ==========================================================


# SLICING
# u = torch.rand(5,4)
# print(u)
# print(u[1, 1])

# get the actual full figure only if you have one element in the tensor
# print(u[1, 1].item())


# ==========================================================

# RESHAPING

v = torch.rand(8,8)
print(v)

# w = v.view(63) # 1 dimension | th size here must not be less than the inherited shape ==> 8*8=64. Hence the minimum value passed here should be 64
# print(w) # This will raise a 'RuntimeError: shape '[5]' is invalid for input of size 64' error

# correct implementation
w = v.view(64)
# print(w)


# you dont have to explicitly determine the size, torch does it automatically. The below implementation is very helpfull especially when youre dealng with voluminous unknown dimensions. -- Print the shape and determine how to eveninly split the items into batches
print(w.size()) # Get size

w = v.view(-1, 8) # -1 to get the end of the matrix, then in batches of 32 to get the sum of 64. Equally yo can bring it all the way down to 16,8,4 or even 2. It just needs to be equal.

# print(w)

