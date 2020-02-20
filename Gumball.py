import math

def vendGumball(currencyAmount, color):
    gumballs = {
        1: [5, "red"],
        2: [10, "yellow"]
    }

    if currencyAmount - gumballs[color][0] < 0:
        print("Not enough currency.")
    else:
        currencyAmount = currencyAmount - gumballs[color][0]
        print("Dispensing {} gumball.".format(gumballs[color][1]))

    return currencyAmount 

def returnCurrency(value):
    quarters = math.floor(value / 25)
    value = value - (quarters * 25)
    dimes = math.floor(value / 10)
    value = value - (dimes * 10)
    nickles = math.floor(value / 5)
    value = value - (nickles * 5)

    print("Returning {} quarters, {} dimes, and {} nickles.".format(quarters, dimes, nickles))

def proccessInput(value, currencyAmount):
    if value.lower() == "h":
        print("R = Dispense Red, Y = Dispense Yellow\nN = Insert Nickle, D = Insert Dime, Q = Insert Quarter\n'ret' to retrieve change and exit\n")
        return True, currencyAmount
    elif value.lower() == "r":
        currencyAmount = vendGumball(currencyAmount, 1)
        return True, currencyAmount
    elif value.lower() == "y":
        currencyAmount = vendGumball(currencyAmount, 2)
        return True, currencyAmount
    elif value.lower() == "n":
        currencyAmount = currencyAmount + 5
        return True, currencyAmount
    elif value.lower() == "d":
        currencyAmount = currencyAmount + 10
        return True, currencyAmount
    elif value.lower() == "q":
        currencyAmount = currencyAmount + 25
        return True, currencyAmount
    elif value.lower() == "ret":
        returnCurrency(currencyAmount)
        return False, 0

if __name__ == "__main__":
    print("Gumball machine.\n R = Dispense Red, Y = Dispense Yellow\n N = Insert Nickle, D = Insert Dime, Q = Insert Quarter\n'ret' to retrieve change and exit")
    currencyAmount = 0
    cont = True
    validInputs = ["h", "r", "y", "n", "d", "q", "ret"]

    while cont:
        if currencyAmount > 0:
            print("Remaining currency is {} cents".format(currencyAmount))
        value = input("Perform action (H for help): ")
        if value.lower() in validInputs:
            cont, currencyAmount = proccessInput(value.lower(), currencyAmount)
        else:
            print("Invalid input.")
    pass