import csv

# 1. Existing employee display
with open("employees.csv", "r") as file:
    employees = csv.DictReader(file)

    for employee in employees:
        print(
            employee["id"],
            employee["name"],
            employee["department"],
            employee["salary"]
        )

# 2. Search Employee Function
def search_employee(employee_id):
    with open("employees.csv", "r") as file:
        employees = csv.DictReader(file)

        for employee in employees:
            if employee["id"] == employee_id:
                print("\nEmployee Found")
                print("ID:", employee["id"])
                print("Name:", employee["name"])
                print("Department:", employee["department"])
                print("Salary:", employee["salary"])
                return

    print("\nEmployee not found")

# 3. Add Employee function
def add_employee():
    employee_id = input("Enter Employee ID: ")

    with open("employees.csv", "r") as file:
        employees = csv.DictReader(file)

        for employee in employees:
            if employee["id"] == employee_id:
                print("\nEmployee ID already exists")
                return

    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    with open("employees.csv", "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "name", "department", "salary"]
        )

        writer.writerow({
            "id": employee_id,
            "name": name,
            "department": department,
            "salary": salary
        })

    print("\nEmployee added successfully")

# 4. Program menu — SABSE NEECHE
choice = input("Enter 1 to Search Employee or 2 to Add Employee: ")

if choice == "1":
    employee_id = input("Enter Employee ID: ")
    search_employee(employee_id)

elif choice == "2":
    add_employee()

else:
    print("Invalid choice")
