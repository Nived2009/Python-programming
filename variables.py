Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Variable

#name should start with a letter or underscore.
a=1
print(a)
1
_=2
print(_)
2

#We cannot use python keywords as variable names.
for=10
SyntaxError: invalid syntax

# Do not use numbers at the start of variable names.
5a=99
SyntaxError: invalid decimal literal

#The only allowed special character is underscore (_) .
thanmai_thanu=45
print(thanmai_thanu)
45
>>> 
>>> #Variable names can only have alphanumeric characters (A-Z,a-z,0-9) and underscore.
>>> @=20
SyntaxError: invalid syntax
>>> 
>>> #Variable names are case sensitive (e.g Age, age and AGE are different variable names)
>>> A=72
>>> B=56
>>> print(b)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(b)
NameError: name 'b' is not defined. Did you mean: 'B'?
>>> print(B)
56
>>> 
>>> 
>>> c=3,4,5,6,7,8
>>> print(c)
(3, 4, 5, 6, 7, 8)
>>> 
>>> u,v,w=78,456,890
>>> print(u,v,w)
78 456 890
>>> 
>>> name="nived"
>>> print(name)
nived
>>> print("name")
name
>>> 
>>> #unpacking: it displaces without brackets
>>> d,e,f=(78,49,30)
>>> print(d,e,f)
78 49 30
>>> 
>>> #del: it helps to clear the stored value in the variable
>>> g=36
>>> print(g)
36
>>> del g
>>> print(g)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(g)
NameError: name 'g' is not defined
