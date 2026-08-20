import csv

# 1. EXISTING EMPLOYEE DISPLAY____________________

with open("employees.csv", "r") as file:
    employees = csv.DictReader(file)

    for employee in employees:
        print(
            employee["id"],
            employee["name"],
            employee["department"],
            employee["salary"]
        )

# 2. SEARCH EMPLOYEE FEATURE____________________

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

# 3. ADD EMPLOYEE FEATURE____________________

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

# 4. EMPLOYEE DELETE FEATURE____________________

def delete_employee(employee_id):
    employees = []

    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)

        for employee in reader:
            employees.append(employee)

    found = False

    for employee in employees:
        if employee["id"] == employee_id:
            employees.remove(employee)
            found = True
            break

    if not found:
        print("\nEmployee not found")
        return

    with open("employees.csv", "w", newline="") as file:
        fieldnames = ["id", "name", "department", "salary"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(employees)

    print("\nEmployee deleted successfully")

# 5. EMPLOYEE UPDATE FEATURE____________________

def update_employee(employee_id):
    employees = []
    found = False

    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)

        for employee in reader:
            if employee["id"] == employee_id:
                found = True

                print("\nCurrent Employee Details")
                print("Name:", employee["name"])
                print("Department:", employee["department"])
                print("Salary:", employee["salary"])

                employee["name"] = input("Enter new name: ")
                employee["department"] = input("Enter new department: ")
                employee["salary"] = input("Enter new salary: ")

            employees.append(employee)

    if not found:
        print("\nEmployee not found")
        return

    with open("employees.csv", "w", newline="") as file:
        fieldnames = ["id", "name", "department", "salary"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(employees)

    print("\nEmployee updated successfully")


##### PROGRAM MENU ---------- SABSE NEECHE #####

choice = input(
    "Enter 1 to Search Employee, 2 to Add Employee, "
    "3 to Delete Employee or 4 to Update Employee: "
)

if choice == "1":
    employee_id = input("Enter Employee ID: ")
    search_employee(employee_id)

elif choice == "2":
    add_employee()

elif choice == "3":
    employee_id = input("Enter Employee ID to delete: ")
    delete_employee(employee_id)

elif choice == "4":
    employee_id = input("Enter Employee ID to update: ")
    update_employee(employee_id)

else:
    print("Invalid choice")