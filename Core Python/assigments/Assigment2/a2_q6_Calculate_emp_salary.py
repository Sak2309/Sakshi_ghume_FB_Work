basic_sal = int (input("Enter the value of basic salary of emplyee : "))

#10% = 10/100 = 0.10
DA = basic_sal * 0.10
TA = basic_sal * 0.12
HRA = basic_sal * 0.15

Total_sal = basic_sal + DA + TA + HRA

print(f"The DA = {DA}, TA = {TA}, HRA = {HRA} are The total salary of employee is {Total_sal}")

#Enter the value of basic salary of emplyee : 20000
#The DA = 2000.0, TA = 2400.0, HRA = 3000.0 are The total salary of employee is 27400.0
