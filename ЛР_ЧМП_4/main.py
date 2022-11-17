import numpy as np
def task1():
    A=np.matrix([[1,2,], [4,-1,]])
    B=np.matrix([[1,2,], [0,1,]])
    rezult=A*B-B*A
    print(f"\n1\n{rezult}")


def task2():
    A=np.array([[-1,2,], [0,1,]])
    rezult=A**2
    print(f"\n2\n{rezult}")


def task3():
    A=np.array([[3,5,], [6,-1,]])
    B=np.array([[2,1,], [-3,2,]])
    rezult=A*B
    print(f"\n3\n{rezult}")


def task4():
    A=np.matrix([[2,3,4,], [1,0,6,], [7,8,9,]])
    rezult=np.linalg.det(A)
    print(f"\n4\n{rezult}")


def task5():
    A=np.array([[1, 2, 3, 4], [-2, 1, 4, 3], [3, -4, -1, 2], [4, 3, -2, -1]])
    rezult=np.linalg.det(A)
    print(f"\n5\n{rezult}")


def task6():
    A=np.array([[1, 2, 2], [2, 1, -2], [2, -2, 1]])
    rezult=np.linalg.inv(A)
    print(f"\n6\n{rezult}")


def task7():
    A=np.array([[-2, 3, 1, -1], [3, 2, 1, 4], [1, 2, 3, 4], [0, 2, 3, 3]])
    rezult=np.linalg.matrix_rank(A)
    print(f"\n7\n{rezult}")
# ??????????????????????????????????????????????????????????????????????????????????????????????
a=np.array([[3,-5,3],[1, 2, 1],[2, 7, 1]])
b=np.array([[1],[4],[8]])
def kramer(a, b):
    a_det = np.linalg.det(a)
    print('Детермінант матриці = ', a_det)
    if (a_det != 0):
        print ('Розв*язуємо систему')
        x_m = np.matrix(a)
        x_m[:, 0] = b # формування допоміжної матриці (1 ст. замінюємо на ст. b)
        print('x_m=', x_m)
        y_m = np.matrix(a) #2 ст. замінюємо на ст. b
        y_m[:, 1] = b #2 c
        print('y_m=',y_m)
        z_m = np.matrix(a) #3 ст. замінюємо на ст. b
        z_m[:, 2] = b
        print('z_m=',z_m)
        x = np.linalg.det(x_m) / a_det
        y = np.linalg.det(y_m) / a_det
        z = np.linalg.det(z_m) / a_det
        print('X = ', round(x,5))
        print('Y=', round(y,5))
        print('Z=', round(z,5))
    else:
            print('Розв*язків немає')
kramer(a, b)
task1()
task2()
task3()
task4()
task5()
task6()
task7()
