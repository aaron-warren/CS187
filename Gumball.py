import math

# Handles logic for vending the gumball and updating the currency afterwards
def vendGumball(currencyAmount, color):
    # Stores the relevant values for each gumballs color and their respective currency amounts
    gumballs = {
        1: [5, "red"],
        2: [10, "yellow"]
    }

    # Error checking to ensure that the user has enough money to vend the desired gumball
    if currencyAmount - gumballs[color][0] < 0:
        print("Not enough currency.")
    else: # If the user does have enough money then it will vend the gumball and then update the amount of currency remaining
        currencyAmount = currencyAmount - gumballs[color][0]
        print("Dispensing {} gumball.".format(gumballs[color][1]))

    return currencyAmount # Returns the remaining amount of currency after vending/not vending the gumball

# Handles logic for calculating amount of coins to return to the user after wanting to leave
def returnCurrency(value):
    # Calculates amount of each coin using method from biggest to smallest coins
    quarters = math.floor(value / 25)
    value = value - (quarters * 25)
    dimes = math.floor(value / 10)
    value = value - (dimes * 10)
    nickles = math.floor(value / 5)
    value = value - (nickles * 5)

    print("Returning {} quarters, {} dimes, and {} nickles.".format(quarters, dimes, nickles))

# Handles logic for respective inputs
def proccessInput(value, currencyAmount):
    if value.lower() == "h": # Outputs our help prompt incase the user forgets the keys
        print("R = Dispense Red, Y = Dispense Yellow\nN = Insert Nickle, D = Insert Dime, Q = Insert Quarter\n'ret' to retrieve change and exit\n")
        return True, currencyAmount
    elif value.lower() == "r": # Sends currency amount and red index (1) to the vend gumball function
        currencyAmount = vendGumball(currencyAmount, 1)
        return True, currencyAmount
    elif value.lower() == "y": # Sends currency amount and yellow index (2) to the vend gumball function
        currencyAmount = vendGumball(currencyAmount, 2)
        return True, currencyAmount
    elif value.lower() == "n": # Updates the amount of currency after a nickle is input into the system
        currencyAmount = currencyAmount + 5
        return True, currencyAmount
    elif value.lower() == "d": # Updates the amount of currency after a dime is input into the system
        currencyAmount = currencyAmount + 10
        return True, currencyAmount
    elif value.lower() == "q": # Updates the amount of currency after a quarter is input into the system
        currencyAmount = currencyAmount + 25
        return True, currencyAmount
    elif value.lower() == "ret": # Handles user wanting to exit system by sending remaining currency to the return currency function
        returnCurrency(currencyAmount)
        return False, 0

if __name__ == "__main__":
    # Initial statement with default help prompt for the user
    print("Gumball machine.\n R = Dispense Red, Y = Dispense Yellow\n N = Insert Nickle, D = Insert Dime, Q = Insert Quarter\n'ret' to retrieve change and exit")
    currencyAmount = 0 # Initialize currency user has at start
    cont = True # Initialize loop for user
    validInputs = ["h", "r", "y", "n", "d", "q", "ret"] # Ensures that only these values can be input, anything else will prompt user error and to retry

    while cont: # Continues loop as long as user doesn't input "ret"
        if currencyAmount > 0: # Outputs amount of currency user has as long as they have more than 0 currency
            print("Remaining currency is {} cents".format(currencyAmount))
        value = input("Perform action (H for help): ") # Prompts user for input
        if value.lower() in validInputs: # If input is in the validInputs array, then it will allow it to go to the input handling
            cont, currencyAmount = proccessInput(value.lower(), currencyAmount)
        else: # Otherwise it will output invalid input and restart the loop
            print("Invalid input.")
    pass