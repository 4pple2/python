from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

choice = Menu()
coffee = CoffeeMaker()
money_cal = MoneyMachine()

# 커피 주문 받기
test = 'true'
while test == 'true':
    customer_coffee = input("choice your coffee : ")
    # report 작성
    if customer_coffee.lower() == 'report':
        coffee.report()
        money_cal.report()

    else:
        # 커피 제조
        desired_drink = choice.find_drink(customer_coffee)

        if desired_drink is not None:
            money_cal.make_payment(2)
            make_dec = coffee.is_resource_sufficient(desired_drink)

            if make_dec:
                coffee.make_coffee(desired_drink)
            else:
                print("end")
            test ='false'
        else:
            test = 'true'

