# import locale
# print(locale.getpreferredencoding())
import time
dat = open('store_2','w', encoding ='utf-8')
#with open ('store_2','w') as dat:
def benchmark(func):
    def speed(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        # можно было не ставить но хотелось чтобы и печать была.
        print(' Время выполнения: {} секунд.\n'.format(end - start))
        print(' Время выполнения: {} секунд.\n'.format(end - start), file=dat)
        return value
    return speed
a = 'abstraction'
# символы вынесены отдельно, так как меняя символы можно изменять рисунок (в определенных пределах)
d = ['*', '#', '%', '^', '@', '^', '%', '#', '*']
g = ['$', '~', ' ', '/', '*', '/', ' ', '~', '$']
@benchmark
def ris(a, d):
    def podst(x, x1, y, z, i, j):
        if x < i < x1 and y <= j < y + 2:
            a[i][j] = z
            return (a[i][j])
        elif x < i < x1 and 20 - (y + 2) <= j < 20 - y:
            a[i][j] = z
            return (a[i][j])
    a = a[:9]
    a = [[i] for i in a]
    # конвектор слов в символы (он есть в задании, но по хорошиму можно было не писать его отдельно
    # обойтись только циклом ниже, немного его изменив,
    # так как по сути он функционально работает по принцыпу конвектора )
    for i in range(len(d)):
        a[i] = (d[i] * 20)
    for i in range(len(a)):
        a[i] = [i for i in a[i]]
    for i in (range(len(a))):
        for j in range(20):
            x, x1, y = 3, 6, 0
            podst(x - 0, x1 + 0, y + 6, '^', i, j)
            podst(x - 1, x1 + 1, y + 4, '%', i, j)
            podst(x - 2, x1 + 2, y + 2, '#', i, j)
            podst(x - 3, x1 + 3, y + 0, '*', i, j)
    for i in (range(len(a))):
        for j in range(20):
            print(a[i][j], end=' ')
            print(a[i][j], end=' ', file=dat)
        print()
        print(file=dat)
    return ris
b = ris
b(a, d)
b(a, g)
dat.close()