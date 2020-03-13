def tickets(gender, age):
    # Input validation for gender, allows only "M", "F", "m", or "f" as valid inputs
    if str(gender).lower() not in ["m", "f"]:
        return "Invalid input for gender"
    
    # Input validation for age, allows only integers of greater or equal value of 0
    if not isinstance(age, int) or age < 0:
        return "Invalid input for age"

    # Handles if gender is "m" or "M"
    if gender.lower() == "m":
        if age > 7 and age < 10: # Boys age >7 and <10, can participate in Storytelling.
            return "Storytelling"
        elif age > 11 and age < 15: # Boys age >11 and <15, can participate in a Quiz.
            return "Quiz"
        elif age < 6: # Boys and girls age <6, can participate in Rhyming.
            return "Rhyming"
        elif age > 20: # Girls and boys age >20, can participate in Poetry.
            return "Poetry"

    # Handles if gender is "f" or "F"
    if gender.lower() == "f":
        if age > 7 and age < 10: # Girls age >7 and <10, can participate in Drawing.
            return "Drawing"
        elif age > 10 and age < 15: # Girls age >10 and <15, can participate in Essay Writing.
            return "Essay Writing"
        elif age < 6: # Boys and girls age <6, can participate in Rhyming.
            return "Rhyming"
        elif age > 20: # Girls and boys age >20, can participate in Poetry.
            return "Poetry"

if __name__ == "__main__":
    print(tickets("F", 10))
    pass