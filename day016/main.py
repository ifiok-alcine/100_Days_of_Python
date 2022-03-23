from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

instant_coffee_maker = CoffeeMaker()
menu = Menu()
coin_processor = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}): ").lower()

    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        instant_coffee_maker.report()
        coin_processor.report()
    else:
        drink = menu.find_drink(user_choice)
        if instant_coffee_maker.is_resource_sufficient(drink) and coin_processor.make_payment(drink.cost):
            instant_coffee_maker.make_coffee(drink)
