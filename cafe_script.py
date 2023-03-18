def main():
    user_name = input("Hello! What is your name? ")
    menu = f"""**************************************
**    Welcome to the Snakes Cafe,   **
**            {user_name}!         
**    Please see our menu below.    **
** To quit at any time, type "quit" **
**************************************

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
    user_order = {
        "Appetizers": [],
        "Entrees": [],
        "Desserts": [],
        "Drinks": []
    }
    order = input("""***********************************
** What would you like to order? **
***********************************
""")

    # while order != 'quit':
    #     order


if __name__ == "__main__":
    main()
