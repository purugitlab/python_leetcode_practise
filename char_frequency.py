# Find frequncy of char with count fuction
str = "aba"
dict = {}
for i in str:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1 
print(dict)
