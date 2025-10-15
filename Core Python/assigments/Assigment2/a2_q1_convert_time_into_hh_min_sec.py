
hr = int (input("Enter the hours : "))
sec= hr
sec = sec % (24 * 3600)
hr = sec //3600
sec %=3600
min = sec // 60
sec %=60

print(f" miniutes = {min} and sec = {sec} hours ={hr}")

#Enter the hours : 10000
 #miniutes = 46 and sec = 40 hours =2

 #Enter the hours : 12345
 #miniutes = 25 and sec = 45 hours =3
