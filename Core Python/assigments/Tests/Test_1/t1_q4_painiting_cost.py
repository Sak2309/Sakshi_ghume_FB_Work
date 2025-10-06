
l = int(input(" Enter the value of length : "))
b = int(input(" Enter the value of breath : "))

interior_cost= int(input(" Enter the value of interior cost : "))
exterior_cost= int(input(" Enter the value of exterior cost: "))

interior_area = l * b
exterior_area= l * b

Total_interior_cost = interior_area * interior_cost
Total_exterior_cost = exterior_area * exterior_cost

Total_painting_cost = Total_interior_cost + Total_exterior_cost 

print(f"Interior area = {interior_area} , Exterior area = {exterior_area}")
print(f"Total interior cost = {Total_interior_cost} , Total exterior cost = {Total_exterior_cost}")
print(f"Total painting cost = {Total_painting_cost}")

#Enter the value of length : 100
#Enter the value of breath : 10
#Enter the value of interior cost : 20000
#Enter the value of exterior cost: 30000
#Interior area = 1000 , Exterior area = 1000
#Total interior cost = 20000000 , Total exterior cost = 30000000
#Total painting cost = 50000000
