amount = float(input("Enter total shopping amount: "))
if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = amount * 0.05
print("Discount =", discount)
print("Final Amount =", amount - discount)
