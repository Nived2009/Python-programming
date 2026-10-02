Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String Methods
#Upper()
a="i am learnimg python"
a.upper()
'I AM LEARNIMG PYTHON'
#capitalize()
a.capitalize()
'I am learnimg python'
#title()
a.title()
'I Am Learnimg Python'
#isupper()
a.isupper()
False
#islower()
a.islower()
True
#startswith()
a.startswith("i")
True
#endswith()
a.endswith("a")
False
#isalpha(): checks the condition if the contains only alphabets
a.isalpha()
False
#note space is not an alphabet
#isdigit(): is the string only contains digits
b="6549849"
b.isdigit()
True
#isalnum(): weather the string digits , alphabets or digits and alphabets
c="nivi141216"
c.isalnum()
True
a.isalnum()
False
b.isalnum()
True
d=56464
d.alnum()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d.alnum()
AttributeError: 'int' object has no attribute 'alnum'
#note: spaces are neither digits nor alphabets

#strip()
#lstrip(): removes left side spaces
#rstrip(): removes right side spaces
e="       python        "
e.lstrip()
'python        '
e.rstrip()
'       python'

#split(): seperates the words in the sentences
a.split()
['i', 'am', 'learnimg', 'python']

#join()
f="lough","out","loud"
"".join(f)
'loughoutloud'
" ".join(f)
'lough out loud'
"-".join(f)
'lough-out-loud'
g="LoL"
"-".join(g)
'L-o-L'

>>> #concatenation
>>> a="i"
>>> b="am"
>>> c"nived"
SyntaxError: invalid syntax
>>> c="nived"
>>> print(a+b+c)
iamnived
>>> print(a+" "+b+" "+c)
i am nived
>>> 
>>> #example
>>> a
'i'
>>> b
'am'
>>> c
'nived'
>>> print((a+" "+b+" "+c).title())
I Am Nived
>>> 
>>> 
>>> #formatting
>>> a=44
>>> b=23
>>> print("The sum of a and b is",a+b)
The sum of a and b is 67
>>> 
>>> 
>>> #format method
>>> a="nived"
>>> b="thanmai"
>>> print("hello {}{}".format(a,b))
hello nivedthanmai
>>> print("hello {} {}".format(a,b))
hello nived thanmai
>>> print("hello {} bye {}".format(a,b))
hello nived bye thanmai
>>> 
>>> #fstring
>>> print(f"hello {a}{b}")
hello nivedthanmai
>>> print(f"hello {a} {b}")
hello nived thanmai
>>> print(f"hello {a} bye {b}")
hello nived bye thanmai
