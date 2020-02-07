# -*- coding:utf-8  -*-
# author: zhuchuang time:2020/1/3

def turn_1(a):
    a=a+1
    print(a)
    print(id(a))

def turn_2(a):
    a[0]=a[0]+1
    print(a)
    print(id(a))

b=5
print(id(b))
print('b=',b)
turn_1(b)
print('b=',b)
c=[2,3]
print(id(c))
turn_2(c)
print(c)
# python不允许程序员选择采用传值还是传引用。Python参数传递采用的肯定是“传对象引用”的方式。
# 这种方式相当于传值和传引用的一种综合。如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值－－相当于通过“传引用”来传递对象。
# 如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，就不能直接修改原始对象－－相当于通过“传值'来传递对象。

d = "123"
e=d
d= "xyz"
print(e)

name1 = "ab"
name1_2=name1.encode('unicode_escape')
print(name1_2)
abc=ascii('你好')
abc=abc.encode('ascii').decode('unicode_escape')
print(abc)
print(abc.encode('unicode_escape').decode('ascii'))

