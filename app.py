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