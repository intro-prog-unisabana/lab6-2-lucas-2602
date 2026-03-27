# Write your code here!
def employee_print(employee_info):
    name = employee_info.get("Name", "N/A")
    salary = employee_info.get("Salary", "N/A")
    role = employee_info.get("Role", "N/A")
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")
    employee_info.pop("Name")
    employee_info.pop("Salary")
    employee_info.pop("Role")
    if not employee_info:
        print("No other info!")
    else:
        for key, value in employee_info.items():
            print(f"{key}: {value}")