# Programming One Formative Assignment 2026
# Done by Sarafina Emmanuely Barnabas - CS 2026
# This is my first programming assignment for Programming One Course 2026.

print("A student grade/assignment tracker to enable users to record homework and exam results, view and filter assignments and display the grade summaries within a single terminal session.")
#Creating a menu list where users can select from using print statements
print(" Below is a menu list where you can choose from;")
print("1. Add homework")
print("2. Add examination")
print("3. List assignments")
print("4. Filter out by subject/type or month")
print("5. Show summary")
print("0. Exit")

#Creating a function that has a menu and input statements to allow users to make a choice from the menu
def menu():
    print(" Below is a menu list where you can choose from;")
    print("1. Add homework")
    print("2. Add examination")
    print("3. List assignments")
    print("4. Filter out by subject/type or month")
    print("5. Show summary")
    print("0. Exit")
    selection = input("Select an option from the menu list provided:")
    return selection

#In order for this function to run I have to call the funtion and assign it to a variable so that I can be able to print the menu list and what the user will select.
user_selection = menu()
print("You selected option: " + user_selection)
