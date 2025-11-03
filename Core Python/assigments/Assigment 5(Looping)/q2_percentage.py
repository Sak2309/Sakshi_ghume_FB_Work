
n_stud = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n_stud + 1):
    print("\nEnter marks of 5 subjects for student {i}")
    
    total_marks = 0
    
    for j in range(1, 6):
        marks = float(input(f"Enter marks for subject {j}: "))
        total_marks += marks  
    

    percentage = (total_marks / 500) * 100
    print(f"Percentage of student { i} = {percentage}")
    
    total_percentage += percentage


average_percentage = total_percentage / n_stud

print("\nAverage percentage of all students = {average_percentage} ")
