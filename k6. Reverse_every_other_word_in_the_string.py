#Reverse every other word in the string
def reverse_alternate(string):
    new_s = string.split()
    result = ''
    for i in range(len(new_s)):
        if i%2 != 0:
            result += new_s[i][::-1] + " "
        else:
            result += new_s[i]+ " "
    return result.strip()

#call the function
obj = reverse_alternate("Reverse this string, please!")
print(obj)
