print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give?(eg: 12) "))
x = int(input("How many people to split the bill? "))

result = float((bill/x) * (1+(tip/100)))
result = round(result,2)

print(f"Each person should pay: ${result}")
