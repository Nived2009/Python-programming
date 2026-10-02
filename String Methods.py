Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String Methods
a="python"
len(a)
6
a="      "
len(a)
6
del a
a="  "
>>> len(a)
2
>>> a="5165489494"
>>> len(a)
10
>>> #len(): it counts no.of characters in the string
>>> 
>>> #variable.count(): it is a method used to count the number of times a specific value appears inside an iterable object
>>> b="twinkle twinkle little star"
>>> b.count("twinkle")
2
>>> b.count("t")
5
>>> b.count(" ")
3
>>> 
>>> #find a string
>>> a
'5165489494'
>>> a="python"
>>> a.find
<built-in method find of str object at 0x000001A55ABFBEA0>
>>> 
>>> a.find("p")
0
>>> #here it gives index of the character in the string
>>> 
>>> 
>>> #escape sequences
>>> #\n-> new line
>>> #\t-> tab space
>>> a="\nUsers\tNIVED\nOneDrive\tDesktop\nPython programs\tcommand prompt\n"
>>> print(a)

Users	NIVED
OneDrive	Desktop
Python programs	command prompt

>>> #replace(): This method replaces occurrences of a specified substring with another substring.
>>> #syntax : string.replace(old, new, count)
>>> a="thanmai is smart"
>>> a.replace("thanmai","nived")
'nived is smart'
>>> b="cow, cow, cow, goat"
>>> b.replace("cow","donkey",2)
'donkey, donkey, cow, goat'
