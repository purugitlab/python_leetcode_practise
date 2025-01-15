# Check list is sorted or not
lst = [1,2,0,4,5,3]
for i in range(1,len(lst)):
    print(lst[i])
    if(lst[i] < lst[i-1] ):
        print(lst,  " is not sorted")
        break
# Remove duplicate from list
lst_1 = [2,4,2,2,6,4]
set1 = set()
for i in range(len(lst_1)):
    if lst_1[i] not in set1:
        set1.add(lst_1[i])
print(lst_1,  "Removed duplicate" , set1)
