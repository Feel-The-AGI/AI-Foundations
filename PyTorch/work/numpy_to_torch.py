import torch
import numpy as np

"""
# CONVERTING TENSOR TO NUMPY ARRAY
# first create a tensor
a = torch.ones(5)
print(a)

# initialize a new variable b to torch tensor a
b = a.numpy()
print(b)
print(type(b)) # check type of b


# BE CAREFUL WHEN CONVERTING BECASUE IF THE TENSOR OBJECT IS ON GPU AND NOT CPU, AND NUMPY POINTS TO CPU, IT WILL CHANGE THE OBJECT TO CPU.
# GPU AND CPU ARE MEMORY LOCATIONS


a.add_(1)
print(a)
print(b) # it will add 1 to each element in the array as well even though we are
"""

# ===========================================================

# CONVERTING NUMPY ARRAY TO TENSOR

c = np.ones(5)
print(c)

d = torch.from_numpy(c)
print(d)

# BE CAREFUL HERE AGAIN, IF YOU MODIFY ONE VARIABLE, IT WILL AFFECT ALL SUBSEQUENT ONES POINTING TO IT

c += 1
print(c)
print(d)

# THESE WARNINGS WILL HAPPEN WHEN YOU'RE DEALING WITH GPU, IT WOULD SAY ITS NOT ABLE TO DETECT A GPU OR SOME SIMILAR ERROR, TELLING YOU THE MEMORY YOU'RE POINTING TO DOESNT EXIST.
# HERES HOW TO TROUBLESHOOT IT
# LETS ALSO CREATE A TENSOR ON THE GPU

"""
if torch.cuda.is_available():
    device = torch.device('cuda')
    print('GPU Found... Using GPU')
    e = torch.ones(2, device=device)
    print(e)
else:
    device = torch.device('cpu')
    print('GPU not found... Using CPU')
"""

# THE ABOVE IS CLUTTERED, LETS WRITE NEAT CODE

device = ['cuda', 'cpu']
if torch.cuda.is_available():
    device = torch.device(device[0])
    print('GPU found... using GPU.')
else:
    device = torch.device(device[1])
    print('GPU not available... using CPU.')

size = 64 

def create_tensor(size: int):
    tnsor = torch.rand(size)
    tnsor1 = torch.rand(size)
    fnl_tnsor = tnsor1.mul_(tnsor**size).to(device) # moves object to available device

    # using a gpu tensor it will cause an error if youu convert it to numpy as numpy only handles cpu tasks.
    # fnl_tnsor.numpy() # only works on cpu
    return fnl_tnsor

print(create_tensor(size))

# =======================================================
# if you need to calculate tensor gradients when reaching optimizations steps do the below
# this tells torch to calculate the gradient of the tensor when you reach the optimizations stage
# whenever theres a variable in a model that needs to be optimized we need the gradients
tensor_grad = torch.rand(5**size, requires_grad=True)
print(tensor_grad)
