
num1=int(input("Enter first num: "))
num2=int(input("Enter second num: "))
num3=int(input("Enter third num: "))

def sum_of_three_num(n1 = 100, n2 = 200, n3 = 300):
    return n1+n2+n3

sum=sum_of_three_num(num1,num2,num3)
print(sum)

sum2=sum_of_three_num()
print(sum2)