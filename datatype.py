Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Datatypes
a=1
type(a)
<class 'int'>

b=4.5
type(b)
<class 'float'>

c='thanmai'
type(c)
<class 'str'>

d="python"
type(d)
<class 'str'>

e='''nived'''
type(e)
<class 'str'>

f=5+4j
type(f)
<class 'complex'>

g=True
type(g)
<class 'bool'>

#datatype conversion
#datatype conversion
int(8)
8
int(6.9)
6
int("python")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
int(6+9j)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

float(1)
1.0
float(5.6)
5.6
float("python")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
float(5+6j)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    float(5+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
>>> float(False)
0.0
>>> 
>>> #string
>>> str(1)
'1'
>>> str(5.6)
'5.6'
>>> str("python")
'python'
>>> str(6+9j)
'(6+9j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> 
>>> complex(1)
(1+0j)
>>> complex(6.9)
(6.9+0j)
>>> complex("python")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    complex("python")
ValueError: complex() arg is a malformed string
>>> complex(6+7j)
(6+7j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> #boolean
>>> bool(1)
True
>>> bool(6.9)
True
>>> bool("python")
True
>>> bool(6+7j)
True
>>> bool(True)
True
>>> bool(False)
False
