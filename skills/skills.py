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
