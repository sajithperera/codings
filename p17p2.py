#finding common divisors

#this function will return the set of common divisors
def commonDivisor(num1, num2):
    for i in range (2, int(min(num1,num2))+1):
        if(num1%i ==0 and num2%i ==0):
            divisors.append(i)
    return divisors


x= int(input("Enter a number 1 : "))

y= int(input("Enter a number 2 : "))

if(x>0 and y>0):
    divisors =[1]
    print(commonDivisor(x,y))
else:
    print("negative number")
