# Programming One Formative Assignment 2026
# Done by Sarafina Emmanuely Barnabas - CS 2026
# This is my first programming assignment for Programming One Course 2026.

print("A student grade/assignment tracker to enable users to record homework and exam results, view and filter assignments and display the grade summaries within a single terminal session.")

# I am now going to create a class named Assignment where all assignments will be stored.
#This is parent class and it will be inherited by the child classes Homework and Examination
class Assignment:
    def __init__(self, subject, title, score, max_score, due_date, assignment_type):
        self.subject = subject
        self.title = title
        self.score = float(score)
        self.max_score = float(max_score)
        self.due_date = due_date
        self.assignment_type = assignment_type
 #I added float to score and max_score to enable users to enter decimal numbers where needed without getting an error in the terminal.

#Homework class is a child of Assignment will inherit its components
#Super is used to take components from parent class and use them with _init_ to initialize the action
class Homework(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
            super().__init__(subject, title, score, max_score, due_date, "Homework")

class Examination(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
            super().__init__(subject, title, score, max_score, due_date, "Examination")
#Examination is also another child of Assignment class meaning it takes all its features

class tracker:
    def __init__(self):
#This is updated list where all assignments will be saved
        self.assignments = []

    def add_assignment(self, assignment):
#This calls the assignment and adds it to list
        self.assignments.append(assignment)

    def list_assignments(self):
#This lists all the assignments added and if no assignments it gives a message that no assignment found
        if not self.assignments:
            print("No assignments found.")
        else:
            for assignment in self.assignments:
                print(f"Subject is {assignment.subject}, Title is {assignment.title}, Score is {assignment.score}/{assignment.max_score}, Due Date is {assignment.due_date}, Type is {assignment.assignment_type}")

#The tracker below is created to enable the user to add assignments and view them in a list
tracker = tracker()

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
    print("ADD HOMEWORK")
    subject = input ("Enter Homework's subject: ")
    title = input ("Enter Homework's title: ")
    score = float(input ("Enter your Homework's score: "))
    max_score = float(input ("Enter your Homework's maximum score: "))
    due_date = input ("Enter your Homework's due date (YYYY-MM-DD): ")
#Here the homework is created and user can input the details of the homework
    homework = Homework(subject, title, score, max_score, due_date)
#Function is called to add homework in the list of assignments
    tracker.add_assignment(homework)

def add_examination():
    print("ADD EXAMINATION")
    subject = input ("Enter Examination's subject: ")
    title = input ("Enter Examination's title: ")
    score = float(input ("Enter your Examination's score: "))
    max_score = float(input ("Enter your Examination's maximum score: "))
    due_date = input ("Enter your Examination's due date (YYYY-MM-DD): ")
#This creates an examination and user can put its details
    examination = Examination(subject, title, score, max_score, due_date)
#The examination function is called and added to assignments list
    tracker.add_assignment(examination)

def list_assignments():
    print("LIST OF ASSIGNMENT")
#To call list of assignments and display them
    tracker.list_assignments()

def filter_assignments():
    print("FILTER ASSIGNMENTS")
    print("1.By Type")
    print("2.By Subject")
    print("3.By Due Date")

    choice = input("Choose: ")
    if choice == "1":
        t = input ("Choose: Homework or Examination  ")
        for assignment in tracker.assignments:
            if assignment.assignment_type == t:
                print(assignment.subject, assignment.title, assignment.score, assignment.due_date)

    if choice =="2":
        s = input ("Type Subject: ")
        for assignment in tracker.assignments:
            if assignment.subject == s:
                print(assignment.subject, assignment.title, assignment.score, assignment.due_date)

    if choice =="3":
        d = input ("Enter due date(YYYY-MM-DD): ")
        for assignment in tracker.assignments:
            if assignment.due_date == d:
                print(assignment.subject, assignment.title, assignment.score, assignment.due_date)

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



