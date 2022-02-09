from math import fabs
from tabulate import tabulate as table
import matplotlib.pyplot as plt


def length(array):
    # выбор длины
    if fabs(array[2] - array[0]) >= fabs(array[3]-array[1]):
        return fabs(array[2] - array[0])
    else:
        return fabs(array[3]-array[1])


def sign(integer):
    if integer == 0:
        return 0
    elif integer > 0:
        return 1
    else:
        return -1


def grafikprint(array):
    # Цифровой дифференциальный анализатор
    graph = [['i', 'x', 'y']]
    deltaX = (array[2] - array[0])/length(array)
    deltaY = (array[3] - array[1])/length(array)
    X = array[0] + 0.5 * sign(deltaX)
    Y = array[1] + 0.5 * sign(deltaY)
    for i  in range(int(length(array))):
        graph.append([i,X,Y])
        X += deltaX
        Y += deltaY
    return graph


def brez(array):
    # общий алгоритм Брезенхема
    x, y = array[0], array[1]
    dx = fabs(array[2] - array[0])
    dy = fabs(array[3] - array[1])
    s2, s1 = sign(array[3] - array[1]), sign(array[2] - array[0])
    trade = None
    if dy > dx :
        dx, dy = dy, dx
        trade = 1
    X, Y = [],[]
    e = 2*dy - dx
    for i in range(int(dx)):
        X.append(x)
        Y.append(y)
        while e > 0:
            if trade == 1:
                x += s1
            else:
                y += s2
            e -= 2*dx
        if trade == 1:
            y += s2
        else:
            x += s1
        e += 2 * dy
    return X,Y


if __name__ == '__main__':
    # более красиво оформить
    array = input('Введите координаты точек: ').split()
    array = [int(i) for i in array]
    print(table(grafikprint(array)))
    a = grafikprint(array)[1:]
    x,y = [],[]
    for i in a:
        x.append(i[1])
        y.append(i[2])
    X,Y = brez(array)
    print(X,Y)
    b = plt.plot(x, y, X, Y)
    plt.show()
