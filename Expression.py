# Vat 7 %
p = float(input("Enter price with vat: "))
print("vat is", p * 7 / 107, "Baht") # p - (100*p/107)

# Selling price
import math
p = float(input("Enter price: "))
print("Selling price is", math.ceil(p * 1.07), "Baht")

# Circle vs square
R, L = input("Enter radius and length of side: ").split()
R, L = float(R), float(L)
print("This circle is larger than this square:", 3.14*R*R > L*L)

# month --> year
Name, M = input("Enter name and no. of months: ").split()
print(Name, "has used this product for", int(M) // 12, "year", int(M) % 12, "month.")

