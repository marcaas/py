def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)

print('f is', f)
print('f() is', f())

f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)

print('f2 == f1 ? :', f1 == f2)

f2 = f1

print('f2 == f1 ? :', f1 == f2)