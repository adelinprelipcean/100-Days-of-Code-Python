import coffee_maker  
import menu
import money_machine

coffee_maker = coffee_maker.CoffeeMaker()
menu = menu.Menu()
money_machine = money_machine.MoneyMachine()

selection = input("What would you like? (espresso/latte/cappuccino): ")

while(selection != 'off'):
    if selection == 'report':
        coffee_maker.report()
        money_machine.report()
    elif selection == 'espresso' or selection == 'cappuccino' or selection == 'latte':
        if coffee_maker.is_resource_sufficient(menu.find_drink(selection)):
            inserted = money_machine.process_coins()
            while(inserted < menu.find_drink(selection).cost):
                inserted = money_machine.process_coins()
            coffee_maker.make_coffee(menu.find_drink(selection))
        else:
            print("Not sufficient resources! Try something else...")
    selection = input("What would you like? (espresso/latte/cappuccino): ")