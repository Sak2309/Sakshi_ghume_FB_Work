n = int(input("Enter the number : "))
temp = n

print(f"before reverse number : {temp}")

d1 = temp % 10
temp = temp // 10
d2 = temp % 10
temp = temp // 10
d3 = temp % 10
temp = temp // 10
rev = d1 * 100 + d2 * 10 + d3
print(f"After the reverse number = {rev}")
if( rev == rev):
    print(f"PALINDER NUMBER.")
else:
    print(f"NOT PALINDER NUMBER.")

