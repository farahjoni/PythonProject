class PyATB:

    name = None
    ID = None
    address = None
    age = None
    phone_number = None

    def __init__(self,name,ID,address,age,phone_number):
        self.name = name
        self.ID = ID
        self.address = address
        self.age = age
        self.phone_number = phone_number

    def student_info(self):
        print(f"Name is {self.name}", f"ID is {self.ID}", f"Address is {self.address}",
            f"Age is {self.age}", f"Phone number is {self.phone_number}")


student1 = PyATB("Jony J", "007", "MK11", "77", "01010101")
student2 = PyATB("Cage J", "001", "MK10", "55", "02020202")

student2.student_info()



