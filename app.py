import csv

with open("employees.csv", "r") as file:
    employees = csv.DictReader(file)

    for employee in employees:
        print(
            employee["id"],
            employee["name"],
            employee["department"],
            employee["salary"]
        )

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


employee_id = input("Enter Employee ID: ")
search_employee(employee_id)