# Employee Salary Calculator

print("====================================")
print("       EMPLOYEE SALARY CALCULATOR")
print("====================================")

# Get employee details
name = input("Enter Employee Name: ")
employee_id = input("Enter Employee ID: ")
basic_salary = float(input("Enter Basic Salary: ₹"))

# Calculate HRA and DA
hra = basic_salary * 0.20
da = basic_salary * 0.10

# Calculate Gross Salary
gross_salary = basic_salary + hra + da

# Calculate tax based on salary
if gross_salary <= 30000:
    tax = 0
elif gross_salary <= 50000:
    tax = gross_salary * 0.05
else:
    tax = gross_salary * 0.10

# Calculate Net Salary
net_salary = gross_salary - tax

# Display Salary Slip
print("\n====================================")
print("             SALARY SLIP")
print("====================================")

print(f"Employee Name : {name}")
print(f"Employee ID   : {employee_id}")

print("------------------------------------")
print(f"Basic Salary  : ₹{basic_salary:,.2f}")
print(f"HRA (20%)     : ₹{hra:,.2f}")
print(f"DA (10%)      : ₹{da:,.2f}")
print(f"Gross Salary  : ₹{gross_salary:,.2f}")
print(f"Tax Deduction : ₹{tax:,.2f}")
print("------------------------------------")
print(f"Net Salary    : ₹{net_salary:,.2f}")
print("====================================")