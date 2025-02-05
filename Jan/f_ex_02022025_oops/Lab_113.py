class PyATB:

    name = None
    ID = None
    address = None
    age = None
    phone_number = None

    def __init__(self):
        self.name = input("Enter your name: ")
        self.ID = input("Enter your ID: ")
        self.address = input("Enter your address: ")
        self.age = input("Enter your age: ")
        self.phone_number = input("Enter your number: ")

    def student_info(self):
        print(f"Name is {self.name}", f"ID is {self.ID}", f"Address is {self.address}",
            f"Age is {self.age}", f"Phone number is {self.phone_number}")

student1 = PyATB()

student1.student_info()




