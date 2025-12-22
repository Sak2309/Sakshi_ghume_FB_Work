def emp_Details():
    id = input("ENTER THE ID OF EMPOLYEE : ")
    name = input("ENTER THE NAME OF EMPOLYEE : ")
    sal= float(input("ENTER THE EMPOLYEE SALARY : "))

    data = f'ID:{id}\n e_NAME:{name}\n Salary:{sal}'
    return id,name,sal
result=emp_Details()
print(result)
    #return data
#print(emp_Details())