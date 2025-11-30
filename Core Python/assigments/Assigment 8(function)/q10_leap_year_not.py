def leap_Year(y):
    if(y % 4 == 0):
        print(f"{y} year  leap by divisuble by 4")
    else:
        print (f" not leap year and not divisible by 4")
        if(y % 100 == 0):
            print(f"{y} year  leap by divisuble by 100")
        else:
            print (f" not leap year and not divisible by 100")
        if(y % 400 == 0):
                print(f"{y} year is leap year divisible by 400")
        else:
            print (f" not leap year and not divisible by 400")
            
y = int(input("enter the year to cheak leap year or not  : "))
leap_Year(y)

