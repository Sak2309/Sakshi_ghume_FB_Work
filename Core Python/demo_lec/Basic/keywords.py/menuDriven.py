ch = 0
while( ch != '7' ):
    print('''please selsect your option :
          1. ADDITION
          2.SUBTRACTION
          3.MULTIPLICATION
          4.EVEN OR ODD NUMBER
          5.POSITIVE OR NEGATIVE NUMBER
          6.CHECK PRIME OR NOT NUMBER
          7.exit
          .....''')
    ch = input("ENTER YOUR CHOICE : ")
    if(ch == '1'):
        print("########ADDITION OPERTAION##########")
        n1 = int(input("ENTER THE VALUE OF NUM 1 :"))
        n2 = int(input("ENTER THE VALUE OF NUM 2 :"))
        sum = n1 + n2
        print(f" ADDITION OF TWO NUMBER {n1} and {n2} is = {sum}")

    elif( ch == '2'):
        print(f"########SUBTRACTION OPERTAION##########")
        n1 = int(input("ENTER THE VALUE OF NUM 1 :"))
        n2 = int(input("ENTER THE VALUE OF NUM 2 :"))
        sub = n1 - n2
        print(f"SUBTRACTION OF TWO NUMBER {n1} and {n2} is = {sub}")

    elif( ch == '3'):
        print(f"########MULTIPLICATION OPERTAION##########")
        n1 = int(input("ENTER THE VALUE OF NUM 1 :"))
        n2 = int(input("ENTER THE VALUE OF NUM 2 :"))
        mul = n1 * n2
        print(f"SUBTRACTION OF TWO NUMBER {n1} and {n2} is = {mul}")
    elif( ch == '4'):
        print(f"###### EVEN ODD NUMBER OPERTAION##########")
        n = int (input("ENTER THE NUMBER TO CHECK THE EVEN OR ODD NUMBER : "))
        if(n %2 == 0 ):
            print(f"{n} is EVEN NUMBER.")
        else:
            print(f"{n} is ODD NUMBER.")
    elif( ch == '5'):
        print(print(f"######## CHECK THE PRIME NUMBER OR NOT OPERTAION##########"))



              
    else:
        print(f"INVALID CHOICE.")
            
