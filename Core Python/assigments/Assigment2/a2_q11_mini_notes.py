amount_1= int(input("enter amount : "))

amount=amount_1
#2000
two_th= amount//2000
print(two_th)
#500
amount=amount%2000
five_hun=amount//500
print(five_hun)
#200
amount=amount%500
two_hun=amount//200
print(two_hun)
#100
amount=amount%200
one_hun=amount//100
print(one_hun)
#50
amount=amount%100
fifty_rs=amount//50
print(fifty_rs)
#20
amount=amount%50
twenty=amount//20
print(twenty)
#10
amount=amount%20
ten=amount//10
print(ten)

print(f'In rs {amount_1} there are{two_th} notes of 2000/-,{five_hun} notes of 500/-,{two_hun} notes of 200/-,{one_hun}notes of 100/- ,{fifty_rs}notes of 50/-,{twenty}notes of 20/-,{ten} notes of 10/-  ')
