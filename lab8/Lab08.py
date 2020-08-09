import employee
import parttime


def print_beauty(lst):
    for item in lst:
        print(item)


employees = [
    employee.Employee("Evren Kilic", "51642", 275000),
    parttime.PartTime("Zana Zengin", "12345", 650, 45),
    employee.Employee("Ayse Kilic", "98765", 315000),
    parttime.PartTime("Anisa Nalan", "64276", 475, 20)
]

print("Original List: ")
print_beauty(employees)

print("\nSorted List: ")
employees.sort()
print_beauty(employees)

total_parttime_salary = 0
number_of_parttime = 0

print("\nSalary of all employees")
for emp in employees:
    print("{0} salary after tax: {1}".format(emp.get_empName(), emp.calculate_salary()))
    if isinstance(emp, parttime.PartTime):
        number_of_parttime += 1
        total_parttime_salary += emp.calculate_salary()

print("\nAverage Salary for PartTime Employees: {0}".format(total_parttime_salary / number_of_parttime))
