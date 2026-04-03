def calculate_ped(p1, q1, p2,q2):

    # PED formula: (Change in Q over the Midpoint of Q) divided by (Change in P over Midpoint of P)
    midpoint_q = (q1 + q2) / 2
    midpoint_p = (p1 + p2) / 2
    change_q = q2 - q1
    change_p = p2 - p1

    ped = (change_q / midpoint_q) / (change_p / midpoint_p)

    return ped


def interpret_ped(ped):
    
    if abs(ped) > 1:
        print(f"The PED is {abs(ped):.2f} therefore it is elastic")
    elif abs(ped) == 1:
        print("PED is 1 therefore it is unit elastic")
    else:
        print(f"PED is {abs(ped):.2f} therefore it is inelastic")

def get_elasticity_inputs():
    print("Add the values which you would like to check")

    p1 = float(input("Enter a value for p1: \n"))
    q1 = float(input("Enter a value for q1: \n"))
    p2 = float(input("Enter a value for p2: \n"))
    q2 = float(input("Enter a value for q2: \n"))

    return p1, q1, p2, q2