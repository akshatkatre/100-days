from coffee_data import MENU, resources

money: float = 0.0
coffee_menu = MENU
coffee_resources = resources
QUARTER_VALUE = 0.25
DIME_VALUE = 0.10
NICKLE_VALUE = 0.05
PENNY_VALUE = 0.01


def check_resources(coffee_option: dict):
    shortage = None
    for key in coffee_option:
        if coffee_resources[key] < coffee_option[key]:
            shortage = key
            return shortage
    return shortage


def print_report():
    print(f"water: {coffee_resources['water']} ml")
    print(f"milk: {coffee_resources['milk']} ml")
    print(f"coffee: {coffee_resources['coffee']} gm")
    print(f"money ${money}")


def process_coins() -> float:
    quarters = float(input('quarters: ') or 0.0)
    dimes = float(input('dimes: ') or 0.0)
    nickles = float(input('nickles: ') or 0.0)
    pennies = float(input('pennies: ') or 0.0)
    total_value = quarters * QUARTER_VALUE + dimes * DIME_VALUE + nickles * NICKLE_VALUE + pennies * PENNY_VALUE
    return total_value


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


def make_coffee(coffee_option: dict):
    for key in coffee_option:
        coffee_resources[key] -= coffee_option[key]


user_input: str = None

while user_input != 'off':
    user_input = input("What would you like? ")
    if user_input == 'report':
        print_report()
    elif user_input in ['espresso', 'latte', 'cappuccino']:
        shortage_value = check_resources(coffee_menu[user_input]['ingredients'])
        if shortage_value is not None:
            print(f'Sorry there is not enough {shortage_value}')
        else:
            total_amount = process_coins()
            # print(total_amount)
            if check_transaction_successful(user_input, total_amount):
                make_coffee(coffee_menu[user_input]['ingredients'])
            else:
                print("Sorry that's not enough money. Money refunded.")
