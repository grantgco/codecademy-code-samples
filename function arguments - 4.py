tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)


# Write your code below:

def assign_food_items(**order_items):
    print(order_items)

    food = order_items.get("food")
    drinks = order_items.get("drinks")

    print(food)
    print(drinks)

# Example Call
assign_food_items(food='Pancakes, Poached Egg', drinks='Water')