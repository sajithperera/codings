#input from the user is required
#common divisors for two numbers


#this function will return the common divisors to both numbers
def cmmn(num1, num2):
    for i in range (2, int(min(num1,num2))+1):
        if(num1%i ==0 and num2%i ==0):
            divisors.append(i)
    return divisors

a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))

divisors =[1]
c= cmmn(a,b)


print("Common diviser for",a," & ",b," are ",divisors)
