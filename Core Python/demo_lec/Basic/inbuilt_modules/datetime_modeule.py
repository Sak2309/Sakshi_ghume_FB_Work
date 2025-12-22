import datetime

res = datetime.datetime.now()
print (res)

res = datetime.datetime.now()
res= res+ datetime.timedelta(days = 7)
print (res)

res = datetime.datetime.strptime('19-12-2025','%d-%m-%Y')
print(res)

res = datetime.datetime.strftime(res,'%d/%m/%Y')
print(res)

res = datetime.datetime.today()
print(res)

res = datetime.time(10,53,9)
print(res)