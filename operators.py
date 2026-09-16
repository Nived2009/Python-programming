Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Operators

#arthematic
a=3
b=6
print (a+b)
9
print (a-b)
-3
print (a*b)
18
print (a//b)
0
print (a/b)
0.5
print (a%b)
3
print (a**b)
729

#assignment
a=3
b=4
print(a+=b)
SyntaxError: invalid syntax
a+=b
print(a)
7
a
7
a-=1
a
6
a
6
a*=5

a
30

a/=10
a
3.0

a**=2
a
9.0

a%=3

a
0.0

#comparision
del a
a
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a
NameError: name 'a' is not defined

#comparision
a=5
b
4
a<b
False
a>b
True
a<=b
False
a>=b
True
a!=b
True
a==b
False
a=5
b=5
a==b
True

del a,b

>>> #logical
>>> a=8
>>> b=10
>>> a<b and b>a
True
>>> a<=b and b>=a
True
>>> a!=b and a==b
False
>>> a<b or b>a
True
>>> a<=b or a>=b
True
>>> a!=b or a==b
True
>>> not True
False
>>> not False
True
>>> 
>>> #Identify
>>> a=5
>>> type(a)
<class 'int'>
>>> type(a) is int
True
>>> type(a) is not int
False
>>> type(a) is float
False
>>> type(a) is not float
True
>>> 
>>> #Membership
>>> a=1,5,6,67,69
>>> 5 in a
True
>>> 67 not in a
False
>>> 12 in a
False
