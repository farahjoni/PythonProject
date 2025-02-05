

grade = int(input("Please enter grade: "))

if grade >= 90 and grade <=100:
    print("You got A!")
elif grade >= 80 and grade <90:
    print("You got B!")
elif grade >= 70 and grade <80:
    print("You got C!")
elif grade >= 60 and grade < 70:
    print("You got D!")
else:
    print("You Failed!")
