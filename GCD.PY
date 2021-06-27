def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)
num1= int(input("enter the first number:"))
num2= int(input("enter the second number:"))
num3= int(input("enter the third number:"))
num4= int(input("enter the fourth number:"))
print(GCD(num1,num2))
