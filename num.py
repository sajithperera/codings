Number = int(input(" Please Enter a Number: "))

if(Number>0):
    for j in range(1, Number+1):
        total = 0
        for i in range(1, j):
            if(j % i == 0):
                total = total + i
        if (total == j):
            print(" %d is a Perfect Number" %j)
        else:
            print(" %d is not a Perfect Number" %j)

else:
    print("The number is not positive")
