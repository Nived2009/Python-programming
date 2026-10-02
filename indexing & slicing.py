Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
#positive indexing
#Thanmai
#0-T,1-h,2-a,3-n,4-m,5-a,6-i
a="Thanmai"
a[0]
'T'
a[1]
'h'
a[5]
'a'
a[6]
'i'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]
'Thanmai'

#negetive indexing
#-7-T,-6-h,-5-a,-4-n,-3-m,-2-a,-1-i
a[-1]
'i'
a[-5]
'a'
a[-1]
'i'
a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]+a[-7]
'iamnahT'

#note: in a sentence space" " is also counted as a index
b="Thanu is Topper"
b[5]
' '

#slicing
#start (Optional): The index where the slice begins (inclusive). Defaults to 0.
#stop (Optional): The index where the slice ends (exclusive — it stops just before this index). Defaults to the end of the sequence.
#sequence[start:stop]

c="Viswa Thanmai"
c[0:5]
'Viswa'
c[6:13]
'Thanmai'

