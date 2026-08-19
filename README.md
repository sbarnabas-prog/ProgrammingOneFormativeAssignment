# Student Grade/Assignment Tracker
A program built in Python for the Programming 1 Formative Project which allows users to record homework and exam results, view and filter assignments and dispaly rade summaries in a single session. 

## Project Overview & Features
This program uses Object Oriented Programming to create assignments as objects not loose variables or dictionaries. It also supports the following:
- Adding assignments - record homework or exam results with subject, title, score, max score and due date.
- Listing assignments - view every assignment that has been recorded
- Filtering assignments - narrow the list down by assignment type, by subject, or by due date.
- Grade summary - calculate the percentage score for each assignment and the overall average across everything that has been recorded and gives back the overall status if it is in danger, good condition or pass.

### Class Structure
- Assignment - the base class which stores subject, title, score, max_score, due_date and assignment_type.
- Homework and examination - these are the sub classes of Assignment that inherit all its properties ad automatically set assignment_type to homework or examination respectively
- GradeTracker - holds th elist of all assignments and provides methods to add, list, filter and sumarize them. 

## How to run
1. Make sure Python is installed (python3 --version to check).
2. Then clone the following repository:
 git clone https://github.com/sbarnabas-prog/
 ProgramingOneFormativeAssignment.git
 cd ProgrammingOneFormativeAssignment
3. Run the program:
 python3 tracker.py
4. Follow the on-screen menu prompts.

No external libraries are required - the project only uses Python's standard library.

## Menu Structure
1. Add homework
2. Add examination
3. List assignments
4. Filter out by subject/type or due date
5. Show summary
0. Exit

When a user selects an option outside 0-5 an error message appears and returns the user to the menu rather than crashing the entire program.

## Sample Interaction

Select an option: 1
ADD HOMEWORK
Enter Homework's subject: Mathematics
Enter Homework's title: Calculus Worksheet
Enter your Homework score:90
Enter your Homework's maximum score: 100
Enter your Homework's due date (YYYY-MM-DD):2026-08-16

Select an option: 3
LIST ASSIGNMENTS
Subject is Mathematics, Title is Calculus Worksheet, Score is 80/100, Due Date is 2026-08-16, Type is Homework

## Screenshots
Add screenshots here showing the program running for each of the four core actions:
-Adding aan assignment
-Listing assignments
-Filtering assignments
-Showing the grade summary

## Repository Link
https://github.com/sbarnabas-prog/ProgrammingOneFormativeAssignment
2026-08-19

