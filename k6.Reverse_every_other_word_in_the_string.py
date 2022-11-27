#Reverse every other word in the string
def reverse_alternate(string):
    '''new_s = string.split()
    result = ''
    for i in range(len(new_s)):
        if i%2 != 0:
            result += new_s[i][::-1] + " "
        else:
            result += new_s[i]+ " "
    return result.strip()'''

    return " ".join(s[::-1] if i%2 else s for i,s in enumerate(string.split()))

obj = reverse_alternate("Reverse this string, please!") #, "Reverse siht string, !esaelp")
print(obj)

# Notes:
# enumerate()
# prog in one line
