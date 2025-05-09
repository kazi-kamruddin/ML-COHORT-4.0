#task1:
x = int(input("enter x: "))
y = int(input("enter y: "))
z = int(input("enter z: "))


if (x>y and x>z):
    print("x is the largest")
elif (y>z and y>x):
    print("y is the largest")
else:
    print("z is the largest")



#task2:
cg1 = float(input("enter cg1: "))
cg2 = float(input("enter cg2: "))
cg3 = float(input("enter cg3: "))
print(" ")


if (cg1<cg2 and cg1<cg3):
    print("1st bondhu has the lowest cg")
elif (cg2<cg3 and cg2<cg1):
    print("2nd bondhu has the lowest cg")
else:
    print("3rd bondhu has the lowest cg")

avg = (cg1 + cg2 + cg3) / 3
print("their avg cg -> ", avg)



#task3:
a = 15
b = 10

c = a^b
print(c)  

#  a = 15 = 1111              
#  b = 10 = 1010
#  c =  5 = 0101    xor e (00,11 -> 0 , 10,01 -> 1) 