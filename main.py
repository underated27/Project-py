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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made and False when it is insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough water")
            return False
    return True


def process_coins():
    """Returns total calculated coins inserted"""
    print("Please insert coins")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickels?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total

def transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted else False"""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry thats not enough money.Money refunded")
def make_coffee(drinkname, orderingredient):
    """Deduct the required ingredients from the resources"""
    for item in orderingredient:
        resources[item] -= orderingredient[item]
    print(f"Here is your drink {drinkname} ☕️")


coffee_machine = True
while coffee_machine:
    coffee = input("What would you like?(espresso/latte/cappuccino)").lower()
    if coffee == "off":
        coffee_machine = False
    elif coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[coffee]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(coffee, drink["ingredients"])