#An example  of recursion from Miller & Ranum to convert a long int to a string
# I have added print statements to show what happens in recursion
# I have set up an array of bases to iterate through, calling the function for each. 

def toStr(n, base):
    print("Calling the conversion function with int", n, "and base of", base)
    convertString = "0123456789ABCDEF"
    if n<base:
        print(n, "is less than", base, "and so just return", n, "and bring the process to an end.")
        return convertString[n]
    else:
        print("Now dividing", n, "by the base", base, "getting", n//base,  "and calculating the remainder", n%base, ". These will be used as arguments to call the function again.\n"  )
# recurse with arguments of the int divided by the base, and the remainder of the int divided by the base
        return toStr(n//base, base) + convertString[n%base]

i = 10258723891
b = [2,8,10]
for x in range(len(b)):
   print("The string of int", i, "in base", b[x], "is:", toStr(i,b[x]), "\n")