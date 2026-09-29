# Employee Salary Calculator 💰

A simple beginner-friendly Python project that calculates an employee's salary based on their basic salary, HRA, DA, and tax deduction.

## 📌 Project Description

The Employee Salary Calculator takes employee details and basic salary as input, calculates the gross salary, applies a simple tax rule, and displays the final net salary as a salary slip.

This project was created to practice basic Python programming concepts.

## ✨ Features

* Enter employee name
* Enter employee ID
* Enter basic salary
* Calculate HRA (20%)
* Calculate DA (10%)
* Calculate gross salary
* Calculate tax deduction
* Calculate net salary
* Display a formatted salary slip

## 🛠️ Technologies Used

* Python 3

## 🧠 Python Concepts Used

* `input()`
* `print()`
* Variables
* Data types
* `float()`
* Arithmetic operators
* `if / elif / else`
* f-strings
* Number formatting

## 📊 Salary Calculation

### HRA

HRA is calculated as 20% of the basic salary.

```text
HRA = Basic Salary × 20%
```

### DA

DA is calculated as 10% of the basic salary.

```text
DA = Basic Salary × 10%
```

### Gross Salary

```text
Gross Salary = Basic Salary + HRA + DA
```

### Tax

```text
Gross Salary ≤ ₹30,000 → 0% Tax

₹30,000 < Gross Salary ≤ ₹50,000 → 5% Tax

Gross Salary > ₹50,000 → 10% Tax
```

### Net Salary

```text
Net Salary = Gross Salary - Tax
```

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

### 2. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 3. Open the project folder

```bash
cd employee-salary-calculator
```

### 4. Run the Python program

```bash
python employee_salary_calculator.py
```

## 💻 Example

```text
====================================
       EMPLOYEE SALARY CALCULATOR
====================================

Enter Employee Name: Rahul
Enter Employee ID: EMP101
Enter Basic Salary: ₹40000

====================================
             SALARY SLIP
====================================

Employee Name : Rahul
Employee ID   : EMP101
------------------------------------
Basic Salary  : ₹40,000.00
HRA (20%)     : ₹8,000.00
DA (10%)      : ₹4,000.00
Gross Salary  : ₹52,000.00
Tax Deduction : ₹5,200.00
------------------------------------
Net Salary    : ₹46,800.00
====================================
```

## 🔮 Future Improvements

Some features that can be added later:

* Bonus calculation
* PF deduction
* Overtime salary
* Department selection
* Multiple employee records
* Save salary records to CSV
* Generate salary reports
* Add a graphical user interface (GUI)

## 👨‍💻 Author

**Jeya Jeev**

This project is part of my Python learning journey.
