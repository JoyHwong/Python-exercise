# hold information for pizza
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# introduce pizza
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
        "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

