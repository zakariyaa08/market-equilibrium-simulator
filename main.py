# Qd formula = a - bP
# Qs formula = c + dP

def demand_curve_inputs():
    # Ask user for demand curve values and return them
    print("Enter the values for the demand curve using the formula Qd = a - bP")
    a = float(input("Enter demand constant a: "))
    b = float(input("Enter demand coefficient b: "))
    return a, b


def supply_curve_inputs():
    # Ask user for supply curve values and return them
    print("Enter the values for the supply curve using the formula Qs = c + dP")
    c = float(input("Enter supply constant c: "))
    d = float(input("Enter supply coefficient d: "))
    return c, d


def calculate_equilibrium(a, b, c, d):
    # Set Qd = Qs and solve for price
    price = (a - c) / (b + d)
    # Plug price back into demand equation to get quantity
    quantity = a - b * price
    return price, quantity


def display_equilibrium(price, quantity):
    # Print the equilibrium results neatly
    print("\nMarket Equilibrium values --")
    print(f"Equilibrium Price:    R{price:.2f}")
    print(f"Equilibrium Quantity: {quantity:.2f} units")


def test_marketprice(a, b, c, d, test_price):
    # Calculate Qd and Qs at the given test price
    qd = a - b * test_price
    qs = c + d * test_price
    return qd, qs


def check_market_condition(qd, qs):
    # Compare Qd and Qs to find shortage, surplus, or equilibrium
    if qd == qs:
        print("The market is in equilibrium.")
    elif qd > qs:
        shortage = qd - qs
        print(f"There is a shortage of {shortage:.2f} units.")
    else:
        surplus = qs - qd
        print(f"There is a surplus of {surplus:.2f} units.")


def main():
    # Get demand and supply inputs from user
    a, b = demand_curve_inputs()
    c, d = supply_curve_inputs()

    # Calculate and display equilibrium
    price, quantity = calculate_equilibrium(a, b, c, d)
    display_equilibrium(price, quantity)

    # Ask for a test price and check market condition
    test_price = float(input("\nEnter a price to test: "))
    qd, qs = test_marketprice(a, b, c, d, test_price)
    check_market_condition(qd, qs)


main()
