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
money = 0
report = {
    "water": 300,
    "milk": 200,
    "coffee": 100}


def check_resources(order_ingredients):
    """Checks if there is enough ingredients to make a drink and return True if there is, but False if there isn't."""
    for item in order_ingredients:
        if order_ingredients[item] >= report[item]:
            print(f"Sorry, there is not enough {item} to make this drink")
            return False
    return True


def process_coins():
    """Calculates the total amount of coins a customer puts in and returns the total"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_successful(money_received, drink_cost):
    """Returns True when the payment is successful or False when insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        report[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {report['water']}ml")
        print(f"Milk: {report['milk']}ml")
        print(f"Coffee: {report['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[user_choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
