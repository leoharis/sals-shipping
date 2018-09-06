def ground_shipping_cost(weight):
    if weight <= 2:
        return 20.00 + (1.50 * weight)
    elif 2 < weight <= 6:
        return 20.00 + (3.00 * weight)
    elif 6 < weight <= 10:
        return 20.00 + (4.00 * weight)
    else:
        return 20.00 + (4.75 * weight)


print("$%.2f" % ground_shipping_cost(8.4))

premium_ground_shipping_cost = 125.00


def drone_shipping_cost(weight):
    if weight <= 2:
        return 0.00 + (4.50 * weight)
    elif 2 < weight <= 6:
        return 0.00 + (9.00 * weight)
    elif 6 < weight <= 10:
        return 0.00 + (12.00 * weight)
    else:
        return 0.00 + (14.25 * weight)


print("$%.2f" % drone_shipping_cost(1.5))


def cheapest_shipping(weight):
    if (ground_shipping_cost(weight) < drone_shipping_cost(weight)) and (
            ground_shipping_cost(weight) < premium_ground_shipping_cost):
        print("The cheapest shipping method is by ground shipping at a cost of " + str(
            "$%.2f" % ground_shipping_cost(weight)))
    elif (drone_shipping_cost(weight) < ground_shipping_cost(weight)) and (
            drone_shipping_cost(weight) < premium_ground_shipping_cost):
        print("The cheapest shipping method is by drone shipping at a cost of " + str(
            "$%.2f" % drone_shipping_cost(weight)))
    else:
        print("The cheapest shipping method is by premium ground shipping at a cost of " + str(
            "$%.2f" % premium_ground_shipping_cost))


cheapest_shipping(4.8)
cheapest_shipping(41.5)
