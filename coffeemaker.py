MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

revenue = 0


def askforOrder():
    print("What would you like? (espresso/latte/cappuccino): ")
    coffee = input()
    return coffee


def report(revenue):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']

    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${revenue}")


def areResourcesSufficient(ingredients):
    if resources['water'] < ingredients['water']:
        print("Sorry there is not enough water")
        return False
    if resources['coffee'] < ingredients['coffee']:
        print('Sorry there is not enough coffee')
        return False
    if 'milk' in ingredients.keys() and ingredients['milk'] > resources['milk']:
        print("Sorry there is not enough milk")
        return False

    return True


def process(quarters, dimes, nickles, pennies):
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


def is_transaction_successful(coffee, quarters, dimes, nickles, pennies):
    cost = process(quarters, dimes, nickles, pennies)
    if cost < MENU[coffee]['cost']:
        return False
    elif cost == MENU[coffee]['cost']:
        return True
    else:
        excess = round(cost - MENU[coffee]['cost'], 2)
        print(f"Here is ${excess} dollars in change.")
        return True


def make_coffee():
    global revenue
    report(revenue)

    coffee = askforOrder()
    ingredients = MENU[coffee]['ingredients']

    if not areResourcesSufficient(ingredients):
        return

    else:
        print("Number of quarters: ")
        quarters = int(input())
        print("Number of dimes: ")
        dimes = int(input())
        print("Number of nickles: ")
        nickles = int(input())
        print("Number of pennies: ")
        pennies = int(input())

        if not is_transaction_successful(coffee, quarters, dimes, nickles, pennies):
            print("Sorry that's not enough money. Money refunded.")

        else:
            revenue += MENU[coffee]['cost']
            for ingredient, quantity  in ingredients.items():
                resources[ingredient] -= quantity

            report(revenue)

            print(f"Here is your {coffee}. Enjoy!")


isOff = False

while not isOff:
    print("Welcome to the Coffee Machine!")
    print("Enter off to switch Coffee Machine off/ report to get the profits: ")
    choice = input()
    if choice == "off":
        isOff = True
    elif choice == "report":
        report(revenue)
    else:
        make_coffee()





