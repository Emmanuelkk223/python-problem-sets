fruit_list = [
    {'fruit': 'Apple', 'calories': 130},
    {'fruit': 'Avocado', 'calories': 50},
    {'fruit': 'Banana', 'calories': 110},
    {'fruit': 'Cantaloupe', 'calories': 50},
    {'fruit': 'Grapefruit', 'calories': 60},
    {'fruit': 'Grapes', 'calories': 90},
    {'fruit': 'Honeydew melon', 'calories': 50},
    {'fruit': 'Kiwifruit', 'calories': 90},
    {'fruit': 'Lemon', 'calories': 15},
    {'fruit': 'Lime', 'calories': 20},
    {'fruit': 'Nectarine', 'calories': 60},
    {'fruit': 'Orange', 'calories': 80},
    {'fruit': 'Peach', 'calories': 60},
    {'fruit': 'Pear', 'calories': 100},
    {'fruit': 'Pineapple', 'calories': 50},
    {'fruit': 'Plums', 'calories': 70},
    {'fruit': 'Strawberries', 'calories': 50},
    {'fruit': 'Sweet cherries', 'calories': 100},
    {'fruit': 'Tangerine', 'calories': 50},
    {'fruit': 'Watermelon', 'calories': 80}
]

fruit = input('Item: ').capitalize()
found = False

for nutrition in fruit_list:
    if fruit == nutrition['fruit']:
        print('Calories:', nutrition['calories'])
        found = True
        break

if not found:
    print(f"{fruit} is not in the list.")
