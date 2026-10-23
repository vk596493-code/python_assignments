customer_name=input("Enter the name:")
amount = int(input("Enter the amount:"))
customer_type = input("customer type(regular/premium):").lower()
discount = 0
if amount >=5000:
    discount = amount * .20
elif amount >= 3000 and amount < 5000:
    discount = amount * .10
elif amount >=1000 and amount < 3000 :
    discount = amount * .5
else :
    discount = 0

if customer_type == "premium":
    discount = 


