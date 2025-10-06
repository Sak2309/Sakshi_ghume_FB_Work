# Enterv the values

f_days = int(input("Enter the days : "))

#perfrome opertion

year = f_days // 365

week_days = f_days % 365

no_of_week = week_days // 7

remaing_days = week_days % 7

#Display result

print(f"In {f_days} years are {year}, weeks are {no_of_week}, week days are {week_days} and the total remaing days are {remaing_days}")

#Enter the days : 1000
#In 1000 years are 2 ,weeks are 38, week days are 270 and the total remaing days are 4