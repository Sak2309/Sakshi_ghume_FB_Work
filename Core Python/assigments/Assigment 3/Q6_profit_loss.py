sp = int(input("Enter the Selling price :"))
cp = int(input("Enter the cost price : "))

if (sp > cp ):
    profit = sp - cp
    print(f"profit={profit}")
    print(f" PROFIT by {profit} ")
elif(cp > sp):
    loss = cp - sp
    print(f"loss = {loss}")
    print(f"LOSS by {loss}  ")
else:
    print(f" NOT PROFIT OR LOSS")

#Enter the Selling price :1000
#Enter the cost price : 234
#profit=766
 #PROFIT by 766
 
 #Enter the Selling price :800
#Enter the cost price : 7000 
#loss = 6200
#LOSS by 6200

#Enter the Selling price :1000
#Enter the cost price : 1000
 #NOT PROFIT OR LOSS