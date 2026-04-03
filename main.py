import matplotlib.pyplot as plt
from price_controls import apply_ceiling, apply_floor, get_price_control

# Qd formula = a - bP
# Qs formula = c + dP

def demand_curve_inputs():
    # Ask user for demand curve values and return them
    print("Enter the values for the demand curve using the formula Qd = a - bP")
    a = float(input("Enter demand constant a: \n"))
    b = float(input("Enter demand coefficient b: \n"))
    return a, b


def supply_curve_inputs():
    # Ask user for supply curve values and return them
    print("Enter the values for the supply curve using the formula Qs = c + dP")
    c = float(input("Enter supply constant c: \n"))
    d = float(input("Enter supply coefficient d: \n"))
    return c, d


def calculate_equilibrium(a, b, c, d):
    # Set Qd = Qs and solve for price
    price = (a - c) / (b + d)
    # Plug price back into demand equation to get quantity
    quantity = a - b * price
    return price, quantity


def display_equilibrium(price, quantity):
    # Print the equilibrium results neatly
    print("\nMarket Equilibrium values: ")
    print(f"Equilibrium Price: R{price:.2f}")
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

def plot_market(a, b, c, d, price, quantity):
    # Create empty lists which will be appended 
    prices = []
    demand = []
    supply = []

    # Generate price values. Double it and add some padding
    for i in range(0, int(price*2)+ 10):
        prices.append(i)

        # Calculate demand and supply at this price
        demand_quantity = a - b * i
        supply_quantity = c + d * i

        demand.append(demand_quantity)
        supply.append(supply_quantity)

            # Plot demand curve
    plt.plot(demand, prices, label="Demand", color="#1f77b4",linewidth=2)

    # Plot supply curve
    plt.plot(supply, prices, label="Supply", color="green", linewidth=2)

    # Plot equilibrium point
    plt.scatter(quantity, price, color="red", label="Equilibrium", s=100, edgecolor="black")

    # Labels and title
    plt.xlabel("Quantity", labelpad=10)
    plt.ylabel("Price", labelpad=10)
    plt.title("Market Equilibrium", pad=25)

    # Legend and grid
    plt.legend()
    plt.grid(True)

    # Show graph
    plt.show()


def main():
    # Get demand and supply inputs from user
    a, b = demand_curve_inputs()
    c, d = supply_curve_inputs()

    # Calculate and display equilibrium
    price, quantity = calculate_equilibrium(a, b, c, d)
    display_equilibrium(price, quantity)

    # Ask for a test price and check market condition
    test_price = float(input("\nEnter a price to test: \n"))
    qd, qs = test_marketprice(a, b, c, d, test_price)
    check_market_condition(qd, qs)
    plot_market(a, b, c, d, price, quantity)

    # Price controls
    choice, control_price = get_price_control()
    if choice == "1":
        apply_ceiling(a, b, c, d, price, control_price)
    elif choice == "2":
        apply_floor(a, b, c, d, price, control_price)
    else:
        print("Invalid choice.")


main()
