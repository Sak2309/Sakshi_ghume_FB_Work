import random
res= random.randint(1,6)
print(res)

res = random.uniform(1.0,10.0)
print(res)

li =[1,2,3,4,5,6]
sample= random.sample(li,2)
print(sample)

shuffle= random.shuffle(li)
print(li)

choice= random.choice(li)
print(choice)

random.seed(19)
res= random.randint(1,100)
print(res)

