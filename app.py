import csv
import re

# 0. EXISTING EMPLOYEE DISPLAY____________________

with open("employees.csv", "r") as file:
    employees = csv.DictReader(file)

    for employee in employees:
        print(
            employee["id"],
            employee["name"],
            employee["department"],
            employee["salary"]
        )

# 1. VIEW ALL EMPLOYEES FEATURE____________________
def view_all_employees():
    print("\nAll Employees")
    print("-" * 50)

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
    while True:
        employee_id = input("Enter Employee ID: ").strip()

        if not employee_id:
            print("\nEmployee ID cannot be empty")
            continue

        if not re.fullmatch(r"[A-Za-z0-9]+", employee_id):
            print("\nEmployee ID can contain only letters and numbers")
            continue

        break

    with open("employees.csv", "r") as file:
        employees = csv.DictReader(file)

        for employee in employees:
            if employee["id"] == employee_id:
                print("\nEmployee ID already exists")
                return

    while True:
        name = input("Enter Employee Name: ").strip()

        if not name:
            print("\nEmployee Name cannot be empty")
            continue

        if not re.fullmatch(r"[A-Za-z ]+", name):
            print("\nEmployee Name can contain only letters and spaces")
            continue

        break

    while True:
        department = input("Enter Department: ").strip()

        if not department:
            print("\nDepartment cannot be empty")
            continue

        if not re.fullmatch(r"[A-Za-z ]+", department):
            print("\nDepartment can contain only letters and spaces")
            continue

        break

    while True:
        salary = input("Enter Salary: ").strip()

        try:
            salary = float(salary)

            if salary < 0:
                print("\nSalary cannot be negative")
                continue

            break

        except ValueError:
            print("\nPlease enter a valid numeric salary")

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

                while True:
                    new_name = input("Enter new name: ").strip()

                    if not new_name:
                        print("\nEmployee Name cannot be empty")
                        continue

                    if not re.fullmatch(r"[A-Za-z ]+", new_name):
                        print("\nEmployee Name can contain only letters and spaces")
                        continue

                    break

                while True:
                    new_department = input("Enter new department: ").strip()

                    if not new_department:
                        print("\nDepartment cannot be empty")
                        continue

                    if not re.fullmatch(r"[A-Za-z ]+", new_department):
                        print("\nDepartment can contain only letters and spaces")
                        continue

                    break

                while True:
                    new_salary = input("Enter new salary: ").strip()

                    try:
                        new_salary = float(new_salary)

                        if new_salary < 0:
                            print("\nSalary cannot be negative")
                            continue

                        break

                    except ValueError:
                        print("\nPlease enter a valid numeric salary")

                employee["name"] = new_name
                employee["department"] = new_department
                employee["salary"] = new_salary

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

while True:
    choice = input(
        "\n1. View All Employees\n"
        "2. Search Employee\n"
        "3. Add Employee\n"
        "4. Delete Employee\n"
        "5. Update Employee\n"
        "6. Exit\n"
        "Enter your choice: "
    )

    if choice == "1":
        view_all_employees()

    elif choice == "2":
        employee_id = input("Enter Employee ID: ").strip()
        search_employee(employee_id)

    elif choice == "3":
        add_employee()

    elif choice == "4":
        employee_id = input("Enter Employee ID to delete: ").strip()
        delete_employee(employee_id)

    elif choice == "5":
        employee_id = input("Enter Employee ID to update: ").strip()
        update_employee(employee_id)

    elif choice == "6":
        print("\nThank you for using Employee Management System.")
        break

    else:
        print("\nInvalid choice. Please try again.")