def Students_Results(percentage):
    if 90 <= percentage <= 100:
        return "Congratulations on your success."
    elif 70 <= percentage < 90:
        return "You should put in more effort."
    elif 0 <= percentage < 70:
        return "We regret to inform you that you have failed."
    else:
        return "Please enter a valid percentage between 0 and 100."



customer_percentage = float(input("Please enter the grade to view the result: "))

print(Students_Results(customer_percentage))