def tickets(gender, age):
    if str(gender).lower() not in ["m", "f"]:
        return "Invalid input for gender"
    
    if not isinstance(age, int):
        return "Invalid input for age"

    if gender.lower() == "m":
        if age > 7 and age < 10:
            return "Storytelling"
        elif age > 11 and age < 15:
            return "Quiz"
        elif age < 6:
            return "Rhyming"
        elif age > 20:
            return "Poetry"
    if gender.lower() == "f":
        if age > 7 and age < 10:
            return "Drawing"
        elif age > 11 and age < 15:
            return "Essay Writing"
        elif age < 6:
            return "Rhyming"
        elif age > 20:
            return "Poetry"

if __name__ == "__main__":
    print(tickets("m", 12))
    pass