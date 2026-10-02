Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Questions the methods(striding,string,list,tuple,sets & dictionary)
>>> #1: a=[9,1,5,2,8,4,7,6,3,0] output should be [7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> a=[9,1,5,2,8,4,7,6,3,0]
>>> b=a[5:]
>>> b.sort()
>>> b.reverse()
>>> b
[7, 6, 4, 3, 0]
>>> 
>>> c=a[0:5]
>>> c.sort()
>>> c.reverse()
>>> c
[9, 8, 5, 2, 1]
>>> 
>>> output=b+c
>>> print("output is",output)
output is [7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
