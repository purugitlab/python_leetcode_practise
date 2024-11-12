# code to check str is symmetrical
str = "amaamaz"

print("input string is " + str)
str_len = len(str)
mid = len(str)//2
print(mid)
print(str_len)
print(str[:mid:],str[mid::])
if str_len % 2 == 0:
    if str[:mid:] == str[mid::]:
        print(str + "is symmetrical")
    else:
        print(str + "is not symmetrical")
elif str_len % 2 != 0:
    if str[:mid:] == str[mid+1::]:
        print(str + "is symmetrical")
    else:
        print(str + "is not symmetrical")
