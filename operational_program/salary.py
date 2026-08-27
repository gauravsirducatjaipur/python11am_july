# Salary calculator → Basic salary + HRA + DA – Tax.

basic_salary = int(input("Enter your basic salary "))
hra = basic_salary * 0.4
da = basic_salary * 0.2


gross_salary = basic_salary + hra + da
tax = gross_salary * 0.1

net_salary = gross_salary - tax

print("Your gross salary is", gross_salary)
print("Your net salary is", net_salary)
