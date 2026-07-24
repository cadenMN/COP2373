
# Program makes a csv file and reads it
import csv

# Make a csv file using student information: first name, last name, and grades for 3 exams
def csv_maker():

    # Get number of instances to be added to csv file
    numStudents = int(input("How many students are you entering grades for? "))

    # Get student information as a list and add it to a list of all students
    grades = []
    print()
    print('Enter grades as a whole number')
    for i in range(numStudents):
        print()
        print('Student', i + 1)
        studentInfo = []
        studentInfo.append(input("Student first name: "))
        studentInfo.append(input("Student last name: "))
        studentInfo.append(int(input("Student Exam 1 grade: ")))
        studentInfo.append(int(input("Student Exam 2 grade: ")))
        studentInfo.append(int(input("Student Exam 3 grade: ")))
        grades.append(studentInfo)

    # Create csv file and add student information
    with open('grades.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Header row with titles of each column
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])
        # Adds row of student information for each student given
        for i in range(numStudents):
            writer.writerow(grades[i])

    csv_reader()
    # End of function

# Function reads csv file created
def csv_reader():
    print()
    with open('grades.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)

        # Creates tabular format with just spacing between columns
        for row in reader:
            print('%-20s %-20s %-20s %-20s %-20s' % tuple(row))


# Calls csv_maker for program to start
csv_maker()