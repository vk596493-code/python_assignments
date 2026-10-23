Customer_Name = input("Enter the name:")
units = int(input("Enter the unit consumed:"))
service_charge = 150
if units <= 100:
  energy_charge = units * 3
elif units <= 200 :
  energy_charge = (100 * 3) + ((units - 100) * 5)
else :
   energy_charge = (100 * 3) + (100 * 5) + ((units - 200) * 7)

final_bills = energy_charge + service_charge
if final_bills >5000 :
  usage_message = "high usage bills"
else :
  usage_message="normal uses" 

print("\n-------eletricity bills-------")
print("Customer_name=",Customer_Name)
print("units consumed",units)
print("energy_charge=",energy_charge)
print(" service charge=",service_charge)
print("finals_bills",final_bills)
print("usage message",usage_message)
