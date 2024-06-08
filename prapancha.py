import sys
import random
import getpass
from datetime import date

menu={"breakfast":{"Idly":10.0,"Dosa":15.0,"Vada":20.0,"Bisibelebath":30.0},
        "lunch":{"Sambar":30.0,"Rasam":35.0},
        "dinner":{"Paneer":38.0,"Fried-rice":50.0}}

def owner_login():
    details = {"vaish":"Hope","thea":"Faith"}
    username = input("Enter your username: ")
    while username not in details:
        print("Invalid username!")
        username = input("Enter your username: ")
    max_attempts = 3
    attempts=0
    for i in range(max_attempts):
        password = getpass.getpass("Enter your password: ")
        if password == details.get(username):
            print("User verified")
            break
        else:
            attempts += 1
            print("Incorrect password. Try again.")
            if attempts == max_attempts:
                print("Maximum attempts reached. Please contact support if you are having trouble.")
                sys.exit(0)
    
    for meal_type, dishes in menu.items():
        print((f"\n{str(''.center(45) + meal_type.capitalize()).ljust(50)} Menu:"))

        print()
    
        for dish, price in dishes.items():
            print((f"{dish.ljust(20)}: {str('₹'+str(price)).rjust(12)}").center(100))
    print()
    while True:
        print("Enter 1.To add an item 2.To delete an item 3.Update item 4.Exit")
        ch=input('Enter your choice: ')
        if ch=='1':
            meal_type = input("Enter meal type (b/l/d for breakfast/lunch/dinner): ").lower()
            if meal_type in ['b', 'l', 'd']:
                meal_type = {'b': 'breakfast', 'l': 'lunch', 'd': 'dinner'}[meal_type]
            dish_name = input("Enter dish name: ").capitalize()
            dish_price = float(input("Enter dish price: "))

            if meal_type in menu:
                if dish_name in menu[meal_type]:
                    print("Dish already exists.")
                menu[meal_type][dish_name] = dish_price
            else:
                menu[meal_type] = {dish_name: dish_price}

            print("Updated menu:")
            for meal_type, dishes in menu.items():
                print((f"\n{str(''.center(45) + meal_type.capitalize()).ljust(50)} Menu:"))

                print()
    
                for dish, price in dishes.items():
                    print((f"{dish.ljust(20)}: {str('₹'+str(price)).rjust(12)}").center(100))
        
        elif ch=='2':
            meal_type = input("Enter meal type (b/l/d for breakfast/lunch/dinner): ").lower()
            if meal_type in ['b', 'l', 'd']:
                meal_type = {'b': 'breakfast', 'l': 'lunch', 'd': 'dinner'}[meal_type]
            if meal_type in menu:
                dish_abbv = input(f"Enter the first two letters of the dish name to be deleted: ").capitalize()

                dish_name=None
                for dish in menu[meal_type]:
                    if dish.startswith(dish_abbv):
                        dish_name=dish
                        break

                if dish_name in menu[meal_type]:
                    del menu[meal_type][dish_name]
                    print(f"{dish_name} deleted from {meal_type.capitalize()} menu.")
                    print("Updated menu:")
                    for meal_type, dishes in menu.items():
                        print((f"\n{str(''.center(45) + meal_type.capitalize()).ljust(50)} Menu:"))

                        print()
    
                        for dish, price in dishes.items():
                            print((f"{dish.ljust(20)}: {str('₹'+str(price)).rjust(12)}").center(100))
                else:
                    print(f"{dish_name} not found in {meal_type.capitalize()} menu.")
            else:
                print(f"{meal_type.capitalize()} menu not found.")

        elif ch=='3':
            meal_type = input("Enter meal type (b/l/d for breakfast/lunch/dinner): ").lower()
            if meal_type in ['b', 'l', 'd']:
                meal_type = {'b': 'breakfast', 'l': 'lunch', 'd': 'dinner'}[meal_type]
            if meal_type in menu:
                dish_abbv = input("Enter the first two letters of the dish name to be updated: ").capitalize()

                dish_name=None
                for dish in menu[meal_type]:
                    if dish.startswith(dish_abbv):
                        dish_name=dish
                        break

                if dish_name in menu[meal_type]:
                    new_price = float(input("Enter the new price for the dish: "))
                    menu[meal_type][dish_name] = new_price
                    print(f"{dish_name} price updated in {meal_type} menu.")
                    print("Updated menu:")
                    for meal_type, dishes in menu.items():
                        print((f"\n{str(''.center(45) + meal_type.capitalize()).ljust(50)} Menu:"))

                        print()
    
                        for dish, price in dishes.items():
                            print((f"{dish.ljust(20)}: {str('₹'+str(price)).rjust(12)}").center(100))
                else:
                    print(f"{dish_name} not found in {meal_type} menu.")
            else:
                print(f"{meal_type} menu not found.")

        elif ch=='4':
            sys.exit()

        else:
            print("Invalid choice")
    return

def biller_login():
    name = input("Enter customer name: ")
    date_of_birth = input("Enter DOB in (YYYY-MM-DD) format: ")
    dob=date.fromisoformat(date_of_birth)
    current_date = date.today()
    current_day = current_date.strftime("%A")
    age=current_date.year-dob.year 

    random_num=random.randint(0,99)
    bill_id="100"+str(random_num)

    for meal_type, dishes in menu.items():
        print((f"\n{str(''.center(45) + meal_type.capitalize()).ljust(50)} Menu:"))

        print()

        for dish, price in dishes.items():
            print((f"{dish.ljust(20)}: {str('₹' + str(price)).rjust(12)}").center(100))
    print()

    bill={}
    while True:
        dish_name=input("Enter the first two letters of dish name or STOP to exit ").lower()

        if dish_name == 'stop':
            break

        found = False
        for meal_type, dishes in menu.items():
            for dish, price in dishes.items():
                if dish_name == dish[:2].lower():
                    quantity = int(input("Enter the quantity "))
                    if dish in bill:
                        bill[dish] += quantity
                    else:
                        bill[dish] = quantity
                    found = True
                    break
            if found:
                break

        if not found:
            print("Item not found in the menu. Please enter the correct abbreviated code.")
    print()

    total_price=0
    for item, quantity in bill.items():
        for meal_type, dishes in menu.items():
            if item in dishes:
                price = dishes[item]
                item_total = price * quantity
                total_price += item_total
    
    if current_date.month == dob.month and current_date.day == dob.day:
        print("Happy birthday!You get 20% off")
        discount=(20/100)*total_price
    elif(age>60):
        print("Senior citizens can avail flat 20'/%' off on everything!")
        discount=(20/100)*total_price
    elif current_day[0].lower()==name[0].lower():
        print("Hello ", name," Since the day starts with you , here's a 15% discount for you ! ")
        discount=(15/100)*total_price
    else:
        print("\nSorry no discount!! Better luck next time.")
        discount=0.00

    tip=input("Would you like to add a tip? (y/n): ").lower()
    if tip=='y':
        tip_amount=float(input("Enter the tip amount: "))
        print("Thank you for the tip!")
    else:
        tip_amount=0.00

    restaurant_name=chr(3242)+ chr(3248)+ chr(3242)+ str(0)+ chr(3226)
    print(restaurant_name.center(124))

    print(f"{''.center(20)}Date: {current_date.strftime('%Y-%m-%d')}    {'Bill ID:'.rjust(55)} {bill_id}")
    

    print()

    total_price=0
    
    print("".ljust(20)+"--------------------------------------------------------------------------------")

    print("".ljust(20)+"Item".ljust(25) + "Quantity".ljust(25) + "Price".ljust(25) + "Total".ljust(25))
    print("".ljust(20)+"--------------------------------------------------------------------------------")

    for item, quantity in bill.items():
        for meal_type, dishes in menu.items():
            if item in dishes:
                price = dishes[item]
                item_total = price * quantity
                total_price += item_total
        print("".ljust(20)+item.ljust(25) + ": " + str(quantity).ljust(25)+"x " + str(price).ljust(20) + "= " + str(item_total).ljust(
        20))

    print("".ljust(20)+"--------------------------------------------------------------------------------")

    gst=(18/100)*total_price
    print("".ljust(20)+"Sub total :                                                             ₹"+format(total_price, '.2f').rjust(7))
    print("".ljust(20)+"GST@ :                                                                  ₹"+format(gst,'.2f').rjust(7))
    print("".ljust(20)+"Tip amount :                                                            ₹"+format(tip_amount,'.2f').rjust(7))
    print("".ljust(20)+"Discount :                                                              ₹"+format(discount,'.2f').rjust(7))
    print("".ljust(20)+"Total :                                                                 ₹"+format(total_price+gst+tip_amount-discount,'.2f').rjust(7))
    
    print("\n"+"".ljust(40)+ "******  Thank you for your visit!!!  ****")

    return

while True:
    print("Enter 1.Owner 2.Biller 3.Exit")
    ch=input("Enter your choice: ")
    if ch=='1':
        print("Welcome to owner desk!")
        owner_login()
    elif ch=='2':
        print("You've entered the billing section.")
        biller_login()
    elif ch=='3':
        print("Thank you for visiting our restaurant.")
        sys.exit()
    else:
        print("Invalid choice")