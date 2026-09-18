""" Exercise 1 """
points = 50
points_gained = 10
points_lost = 5

final_score = points + points_gained - points_lost
print(final_score)

""" Exercise 2 """
recipe_serves = 4
num_eggs = 2
cheese_ounces = 4
num_guests = 6

required_eggs = (num_eggs / recipe_serves) * num_guests
required_cheese = (cheese_ounces / recipe_serves) * num_guests

print(required_eggs)
print(required_cheese)

""" Exercise 3 """
total_budget = 500
daily_cost = 45
trip_length = 7

remaining_budget = total_budget - (daily_cost * trip_length)
print(remaining_budget)

""" Exercise 4 """
def calculate_price(cost, tip):
    total = cost + (cost * tip)
    return total

print(calculate_price(50.0, 0.15))

""" Exercise 5 """
def calculate_change(purchase_price, amount_paid):
    change = amount_paid - purchase_price
    return change

print(calculate_change(17.50, 20.00))

""" Exercise 6 """
def minutes_til_midnight(hour, minute):
    current_total_minutes = (hour * 60) + minute
    total_day_minutes = 24 * 60
    minutes_left = total_day_minutes - current_total_minutes
    return minutes_left

print(minutes_til_midnight(15, 30))

""" Exercise 7 """
def apply_discount(price, discount):
    return price - (price * discount)

def apply_tax(price, sales_tax):
    return price + (price * sales_tax)

def final_price(price, discount, sales_tax):
    discounted_price = apply_discount(price, discount)
    total_cost = apply_tax(discounted_price, sales_tax)
    return total_cost

print(final_price(85, 0.15, 0.08))