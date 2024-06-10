from data import MENU, resources
turn_off = False


def print_report():
    print(f'''water: {resources['water']}ml
milk: {resources['milk']}ml
coffee: {resources['coffee']}g
money: ${resources['money']}
    ''')


def check_resources(order):
    required_water = MENU[order]['ingredients']['water']
    required_coffee = MENU[order]['ingredients']['coffee']
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]
    if order != 'espresso':
        required_milk = MENU[order]['ingredients']['milk']
        if required_milk > milk:
            print('Sorry, there is not enough milk')
            return False
    if required_water > water:
        print('Sorry, there is not enough water')
        return False
    if required_coffee > coffee:
        print('Sorry, there is not enough coffee')
        return False
    else:
        return True


def process_coins(quarters,dimes,nickles,pennies):
    total_coins = quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01

    return total_coins


def check_transaction(order,quarters,dimes,nickles,pennies):
    order_price = MENU[order]['cost']
    coins=process_coins(quarters,dimes,nickles,pennies)
    if order_price > coins:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif order_price == coins:
        resources['money'] += order_price
        return True
    elif order_price < coins:
        print(f'Here is ${coins-order_price} in charge.')
        resources['money'] += order_price
        return True


def make_coffee(order):
    required_water = MENU[order]['ingredients']['water']
    required_coffee = MENU[order]['ingredients']['coffee']
    resources["water"] = resources["water"]-required_water
    resources["coffee"] = resources["coffee"]-required_coffee
    if order != 'espresso':
        required_milk = MENU[order]['ingredients']['milk']
        resources["milk"] = resources["milk"]-required_milk
    print(f'Here is your {order} ☕. Enjoy! ☺')


while not turn_off:
    your_order = input('What would you like? (espresso/latte/cappuccino):')
    if your_order == 'report':
        print_report()
    elif your_order == 'off':
        turn_off = True
        break
    else:
        if check_resources(your_order):
            print('Please insert coins.')
            quarters = float(input('how many quarters?: '))
            dimes = float(input('how many dimes?: '))
            nickles = float(input('how many nickles?: '))
            pennies = float(input('how many pennies?: '))
            process_coins(quarters, dimes, nickles, pennies)
            if check_transaction(your_order,quarters,dimes,nickles,pennies):
                make_coffee(your_order)


