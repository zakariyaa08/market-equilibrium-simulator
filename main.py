# Qd formula = a - bP

a = float(input("Enter demand constant a: "))
b = float(input("Enter demand coefficient b: "))

# Qs formula = c - dP
c = float(input("Enter supply constant c: "))
d = float(input("Enter supply coefficient d: "))


# Equilibrium: a - bP = c + dP
# Rearranging gives:
# P = (a - c) / (b + d)
price = (a - c) / (b + d)

# Plug in to find quantity 
quantity = a - b * price

print("Market Equilibrium values --")
print(f"Equilibrium Price: R{price}")
print(f"Equilibrium Quantity: R{quantity}")


# Work out shortages and surpluses
test_price = float(input("Enter a market price to test: \n"))

# Same Qd and Qs formulas but now with a price value
qd = a - b * test_price
qs = c + d * test_price

# Set conditions and check
if qd == qs:
    print("The market is in equilibiruim.")
elif qd > qs:
    shortage = qd -qs
    print(f"There is a shortage of {shortage} units.")
else:
    surplus = qs - qd
    print(f"There is a surplus of {surplus} units.")

