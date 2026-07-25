
# Program uses numpy on a csv file
import numpy as np

# Makes numpy array from grades.csv then runs array through grade_analysis
def main():

    # Make numpy array from grades.csv and use header row as column names
    # Renames headers with spaces to underscores EX: 'Exam 1' -> 'Exam_1'
    grades = np.genfromtxt('grades.csv', dtype = None, delimiter = ',', names = True)

    # Print the first few rows of the dataset to understand its structure.
    print()
    print(grades[:3])

    # Call other functions to run score analysis
    grade_analysis(grades)

    # End of program


# Uses numpy to analyze each individual exam
def grade_analysis(grades):

    # Calculates and prints: mean, median, standard deviation, minimum, and maximum of scores.
    # For each individual exam
    for i in range(3):
        # Variable because numpy doesn't like operations in its place
        exam = i+1

        print()
        print('Exam', exam, 'statistics')
        print('Mean:', np.mean(grades['Exam_%d' %exam]))
        print('Median:', np.median(grades['Exam_%d' %exam]))
        print('Standard Deviation:', round(np.std(grades['Exam_%d' %exam]), 2))
        print('Minimum:', np.min(grades['Exam_%d' %exam]))
        print('Maximum:', np.max(grades['Exam_%d' %exam]))

    # Add all exam columns together
    exam1 = np.array(grades['Exam_1'])
    exam2 = np.array(grades['Exam_2'])
    exam3 = np.array(grades['Exam_3'])
    allExams = np.column_stack((exam1, exam2, exam3))

    # Calculates and prints: mean, median, standard deviation, minimum, and maximum of scores.
    # For all scores combined
    print()
    print('Total statistics (all exams combined)')
    print('Mean:', np.mean(allExams))
    print('Median:', np.median(allExams))
    print('Standard Deviation:', round(np.std(allExams), 2))
    print('Minimum:', np.min(allExams))
    print('Maximum:', np.max(allExams))

    # Calculates and prints number of students who passed & failed per exam (score >= 60 = pass)
    # Variables used as accumulators for all exams combined
    totalPassed = 0
    totalFailed = 0

    print()
    for test in range(3):
        # Variables for each individual exam calculations
        passed = 0
        failed = 0
        examNum = test +1

        # Goes through each score in exam
        for score in grades['Exam_%d' %examNum]:
            if score >= 60:
                passed += 1
                totalPassed += 1
            else:
                failed += 1
                totalFailed += 1

        # Prints results for individual exam
        print('For Exam %d: %d passed & %d failed' %(examNum, passed, failed))

    # Pass percentage of all exams
    passPercent = (totalPassed / 30) * 100
    print()
    print('The pass percentage across all exams is', str(passPercent) + '%')


# Calls main function for program to run
main()