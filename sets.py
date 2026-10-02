Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
#set  is an unordered collection
a{3,6.9,"thanmai",6+7j,False}
SyntaxError: invalid syntax
a={3,6.9,"thanmai",6+7j,False}
a
{False, 3, 6.9, 'thanmai', (6+7j)}
type(a)
<class 'set'>
#set don't store repeated values
a={5,1,2,7,3,1,6,5,4,1,8,4,9,4,8,9,4}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}

#add()
a.add(67)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 67}

#issubset()
b={1,5,67}
b.issubset(a)
True
a.issubset(b)
False

#issuperset()
a.issuperset(b)
True
b.issuperset(a)
False

#union()
c={22,54,564,98,64,8,4}
a.union(c)
{64, 1, 2, 3, 4, 5, 6, 7, 8, 9, 67, 98, 564, 54, 22}

#intersection()
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 67}
b
{1, 67, 5}
c
{64, 98, 4, 564, 54, 22, 8}
a.intersection(c)
{8, 4}

#difference()
a.difference(c)
{1, 2, 3, 67, 5, 6, 7, 9}
c.difference(a)
{64, 98, 564, 54, 22}

#update()
a.update(c)
a
{64, 1, 2, 3, 4, 5, 6, 7, 8, 9, 67, 98, 564, 54, 22}
b={}
b.update(a)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    b.update(a)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
b={478484875}
48
b.update(a)
b
{64, 1, 2, 3, 4, 5, 6, 7, 8, 9, 67, 478484875, 22, 98, 564, 54}

#symmetric_difference()
a={1,2,3,4,5}
b={4,5,6,7,8}
a.symmetric_difference(b)
{1, 2, 3, 6, 7, 8}

#difference_update()
a.difference_update(b)
a
{1, 2, 3}

#intersection_update()
a={1,2,3,4,5}
a.intersection_update(b)
a
{4, 5}

#symmetric_difference_update()
a={1,2,3,4,5}
>>> a.symmetric_difference_update(b)
>>> a
{1, 2, 3, 6, 7, 8}
>>> 
>>> #copy()
>>> a
{1, 2, 3, 6, 7, 8}
>>> b
{4, 5, 6, 7, 8}
>>> b=a.copy()
>>> b
{1, 2, 3, 6, 7, 8}
>>> 
>>> #pop()
>>> a.pop()
1
>>> a
{2, 3, 6, 7, 8}
>>> 
>>> #remove()
>>> a.remove(2)
>>> a
{3, 6, 7, 8}
>>> 
>>> #discard()
>>> a.discard(7)
>>> a
{3, 6, 8}
>>> 
>>> #clear()
>>> a.clear()
>>> a
set()
>>> 
>>> #isdisjoint()
>>> a={1,2,3,4,5}
>>> b={6,7,8,9}
>>> c{1,2,6,7}
SyntaxError: invalid syntax
>>> c={1,2,6,7}
>>> a.isdisjoint(b)
True
>>> a.isdisjoint(c)
False
>>> b.isdisjoint(c)
False
