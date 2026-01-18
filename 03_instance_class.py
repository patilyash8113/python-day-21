# class Employee:
#     company="Asus" #This is class attribute
#     company2="amazon"
#     def __init__(self,salary,name,bond,company): # this is called instance attribute..
#        self.salary=salary #create a instance attribute of name salary and assign it with salary..
#        self.name=name
#        self.bond=bond
#        self.company=company

#     def get_salary(self):
#         return self.name
    
#     def get_info(self):
#         print(f"The num of the employee is {self.name}. salary of the employee is {self.salary}.And the of the employee with company is {self.bond}...")
# e1=Employee(3400,"yash",4,"tesla") 
# print(e1.company) #it will print instance attrubute if or whenever it present
# print(Employee.company) #this will always print class attribute..
# print(Employee.company2)



# #object introspection= "object introspection is basically a way to find all the methods that a particular object in python has."
# print(dir(e1))






class Employee:
    company="Asus"

    def __init__(self,salary,name,bond,company):
        self.salary=salary
        self.name=name
        self.bond=bond
        self.company=company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(F"the name of the employee is {self.name}.the salary of the employee is {self.salary}.the bond with employee in company is{self.bond}")
    
e1=Employee(3400,"yash",4,"Amazon")
print(e1.company)
print(Employee.company)