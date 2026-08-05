# Programming One Formative Assignment 2026
# Done by Sarafina Emmanuely Barnabas - CS 2026
# This is my first programming assignment for Programming One Course 2026.

print("A student grade/assignment tracker to enable users to record homework and exam results, view and filter assignments and display the grade summaries within a single terminal session.")

#Since we will later have different assignments, a list is now created to store these assignments
assignments = []

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

#Creating function for each menu option
def add_homework():
    print("You now have to add your homework")

def add_examination():
    print("You now have to add your examination")

def list_assignments():
    print("By selecting this option, all your assignments will be displayed")

def filter_assignments():
    print("By selecting this option, you can filter all your assignments by month, subject or type")

def show_summary():
    print("You can now see all the summary of your assignments, exams, homeworks and grades")

def exit_program():
    print("You have chosen to exit the program.")


never_end = True

#Creating function that makes the user see the menu list again untill they select to exit the program ,and this is possible with the while loop
while never_end:

    #In order for this function to run I have to call the funtion and assign it to a variable so that I can be able to print the menu list and what the user will select.
    user_selection = menu()
    
#After a user has made a selcetion from the menu, I will use the if statements to check what they have selected and give the correct response.
    if user_selection=="1":
        add_homework()

    elif user_selection=="2":
        add_examination()

    elif user_selection=="3":
        list_assignments()

    elif user_selection=="4":
        filter_assignments()

    elif user_selection=="5":
        show_summary()

    elif user_selection=="0":
        exit_program()
        never_end = False

    else:
        print("This selection does not exist, please select an option from the menu given above.")

