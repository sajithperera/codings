#changing the base to decimal


#binary to decimal
def bintodeci(number):
    result = int(number,2)
    return result


#octal to decimal
def octtodeci(number):
    result = int(number,8)
    return result


#hexadecimal to decimal
def hextodeci(number):
    result = int(number,16)
    return result




s= input("Enter the number : ")
n= int(input("Enter the base number : "))


if(n==2):
    val=bintodeci(s)
if(n==8):
    val=octtodeci(s)
if(n==16):
    val=hextodeci(s)



print("The number in decimal base is ",val)
