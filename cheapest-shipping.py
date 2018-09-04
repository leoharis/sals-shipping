def ground_shipping(weight):
    if weight <= 2:
        return 20 + (1.50 * weight)
    elif 2 < weight <= 6:
        return 20 + (3.00 * weight)
    elif 6 < weight <= 10:
        return 20 + (4.00 * weight)
    else:
        return 20 + (4.75 * weight)


print("$%.2f" % ground_shipping(8.4))
