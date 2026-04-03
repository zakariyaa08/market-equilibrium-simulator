def apply_ceiling(a, b, c, d, eq_price, ceiling_price):
    qd = a - b * ceiling_price
    qs = c + d * ceiling_price

    if ceiling_price >= eq_price:
        print("Non-binding")
    else:
        shortage = qd - qs
        print(f"Price Ceiling at R{ceiling_price:.2f}")
        print(f"Quantity demanded: {qd:.2f} units")
        print(f"Quantity supplied: {qs:.2f} units")
        print(f"Shortage: {shortage:.2f} units")

def apply_floor(a, b, c, d, eq_price, floor_price):
    qd = a - b * floor_price
    qs = c + d * floor_price

    if floor_price <= eq_price:
        print("Non binding")

    else: 
        surplus = qs - qd
        print(f"Price Floor at R{floor_price:.2f}")
        print(f"Quantity demanded: {qd:.2f} units")
        print(f"Quantity supplied: {qs:.2f} units")
        print(f"Surplus: {surplus:.2f} units")


def get_price_control():
    print("Price Controls: ")
    print("1. Price Ceiling")
    print("2. Price Floor")
    choice = input("Choose 1 or 2: \n")
    control_price = float(input("Enter the control price: \n"))
    return choice, control_price


        