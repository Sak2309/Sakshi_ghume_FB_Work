def area_Rectangle(length,breath):

    area_rectangle = length * breath
    return area_rectangle

    
l = int(input("ENTER THE LENGTH OF RECTANGLE : "))
b = int (input("ENTER THE BREATH OF RECTANGLE : "))    
res =area_Rectangle(l,b)
print(f" RECTANGLE of LENGTH IS {l} and BREATH IS {b} THE AREA OF RECTANGLE IS :",res)
