Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Striding
>>> #[a]-indexing
>>> #[a:b]-slicing
>>> #[a:b:c]-striding
>>> #a-starting
>>> #b-ending
>>> #c-increment
>>> 
>>> a="data Science"
>>> "STRIDING"
... 
... #[a : b : c]
... 
... #a → Starting index
... #b → Ending index
... #c → Increment (step)
... 
... 
... #Example 1:
... 
... a = "striding"
... 
... #Index:
... # 0 1 2 3 4 5 6 7
... #  s t r i d i n g
... 
... 
... a[::]
... 
... 
... a[0::1]
... 
... #It first takes a[0], which is 's'.
... 
... #The increment is 1, so:
... 
... #a[0 + 1] = a[1] = 't'
... 
... #Again, the increment is 1:
... 
... #a[1 + 1] = a[2] = 'r'
... 
... #This continues until the last character:
... 
#a[6 + 1] = a[7] = 'g'

#∴ It prints "striding"


[::2]

#It first takes a[0] → 's'.

#The increment is 2, so:

#a[0 + 2] = a[2] → 'r'

#Next: a[2 + 2] = a[4] → 'd'

#Next: a[4 + 2] = a[6] → 'n'

#Now: a[6 + 2] = a[8]

#But a[8] does not exist.

#∴ Output is "srdn"

#Example 2:

a = "cloud computing"

#Index:
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
#  c l o u d _ c o m p  u  t  i  n  g


a[6:15:2]

#First:

#a[6:15] → "computing"

#Now: a[6:15:2] → The increment is 2.

#So: a[6] → 'c'

#a[6 + 2] = a[8] → 'm'

#a[8 + 2] = a[10] → 'u'

#a[10 + 2] = a[12] → 'i'

#a[12 + 2] = a[14] → 'g'


#∴ The output of a[6:15:2] is "cmuig"
SyntaxError: multiple statements found while compiling a single statement
"STRIDING"

#[a : b : c]

#a → Starting index
#b → Ending index
#c → Increment (step)


#Example 1:

a = "striding"

#Index:
# 0 1 2 3 4 5 6 7
#  s t r i d i n g


a[::]
'striding'

a[0::1]
'striding'
#It first takes a[0], which is 's'.

#The increment is 1, so:

#a[0 + 1] = a[1] = 't'

#Again, the increment is 1:

#a[1 + 1] = a[2] = 'r'

#This continues until the last character:

#a[6 + 1] = a[7] = 'g'

#∴ It prints "striding"


a[::2]
'srdn'
#It first takes a[0] → 's'.

#The increment is 2, so:

#a[0 + 2] = a[2] → 'r'

#Next: a[2 + 2] = a[4] → 'd'

#Next: a[4 + 2] = a[6] → 'n'

#Now: a[6 + 2] = a[8]

#But a[8] does not exist.

#∴ Output is "srdn"

#Example 2:

a = "cloud computing"

#Index:
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
#  c l o u d _ c o m p  u  t  i  n  g


a[6:15:2]
'cmuig'
#First:

#a[6:15] → "computing"

#Now: a[6:15:2] → The increment is 2.

#So: a[6] → 'c'

#a[6 + 2] = a[8] → 'm'

#a[8 + 2] = a[10] → 'u'

#a[10 + 2] = a[12] → 'i'

#a[12 + 2] = a[14] → 'g'


