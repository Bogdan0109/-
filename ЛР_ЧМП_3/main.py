# import numpy as np
# import math
# from scipy.misc import derivative

# def f(x):
#     return pow(x,4) +4*pow(x,3) - 8*pow(x,2) - 17

# # a = -2.
# # b = -1/2
# # eps = 0.001 #точність

# def nuton(a,b,eps):
#     df2 = derivative(f, b, n = 1)
#     if (f(b)*df2>0):
#         xi = b
#     else:
#         xi = a
#     df = derivative(f,xi, n= 1)
#     xi_1 = xi - f(xi)/df
#     while (abs(xi_1 - xi)>eps): #accuracy check
#         xi = xi_1
#         xi_1 = xi - f(xi)/df
#     return print ('Solving the equation by Newton*s method x = ', xi_1)
    
# nuton(-2,-1/2,0.0001)

import numpy as np
import math
from scipy.misc import derivative

def f(x):
    return pow(x,4) +4*pow(x,3) - 8*pow(x,2) - 17

def komb(a,b,eps):
    if (derivative(f, a, n = 1)*derivative(f, a, n = 2)>0):
        a0 = a
        b0 = b
    else:
        a0 = b
        b0 = a
    ai = a0
    bi = b0
    while abs(ai-bi)>eps:
        ai_1 = ai -f(ai)*(bi - ai)/(f(bi) - f(ai))
        bi_1 = bi - f(bi)/derivative(f,bi, n= 1)
        ai = ai_1
        bi = bi_1
    x = (ai_1+bi_1)/2
    return print('Solving the equation by the combined method x = ', x)

komb(-2,-1/2,0.0001)
