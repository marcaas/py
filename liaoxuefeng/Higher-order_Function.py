from functools import reduce
from ctypes import sizeof

# def add(x,y,f):
#     return f(x)+f(y)
# print(add(-5,6,abs))

# def f(x):
#     return x*x

# L=map(f,[1,2,3,4,5,6,7,8,9])
# print(list(L))
# #-----------------------------------------------------------------------------------------------------------------------
# L=map(str,[1,2,3,4,5,6,7,8,9])
# print(list(L))

# from functools import reduce
# def add(x,y):
#     return x+y

# print(reduce(add,[1,3,5,7,9]))
# #-----------------------------------------------------------------------------------------------------------------------
# def fn(x,y):
#     return x*10+y
# print(reduce(fn,[1,3,5,7,9]))

# def char2num(s):
#     digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     return digits[s]

# print(reduce(fn,map(char2num,'13579')))
# #-----------------------------------------------------------------------------------------------------------------------
# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# def str2int(s):
#     def fn(x,y):
#         return x*10+y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn,map(char2num,s))

# print(str2int('13579'))
# #-----------------------------------------------------------------------------------------------------------------------
# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# def str2int(s):
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(lambda x,y:x*10+y,map(char2num,s))

# print(str2int('13579'))
# #-----------------------------------------------------------------------------------------------------------------------
# def normalize(name):
#     return str(name[0].upper())+str(name[1:].lower())

# namels = ['adam', 'LISA', 'barT']

# print(list(map(normalize,namels)))
# #-----------------------------------------------------------------------------------------------------------------------
# def prod(L):
#     def f(x,y):
#         return x*y
#     return reduce(f,L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')
# #-----------------------------------------------------------------------------------------------------------------------
# #利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2float(s):
#     sb = s.find('.')
#     def char2int(c):
#         return DIGITS[c]
#     def add(x,y):
#         return x * 10 + y
#     return reduce(add,map(char2int,s.replace('.',"")))/(10**sb)
    
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')
#-----------------------------------------------------------------------------------------------------------------------
