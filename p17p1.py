#divisor list finding


#finding the divisor list
def findDivisor(num):
    for i in range(2,int(num/2)+1):
        if (num%i==0):
            divisors.append(i)
    divisors.append(num)
    return divisors





x= int(input("Enter a number : "))

if (x>0):
    divisors = [1]
    print(findDivisor(x))
else:
    print("negative number")
