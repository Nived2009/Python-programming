Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#List[]
a=[67,6.9,"python",9+9j,True]
type(a)
<class 'list'>
b=69
type(b)
<class 'int'>
c=[69]
type(c)
<class 'list'>

a=["python","java","c","c"]
a=["python","java","c","c++"]
a.append("html")
a
['python', 'java', 'c', 'c++', 'html']

print(a.append(["AI","ML"]))
None
a.append(["AI","ML"])
a
['python', 'java', 'c', 'c++', 'html', ['AI', 'ML'], ['AI', 'ML']]
del a
a=["python","java","c","c++"]
a.append(["AI","ML"])
a
['python', 'java', 'c', 'c++', ['AI', 'ML']]

 
#extend()
a.extend("ds","html")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.extend("ds","html")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["ds","html"])
a
['python', 'java', 'c', 'c++', ['AI', 'ML'], 'ds', 'html']

#insert()
a=["artist","kopist"]
a.insert(1,"sadist")
a
['artist', 'sadist', 'kopist']

#index()
a
['artist', 'sadist', 'kopist']
a.index("artist")
0
a.index("sadist")
1

#copy()
b=a.copy()
b
['artist', 'sadist', 'kopist']

#sort()
a=['python', 'java', 'c', 'c++', 'AI', 'ML', 'ds', 'html']
a.sort()
a
['AI', 'ML', 'c', 'c++', 'ds', 'html', 'java', 'python']
b=[5,86,8,,981,54,9,4,5,3,65,6]
SyntaxError: invalid syntax
b=[5,86,8,981,54,9,4,5,3,65,6]
b.sort()
b
[3, 4, 5, 5, 6, 8, 9, 54, 65, 86, 981]

#reverse()
a=[1,2,3,4,5,6,7,8,9]
a.reverse()
a
[9, 8, 7, 6, 5, 4, 3, 2, 1]
b=["nanna","amma","anna","tammudu"]
b.reverse()
b
['tammudu', 'anna', 'amma', 'nanna']

>>> #pop()
>>> b
['tammudu', 'anna', 'amma', 'nanna']
>>> b.pop()
'nanna'
>>> b
['tammudu', 'anna', 'amma']
>>> b.pop(1)
'anna'
>>> b
['tammudu', 'amma']
>>> 
>>> #remove()
>>> b
['tammudu', 'amma']
>>> b.remove("tammudu")
>>> b
['amma']
>>> 
>>> #len()
>>> a=['python', 'java', 'c', 'c++', 'AI', 'ML', 'ds', 'html']
>>> len(a)
8
>>> 
>>> #count()
>>> b=[1,5,1,15,15,6,9,165,18,8,9]
>>> b.count(5)
1
>>> b.count(15)
2
>>> a.count('AL')
0
>>> a.count('ML')
1
>>> 
>>> a
['python', 'java', 'c', 'c++', 'AI', 'ML', 'ds', 'html']
>>> #clear()
>>> a.clear
<built-in method clear of list object at 0x0000013E7DC83700>
>>> a.clear()
>>> a
[]
>>> a.append(['tammudu', 'anna', 'amma', 'nanna'])
>>> a
[['tammudu', 'anna', 'amma', 'nanna']]
