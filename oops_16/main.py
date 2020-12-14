from oops_16.menu import Menu, MenuItem
from oops_16.coffee_maker import CoffeeMaker
from oops_16.money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


user_input: str = None
while user_input != 'off':
    user_input = input('​What would you like? (espresso/latte/cappuccino): ').lower()
    if user_input == 'off':
        pass
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(user_input)
        if menu_item is not None:
            if coffee_maker.is_resource_sufficient(menu_item):
                money_machine.make_payment(menu_item.cost)
                coffee_maker.make_coffee(menu_item)


