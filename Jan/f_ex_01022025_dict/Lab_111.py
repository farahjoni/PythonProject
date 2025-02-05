
string = input("Enter a string: ")

char_count={}

for i in string:
    char_count[i] = char_count.get(i,0) + 1
print(char_count)



