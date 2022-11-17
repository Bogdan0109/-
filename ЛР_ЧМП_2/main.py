import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

def f(x): 
    return pow(x,4) - 4*pow(x,3) - 8*pow(x,2) - 17

a = 1.

b = 2.

eps = 0.0001 #точність

# def dihotom(a, b, eps):
#     while (abs(a-b) > eps):
#         if f(a)*f((a+b)/2)<0:
#             b = (a+b)/2
#         else:
#             a = (a+b)/2
    
#     print('Корінь рівняння x = ', round((a+b)/2,5))

# dihotom(-5,-1,0.0001)#розв'язок для 1 відрізка
# dihotom(4,9,0.0001)#для 2 відрізка

# x = np.arange(a, b, 0.01)

# plt.plot(x, f(x))

# plt.xlabel('x')

# plt.ylabel('f(x)')

# plt.title('Метод ділення навпіл')

# plt.grid()

# plt.show()



# def hord (a, b, eps):
#     if (f(a)*derivative(f, a, n = 2)>0):
#         x0 = a
#         xi = b
#     else:
#         x0 = b
#         xi = a
#     xi_1 = xi-(xi - x0) * f(xi)/(f(xi) - f(x0))
#     while (abs(xi_1 - xi) > eps):
#         xi = xi_1
#         xi_1 = xi-(xi - x0) * f(xi)/(f(xi) - f(x0))     
#     print(f'Метод хорд.Корінь знаходиться в точці x =', round(xi_1,5))
#     return xi_1


# hord(-5, -1, 0.0001)
# hord(4, 10, 0.0001)




