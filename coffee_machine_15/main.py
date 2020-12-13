from coffee_machine_15.coffee_data import MENU, resources

money: float = 0.0
coffee_menu = MENU
coffee_resources = resources
QUARTER_VALUE = 0.25
DIME_VALUE = 0.10
NICKLE_VALUE = 0.05
PENNY_VALUE = 0.01


def check_resources(coffee_option: str) -> str:
    # print('Inside check resources...')
    shortage = None
    for key in coffee_resources:
        if key == 'milk' and coffee_option == 'espresso':
            pass
        else:
            # print(f"{coffee_resources[key]} vs {coffee_menu[coffee_option]['ingredients'][key]}")
            if coffee_resources[key] < coffee_menu[coffee_option]['ingredients'][key]:
                shortage = key
                break
    # print(f'shortage value: {shortage}')
    return shortage


def print_report():
    for i in coffee_resources:
        print(f"{i}: {coffee_resources[i]}")
    print(f"money ${money}")


def process_coins() -> float:
    quarters = float(input('quarters: ') or 0.0)
    dimes = float(input('dimes: ') or 0.0)
    nickles = float(input('nickles: ') or 0.0)
    pennies = float(input('pennies: ') or 0.0)
    total_value = quarters * QUARTER_VALUE + dimes * DIME_VALUE + nickles * NICKLE_VALUE + pennies * PENNY_VALUE
    return total_value


# todo Check transaction is successful
def check_transaction_successful(coffee_option: str, amount: float) -> bool:
    global money
    # print(f"**** {coffee_menu[coffee_option]['cost']} vs {amount}")
    if coffee_menu[coffee_option]['cost'] > amount:
        return False
    else:
        if amount - coffee_menu[coffee_option]['cost'] > 0:
            # print(f"Here is the ${amount - coffee_menu[coffee_option]['cost']} in change.")
            print("Here is the ${:.2f} in change".format(round((amount - coffee_menu[coffee_option]['cost']), 2)))
        money += coffee_menu[coffee_option]['cost']
        return True


def make_coffee(coffee_option: str):
    # print(f'coffee resources before: {coffee_resources}')
    coffee_resources['water'] -= coffee_menu[coffee_option]['ingredients']['water']
    coffee_resources['coffee'] -= coffee_menu[coffee_option]['ingredients']['coffee']
    if coffee_option != 'espresso':
        coffee_resources['milk'] -= coffee_menu[coffee_option]['ingredients']['milk'] or 0.0
    # print(f'coffee resources after: {coffee_resources}')


user_input: str = None

while user_input != 'off':
    user_input = input("What would you like? ")
    if user_input == 'report':
        print_report()
    elif user_input in ['espresso', 'latte', 'cappuccino']:
        shortage_value = check_resources(user_input)
        if shortage_value is not None:
            print(f'Sorry there is not enough {shortage_value}')
        else:
            total_amount = process_coins()
            # print(total_amount)
            if check_transaction_successful(user_input, total_amount):
                make_coffee(user_input)
            else:
                print("Sorry that's not enough money. Money refunded.")
