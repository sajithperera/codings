#palindrome check with how the recursive algorithm flows


#return whether this is a palindrome or not
def ispal(s):
    if(len(s)<2):
        print("About to return True from isPal from the base case")
        return True
    if(s[0]==s[-1]):
        result=(s[0]==s[-1])
        print("About to return result", result, "from isPal with argument", s[1:-1]) 
        return ispal(s[1:-1])
    else:
        return False



s = input("Enter yor string lowercase : ")

n = ispal(s)

if(n== True):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
