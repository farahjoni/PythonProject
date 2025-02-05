list = [1,1,1,2,2,3,4,3,4]
#remove duplicates by using list
unique_list = set()

for i in list:
    if i not in unique_list:
        unique_list.add(i)
print(unique_list)



