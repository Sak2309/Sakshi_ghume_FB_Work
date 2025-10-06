a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

x = (-b  + ( b ** 2 - 4 * a * c )**0.5) / 2 * a
y = (-b  - ( b ** 2 - 4 * a * c )**0.5) / 2 * a

print(f"the required roots are x is {x} and y is {y} ")

