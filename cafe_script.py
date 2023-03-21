def main():
    '''
    Snakes Cafe - This script prints out a menu to the
    customer, asking their name and taking their order.
    Only items listed in the cafe menu can be selected.
    '''

    customer_name = input("Hello! What is your name? ")
    menu = f"""*****************************************
**    Welcome to the Snakes Cafe,      **
**            {customer_name}!         
**     Please see our menu below.      **
**     To view your order and exit     **
**   the cafe, please type "Checkout"  **
*****************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears"""

    print(menu)

    Menu = {
        "wings": 0,
        "cookies": 0,
        "spring rolls": 0,
        "salmon": 0,
        "steak": 0,
        "meat tornado": 0,
        "a literal garden": 0,
        "ice cream": 0,
        "cake": 0,
        "pie": 0,
        "coffee": 0,
        "tea": 0,
        "unicorn tears": 0,
    }

    customer_order = {}

    order = input("""***********************************
** What would you like to order? **
***********************************
""")

    while order.lower() != "quit":
        # print(Menu.keys())
        if order.lower() in Menu:

            # Menu[order.lower()] += 1
            if order.lower() not in customer_order:
                customer_order[order.lower()] = 1
            else:
                customer_order[order.lower()] += 1
            print(customer_order)
            order = input(f"""You have ordered {customer_order[order.lower()]} order(s) of {order}. 
Anything else? """)
        elif order.lower() == "checkout":
            print(f"""
***********************************
**         Order Summary         **
**                               **
**         Thank You For         **
**        Your Business!!!       **
***********************************

Customer: {customer_name}
""")
            for item, qty in customer_order.items():
                print(qty, item)

            order = "quit"

        else:
            order = input(f"{order} doesn't exist in our menu, please choose another item. ")

        # for item_group in Menu.values():
        #     print(item_group)
            # for item in range(0, len(item_group)):
            #     print(item)

        # if order.lower() not in :
        #     user_selection.append(order)
        #     order = input(f"So far I have: {user_selection}. Anything else? ")
        #     # order = input("I didn't quite get that, please order correct item. ")
        #     # continue
        # else:
        #     # user_selection.append(order)
        #     # order = input(f"So far I have: {user_selection}. Anything else? ")
        #     order = input("I didn't quite get that, please order correct item. ")

    # print("You have selected: ", user_selection)


if __name__ == "__main__":
    main()
