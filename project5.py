def smart_input(prompt):
    """Automatically detects and converts user input to int, float, or string."""
    value = input(prompt)

    if value.isdigit():
        return int(value)

    try:
        return float(value)
    except:
        return value

def safe_int(prompt):
    """Safely reads an integer from the user and prevents program crashes."""
    while True:
        try:
            return int(input(prompt))
        except:
            print("Invalid input. Please enter a number.")

def safe_float(prompt):
    """Safely reads a float value from the user and prevents program crashes."""
    while True:
        try:
            return float(input(prompt))
        except:
            print("Invalid input. Please enter a valid number.")

class Person:
    """Represents a basic person with name and age"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):
    """Represents an employee with ID and salary"""

    def __init__(self, name="", age=0, emp_id="", salary=0):
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary

    def __del__(self):
        print("Employee resources freed.")

    def get_id(self):
        return self.__emp_id

    def set_id(self, eid):
        self.__emp_id = eid

    def get_salary(self):
        return self.__salary

    def set_salary(self, sal):
        self.__salary = sal

    def display(self):
        super().display()
        print("Employee ID:", self.__emp_id)
        print("Salary:", self.__salary)

class Manager(Employee):
    """Represents a manager with department"""

    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)

class Developer(Employee):
    """Represents a developer with programming language"""

    def __init__(self, name, age, emp_id, salary, language):
        super().__init__(name, age, emp_id, salary)
        self.language = language

    def display(self):
        super().display()
        print("Programming Language:", self.language)



people_list = []




while True:

    print("\n--- Python OOP Project: Employee Management System ---")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show ALL Details")
    print("5. Show Specific Details")
    print("6. Exit")

    choice = safe_int("Enter your choice: ")

    if choice == 1:

        name = smart_input("Enter Name: ")
        age = safe_int("Enter Age: ")

        person = Person(name, age)
        people_list.append(person)

        print("\nPerson created with name:", name, "and age:", age)

    elif choice == 2:

        name = smart_input("Enter Name: ")
        age = safe_int("Enter Age: ")
        eid = smart_input("Enter Employee ID: ")
        salary = safe_float("Enter Salary: ")

        employee = Employee(name, age, eid, salary)
        people_list.append(employee)

        print("\nEmployee created with name:", name,
              ", age:", age,
              ", ID:", eid,
              ", and salary:", salary)

    elif choice == 3:

        name = smart_input("Enter Name: ")
        age = safe_int("Enter Age: ")
        eid = smart_input("Enter Employee ID: ")
        salary = safe_float("Enter Salary: ")
        dept = smart_input("Enter Department: ")

        manager = Manager(name, age, eid, salary, dept)
        people_list.append(manager)

        print("\nManager created with name:", name,
              ", age:", age,
              ", ID:", eid,
              ", salary:", salary,
              ", and department:", dept)

    elif choice == 4:

        if not people_list:
            print("No data available.")
        else:
            print("\n--- All Stored Objects ---")
            for obj in people_list:
                print("\nDetails:")
                obj.display()

        print("\nInheritance Check:")
        print("Manager subclass of Employee:",
              issubclass(Manager, Employee))
        print("Developer subclass of Employee:",
              issubclass(Developer, Employee))

    elif choice == 5:

        print("\nChoose type to display:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        opt = safe_int("Enter your choice: ")

        found = False

        for obj in people_list:

            if opt == 1 and type(obj) == Person:
                obj.display()
                print()
                found = True

            elif opt == 2 and type(obj) == Employee:
                obj.display()
                print()
                found = True

            elif opt == 3 and type(obj) == Manager:
                obj.display()
                print()
                found = True

        if not found:
            print("No matching records found.")

    elif choice == 6:

        print("\nExiting the system. All resources have been freed.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
