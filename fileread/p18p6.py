#read through a file and counting some special characters


leftcount=0
rightcount=0
newlinecount=0
lettercount=0
commentcount=0


f = open("test.txt") #file open
if(f):
    s=f.readline()  #read line by line
    while(s!=""):
        for i in range(len(s)):
            if (s[i]=='<'):
                leftcount = leftcount+1
            if (s[i]=='>'):
                rightcount = rightcount+1
            if (s[i] == '\n'):
                newlinecount = newlinecount+1
            if (s[i]=='e'):
                lettercount = lettercount+1
            if (s[i]=='!'):
                commentcount = commentcount+1
        s =f.readline()     #next line read

    f.close()               #close the file

    q = open("Result.txt",'w')  #open the file to write

    q.write("This is the result file generated \n\n\n")
    q.write("Number of left angle brackets (<) are : %d \n"%leftcount)
    q.write("Number of right angle brackets (>) are : %d \n"%rightcount)
    q.write("Number of New line are : %d \n"%newlinecount)
    q.write("Number of  lowercase letter 'e' are : %d \n"%lettercount)
    q.write("Number of  comments are : %d \n"%commentcount)
        

    q.close()       #close the file
else:
    print("File is not there")
