# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs

# f1, f2, f3 = count()

# print(f1(), f2(), f3())

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs

# f1, f2, f3 = count()

# print(f1(), f2(), f3())

# ===========================================================================================================

# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))

# print('is_odd: ', L)

# L = list(filter(lambda x : x % 2 == 1, range(1,20)))

# print('lambda: ', L)

# ======================================================================

# class Student():
#     def __init__(self, name, score) -> None:
#         self.name = name
#         self.score = score

#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'

# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())

# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

# ========================================================================================

# # 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
# # class Student(object):
# #     def __init__(self, name, gender):
# #         self.name = name
# #         self.gender = gender

# class Student():
#     def __init__(self, name, gender) -> None:
#         self.__name = name
#         self.__gender = gender
    
#     def get_gender(self):
#         return self.__gender

#     def set_gender(self, new_gender):
#         self.__gender = new_gender

# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

# ===================================================================

# # 继承和多态

# class Animal():
#     pass

# class Dog(Animal):
#     def run(self):
#         print('Dog is running..')

# class Cat(Animal):
#     def run(self):
#         print('Cat is running..')

# dog = Dog()
# dog.run()

# cat = Cat()
# cat.run()

# =======================================================

# # 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

# class Student(object):
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Student.count += 1

# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')

# ==========================================================

# from multiprocessing import Process
# import os

# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

    # ==============================================================================

# from tkinter import *
# import tkinter.messagebox as messagebox

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()

#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)

# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()

# ==================================================================================

# # 导入socket库:
# import socket

# # 创建一个socket:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # 建立连接:
# s.connect(('www.sina.com.cn', 80))

# # 发送数据:
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)

# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

# # 关闭连接:
# s.close()

# =========================================================================

# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# import sqlite3

# # 连接到SQLite数据库
# # 数据库文件是test.db
# # 如果文件不存在，会自动在当前目录创建:
# conn = sqlite3.connect('test.db')
# # 创建一个Cursor:
# cursor = conn.cursor()
# # 执行一条SQL语句，创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 继续执行一条SQL语句，插入一条记录:
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# # 通过rowcount获得插入的行数:
# print('rowcount =', cursor.rowcount)
# # 关闭Cursor:
# cursor.close()
# # 提交事务:
# conn.commit()
# # 关闭Connection:
# conn.close()

# # 查询记录：
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# # 执行查询语句:
# cursor.execute('select * from user where id=?', '1')
# # 获得查询结果集:
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()

# ======================================================================

# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# =======================================================

# try:
#     print('try...')
#     r = 10 / int('a')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# finally:
#     print('finally...')
# print('END')

# ===================================================

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# ===================================================