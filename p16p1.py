#recursive program

#this function will return the number and calculate number of terms
def f(n):
    global terms
    terms = terms +1
    print("function calls for ",n)
    if n == 1:
        return 2
    else:
        return 2 * f(n-1)

x= int(input("Enter a number >1 : "))
while(x>=1):
    terms =0
    print("The value returned by the function is ",f(x))
    print("Number of terms in the function ",terms)
    x= int(input("Enter a number >1 : "))
    
print("end of the program")

