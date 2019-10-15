#base changing program



#this function will change the base
def basechange(a,b):
    if (b==2):
        result = binary(a)
    if (b==8):
        result = octal(a)
    if (b==16):
        result = hexa(a)
    return result

#binary base
def binary(number):
    return bin(number)

#octal base
def octal(number):
    return oct(number)

#hexadecimal base
def hexa(number):
    return hex(number)


a = int(input("Enter the number : "))
b = int(input("Enter the base : "))

if (a>0 and b>0):
    print("The number in base ",b ,"is ",basechange(a,b))
else :
    print("You enterd a negative number ")
