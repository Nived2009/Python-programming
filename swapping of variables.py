print("Swapping of two variables\n")

print("Pythonic Method")
a=int(input("a= "))
b=int(input("b= "))
a,b=b,a
print("after swapping a=",a," b=",b)

del a,b
print("\nTemporary Variable  Method")
a=int(input("a= "))
b=int(input("b= "))
temp=a
a=b
b=temp
print("after swapping a=",a," b=",b)

del a,b

print("\nArithmetic Operators Method")
a=int(input("a= "))
b=int(input("b= "))
a=a+b
b=a-b
a=a-b
print("after swapping a=",a," b=",b)

del a,b

print("\nNumber formatting method")#Swapping variables purely through string/number formatting does not actually change the values stored in memory. Instead, it alters the representation of the data visually when printing it out.
a=int(input("a= "))
b=int(input("b= "))
print("after swapping a=%d b=%d"%(b,a))

