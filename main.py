from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
money=MoneyMachine()
menu=Menu()

is_on="Yes"

while is_on=="Yes":
    options=menu.get_items()
    choice=input(f"What wold you like to have{options}:  ")
    if choice=="no":
        break
    elif choice=="report":
        coffee_maker.report()
        money.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)