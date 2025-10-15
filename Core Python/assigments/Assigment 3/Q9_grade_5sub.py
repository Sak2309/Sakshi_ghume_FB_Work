num1= int(input("enter the num1 marks : "))
num2= int(input("enter the num2 marks : "))
num3= int(input("enter the num3 marks : "))
num4= int(input("enter the num4 marks : "))
num5= int(input("enter the num5 marks : "))

values=num1+num2+num3+num4+num5

print(f'gain_marks = {values}')
percentage=(values/500) * 100

print(f'percentage is {percentage}%')

if(percentage >=90):
    print(f"FRIST CLASS")
elif(percentage >=70):
    print(f"SECOND CLASS")
elif(percentage >= 50):
    print(f"PASS")
else:
    print(f"FAILL")