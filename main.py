from menu import MENU, resources
# The default contents in the machine
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0


def check_resources(order, water, milk, coffee):
    """Takes the order and check if there are enough ingredients to make it"""
    if order == "espresso":
        if water < MENU["espresso"]["ingredients"]["water"]:
            print("No enough water for your espresso")
            return 0
        elif coffee < MENU["espresso"]["ingredients"]["coffee"]:
            print("No enough coffee for your espresso")
            return 0
        else:
            return 1

    elif order == "latte":
        if water < MENU["latte"]["ingredients"]["water"]:
            print("No enough water for your latte")
            return 0
        elif coffee < MENU["latte"]["ingredients"]["coffee"]:
            print("No enough coffee for your latte")
            return 0
        elif milk < MENU["latte"]["ingredients"]["milk"]:
            print("No enough milk for your latte")
            return 0
        else:
            return 1

    elif order == "cappuccino":
        if water < MENU["cappuccino"]["ingredients"]["water"]:
            print("No enough water for your cappuccino")
            return 0
        elif coffee < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("No enough coffee for your cappuccino")
            return 0
        elif milk < MENU["cappuccino"]["ingredients"]["milk"]:
            print("No enough milk for your cappuccino")
            return 0
        else:
            return 1


def process_coins():
    """Takes the inserted money and returns the sum of it"""
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    # Calculate how much have been inserted of each coin
    quarters_sum = quarters * 0.25
    dimes_sum = dimes * 0.10
    nickles_sum = nickles * 0.05
    pennies_sum = pennies * 0.01
    # Total of all the inserted coins
    total_coins = quarters_sum + dimes_sum + nickles_sum + pennies_sum
    return total_coins


# Flag to help exit the loop when becomes False
should_continue_serving = True

while should_continue_serving:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # A secret entry to turn the machine off for maintenance
    if order == "off":
        should_continue_serving = False
    # Another secret word to display the status of the machine
    elif order == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    elif order == "espresso":
        # Call check_resources function to see if there are enough ingredients
        # to proceed with the order
        if check_resources(order, water, milk, coffee) == 1:
            print("Please insert coins")
            # Call process_coins function to ask the user to insert coins
            # and calculate them
            coins = process_coins()
            # If the money inserted is enough, proceed with the order
            if coins >= MENU["espresso"]["cost"]:
                # Check if there is any remaining change to give back
                change = coins - (MENU["espresso"]["cost"])
                if change > 0:
                    print(f"Here is ${round(change, 2)} in change.")
                # Keep tracking of the money collected to see how much
                # money the machine contains
                money += (coins - change)
                # Update the ingredients quantity after each order to see
                # how much ingredients left
                water -= MENU["espresso"]["ingredients"]["water"]
                coffee -= MENU["espresso"]["ingredients"]["coffee"]
                print("Here is your espresso ☕️. Enjoy!")
            # Refund the money when the user didn't insert enough coins
            else:
                print("Sorry that's not enough money. Money refunded.")
        # When at least one of the ingredients is not enough for the order
        else:
            print("Sorry for the inconvenience")
    elif order == "latte":
        # Call check_resources function to see if there are enough ingredients
        # to proceed with the order
        if check_resources(order, water, milk, coffee) == 1:
            print("Please insert coins")
            # Call process_coins function to ask the user to insert coins
            # and calculate them
            coins = process_coins()
            # If the money inserted is enough, proceed with the order
            if coins >= MENU["latte"]["cost"]:
                # Check if there is any remaining change to give back
                change = coins - (MENU["latte"]["cost"])
                if change > 0:
                    print(f"Here is ${round(change, 2)} in change.")
                # Keep tracking of the money collected to see how much
                # money the machine contains
                money += (coins - change)
                # Update the ingredients quantity after each order to see
                # how much ingredients left
                water -= MENU["latte"]["ingredients"]["water"]
                coffee -= MENU["latte"]["ingredients"]["coffee"]
                milk -= MENU["latte"]["ingredients"]["milk"]
                print("Here is your latte ☕️. Enjoy!")
            # Refund the money when the user didn't insert enough coins
            else:
                print("Sorry that's not enough money. Money refunded.")
        # When at least one of the ingredients is not enough for the order
        else:
            print("Sorry for the inconvenience")
    elif order == "cappuccino":
        # Call check_resources function to see if there are enough ingredients
        # to proceed with the order
        if check_resources(order, water, milk, coffee) == 1:
            print("Please insert coins")
            # Call process_coins function to ask the user to insert coins
            # and calculate them
            coins = process_coins()
            # If the money inserted is enough, proceed with the order
            if coins >= MENU["cappuccino"]["cost"]:
                # Check if there is any remaining change to give back
                change = coins - (MENU["cappuccino"]["cost"])
                if change > 0:
                    print(f"Here is ${round(change, 2)} in change.")
                # Keep tracking of the money collected to see how much
                # money the machine contains
                money += (coins - change)
                # Update the ingredients quantity after each order to see
                # how much ingredients left
                water -= MENU["cappuccino"]["ingredients"]["water"]
                coffee -= MENU["cappuccino"]["ingredients"]["coffee"]
                milk -= MENU["cappuccino"]["ingredients"]["milk"]
                print("Here is your cappuccino ☕️. Enjoy!")
            # Refund the money when the user didn't insert enough coins
            else:
                print("Sorry that's not enough money. Money refunded.")
        # When at least one of the ingredients is not enough for the order
        else:
            print("Sorry for the inconvenience")

