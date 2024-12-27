### https://www.hackerrank.com/challenges/list-comprehensions/problem
if __name__ == '__main__':
    # Take input values for X, Y, Z, and N from the user
    X = int(input())  # Upper limit for the first dimension (x)
    Y = int(input())  # Upper limit for the second dimension (y)
    Z = int(input())  # Upper limit for the third dimension (z)
    N = int(input())  # Sum threshold, coordinates where x + y + z == N will be excluded
    
    # List comprehension to generate valid coordinates
    # It iterates over all values of x, y, and z within the specified range
    # and includes only those where x + y + z is not equal to N
    result = [[x, y, z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x + y + z != N]

    # Print the resulting list of coordinates
    print(result)
### https://www.hackerrank.com/challenges/python-tuples/problem
if __name__ == '__main__':  # This line checks if this script is being run directly (not imported as a module)
    
    n = int(input())  # Step 1: Get an integer input from the user, this is the count of numbers to be entered
    
    # Step 2: Input the space-separated integers from the user and convert them into a tuple
    integer_list = tuple(map(int, input().split()))  # The input is split into separate strings, converted to integers, and stored as a tuple
    
    # Step 3: Compute the hash value of the tuple
    result = hash(integer_list)  # The hash function creates a unique fixed-size hash value for the tuple
    
    # Step 4: Print the result
    print(result)  # Output the hash value
### https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':  # This checks if the script is being run directly (not imported as a module)
    
    # Step 1: Ask the user to input the number of students
    n = int(input())  # The user inputs a number that represents how many students there are

    # Step 2: Create an empty list to store student names and their grades
    students = []  # This list will hold sub-lists, where each sub-list is [name, grade]

    # A loop to get student names and grades
    for _ in range(n):  # Repeat n times (the number of students)
        name = input()  # Ask for the student's name
        grade = float(input())  # Ask for the student's grade and convert it to a decimal number
        students.append([name, grade])  # Add the [name, grade] pair to the students list

    # Step 3: Find all unique grades by using a set, then sort them
    grades = sorted(set([grade for name, grade in students]))  # Extract all grades, remove duplicates with set(), and sort

    # The second lowest grade is the second item in the sorted list
    second_lowest_grade = grades[1]  # Get the second lowest grade from the sorted list of grades

    # Step 4: Find all students who have the second lowest grade
    second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]  
    # We look through the students list and collect names of students with the second lowest grade

    # Step 5: Sort the names alphabetically
    for student in sorted(second_lowest_students):  # Sort the names alphabetically
        print(student)  # Print each student's name on a new line


