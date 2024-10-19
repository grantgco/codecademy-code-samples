def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  print(split_price)

# Write your code below:

table_7_total = [534.50, 20.0, 5]

calculate_price_per_person(*table_7_total)

# Using the * or ** unpacking arguments, you can pass through items like above
# where there is a list of three items and a function that requires three
# arguments.  This can then pass the three arguments essentially as one.
