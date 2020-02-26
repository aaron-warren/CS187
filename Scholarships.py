# A student is eligible for scholarships if he satisfies the below conditions:

# A. Student is between the  age 18 and 24 (boundary value included)

# B. Student has lived in California for last 2 years, if he fails this criterion, check if satisfies D.

# C. Has worked part time for at least for 6 months in the relevant field of study, if he fails this criterion, check if satisfies E.

# D. Parents of the student have paid California state tax for at least 1 year in their lifetime.

# E. Has volunteered for a cause and has a valid proof of it.

# F. Has household income less than 5000$ per annum then one need not satisfy criteria C, he will be redirected to "Dean for consideration"

def eligible():
    eligibility = []

    age = getNumber("Input age: ")
    if age >= 18 and age <= 24:
        eligibility.append(1)

    resident = getLetter("Lived in California last 2 years (y/n): ")
    if resident == "n":
        taxes = getLetter("Parents paid CA state tax for at least 1 year throughout life (y/n): ")
        if taxes == "y":
            eligibility.append(1)
        else:
            eligibility.append(0)
    else:
        eligibility.append(1)
    
    partTime = getNumber("Duration in months working part time in relevant field of study: ")
    if partTime < 6:
        volunteer = getLetter("Volunteered for a cause and have valid proof (y/n): ")
        if volunteer == "y":
            eligibility.append(1)
        else:
            eligibility.append(0)
    else:
        eligibility.append(1)
    
    household = getLetter("Household income less than $5000 per annum (y/n): ")
    if household == "y":
        eligibility[2] = "Dean for consideration"

    return eligibility

def getNumber(prompt):
    while True:
        number = input(prompt)
        if number.isdigit():
            number = int(number)
            break;
        else:
            print("Invalid input.")
    return number

def getLetter(prompt):
    possibleInputs = ["y", "n"]
    while True:
        letter = input(prompt)
        if letter.lower() in possibleInputs:
            break;
        else:
            print("Invalid input.")
    return letter.lower()

if __name__ == "__main__":
    
    earray = eligible()
    print(earray)

    pass