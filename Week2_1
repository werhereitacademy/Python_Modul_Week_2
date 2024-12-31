"""
Question1: Student Grades Processing
You need to write a Python program to process a student's grades. The program needs to perform the following functions:

Store information and notes for 10 students using a dictionary. Let each student have their name, surname and grades (Midterm, Final and Oral grades). For example:

students = {
    "Ahmet Yılmaz": [85, 90, 78],       #Midterm: 85, Final: 90, Oral: 78
    'Mehmet Demir': [92, 88, 76],       #Midterm: 92, Final: 88, Oral: 76
    "Ayşe Kaya": [78, 89, 95],          #Midterm: 78, Final: 89, Oral: 95
    "Zeynep Çelik": [65, 70, 80],       #Midterm: 65, Final: 70, Oral: 80
    'Ali Kara': [50, 60, 55],           #Midterm: 50, Final: 60, Oral: 55
    'Fatma Yıldız': [88, 85, 90],       #Midterm: 88, Final: 85, Oral.: 90
    'Murat Aydın': [72, 68, 74],        #Midterm: 72, Final: 68, Oral: 74
    'Elif Aksoy': [95, 98, 88],         #Midterm: 95, Final: 90, Oral: 88
    "Hakan Öztürk": [45, 50, 55],       #Midterm: 45, Final: 50, Oral: 55
    "Canan Taş": [80, 75, 82]           #Midterm: 80, Final: 75, Oral: 82
}

1-Calculate each student's GPA and add it to the dictionary.

2-Find the student with the highest GPA and print it on the screen.

3- Separate each student's name from their surname and store them in a separate tuple and add them to a list.

4-Sort the names in alphabetical order and print the sorted list on the screen.

5-Keep students with a GPA below 70 in a cluster (set).
"""
import os

# Main program
if __name__ == "__main__":
    students = dict()
    grade_rates = [20, 60, 20]
    incorrectly_entered = False
    exit_confirmation = True
    while exit_confirmation :
        os.system("clear" if os.name == "posix" else "cls")
        main_menu = [
                "_____________________________________________________",
                "             Student Information System              ",
                "_____________________________________________________",
                "   (1) Student Adding Procedures.\n",
                "   (2) Student with the Highest Grade Point Average.\n",
                "   (3) Alphabetical Student List.\n",
                "   (4) List of students with a general average below 70.\n",
                f"   (s) Change the average calculation rates.(Midterm: %{(grade_rates[0]/sum(grade_rates) * 100):.2f} Final: %{(grade_rates[1]/sum(grade_rates) * 100):.2f} Oral: %{(grade_rates[2]/sum(grade_rates) * 100):.2f})\n",
                "   (q) You can exit the program by pressing.\n\n"
        ]

        for i in main_menu:
            print(i)

        if incorrectly_entered:
            print('\t'.expandtabs(5), "You have entered incorrectly. Please check the menu and make your selection again!")
            incorrectly_entered = False

        print('\t'.expandtabs(5), "Please select the action you wish to perform:", end=" ")
        select_menu = input()

        if select_menu in ["q", "Q"]:
            exit_confirmation = False
        elif select_menu == "1":
            exit_student_menu = True
            while exit_student_menu:
                os.system("clear" if os.name == "posix" else "cls")
                print(f"Name Surename: [Midterm: %{(grade_rates[0]/sum(grade_rates) * 100):.2f} Final: %{(grade_rates[1]/sum(grade_rates) * 100):.2f} Oral: %{(grade_rates[2]/sum(grade_rates) * 100):.2f}, GAB]\n",
                      "___________________________________________")
                for student,grade in students.items():
                    print(student," : ",grade)
                main_menu = main_menu = [
                        "_____________________________________________________",
                        "            Student Adding Procedures.               ",
                        "_____________________________________________________",
                        "   (1) Adding a Student.\n",
                        "   (2) Student Correction.\n",
                        "   (3) Student Deletion.\n",
                        "   (4) Add standard student list.\n",
                        "   (m) To return to the main menu.\n\n"
                ]
                for i in main_menu:
                    print(i)

                if incorrectly_entered:
                    print('\t'.expandtabs(5), "You have entered incorrectly. Please check the menu and make your selection again!")
                    incorrectly_entered = False

                print('\t'.expandtabs(5), "Please select the action you wish to perform:", end=" ")
                select_menu = input()
                if select_menu in ["m", "M"]:
                    exit_student_menu = False
                elif select_menu == "1":
                    new_student_name = input("Please enter the student's name: ")
                    new_student_surname = input("Please enter the student's surname: ")
                    if new_student_name+" "+ new_student_surname in students.keys():
                        print("This student already exists.")
                        input("Press enter to continue...")
                    else:
                        new_student_midterm = int(input("Please enter the student's midterm grade: "))
                        new_student_final = int(input("Please enter the student's final grade: "))
                        new_student_oral = int(input("Please enter the student's oral grade: "))
                        new_student_gab = round((new_student_midterm * grade_rates[0] + new_student_final * grade_rates[1] + new_student_oral * grade_rates[2]) / sum(grade_rates) , 2)
                        students[new_student_name+" "+ new_student_surname] =[new_student_midterm, new_student_final, new_student_oral, new_student_gab]
                        print("Student added successfully.")
                elif select_menu == "2":
                    edit_student_name = input("Please enter the student's name and surename you want to edit: ")
                    if edit_student_name in students.keys():
                        edit_student_midterm = int(input("Please enter the student's midterm grade: "))
                        edit_student_final = int(input("Please enter the student's final grade: "))
                        edit_student_oral = int(input("Please enter the student's oral grade: "))
                        edit_student_gab = round((edit_student_midterm * grade_rates[0] + edit_student_final * grade_rates[1] + edit_student_oral * grade_rates[2]) / sum(grade_rates) , 2)
                        students[edit_student_name] = [edit_student_midterm, edit_student_final, edit_student_oral, edit_student_gab]
                        print("Student edited successfully.")
                    else:
                        print("Student not found.")
                        input("Press enter to continue...")
                elif select_menu == "3":
                    delete_student_name = input("Please enter the student's name and surename you want to delete: ")
                    if delete_student_name in students.keys():
                        if True if input("Are you sure you want to delete the student? (Y/N): ") in ["y","Y"] else False:
                            del students[delete_student_name]
                            print("Student deleted successfully.")
                        else:
                            print("Student deletion canceled.")
                            input("Press enter to continue...")
                    else:
                        print("Student not found.")
                        input("Press enter to continue...")
                elif select_menu == "4":
                    confirmation = True if input("Are you sure you want to add the standard student list? (Y/N): ") in ["y","Y"] else False 
                    if confirmation:
                        students = {
                            "Ahmet Yılmaz": [85, 90, 78,round((85 * grade_rates[0] + 90 * grade_rates[1] + 78 * grade_rates[2]) / sum(grade_rates) , 2)],       
                            'Mehmet Demir': [92, 88, 76,round((92 * grade_rates[0] + 88 * grade_rates[1] + 76 * grade_rates[2]) / sum(grade_rates) , 2)],      
                            "Ayşe Kaya": [78, 89, 95,round((78 * grade_rates[0] + 89 * grade_rates[1] + 95 * grade_rates[2]) / sum(grade_rates) , 2)],         
                            "Zeynep Çelik": [65, 70, 80,round((65 * grade_rates[0] + 70 * grade_rates[1] + 80 * grade_rates[2]) / sum(grade_rates) , 2)],      
                            "Ali Kara": [50, 60, 55,round((50 * grade_rates[0] + 60 * grade_rates[1] + 55 * grade_rates[2]) / sum(grade_rates) , 2)],          
                            "Fatma Yıldız": [88, 85, 90,round((88 * grade_rates[0] + 85 * grade_rates[1] + 90 * grade_rates[2]) / sum(grade_rates) , 2)],      
                            "Murat Aydın": [72, 68, 74,round((72 * grade_rates[0] + 68 * grade_rates[1] + 74 * grade_rates[2]) / sum(grade_rates) , 2)],       
                            "Elif Aksoy": [95, 98, 88,round((95 * grade_rates[0] + 98 * grade_rates[1] + 88 * grade_rates[2]) / sum(grade_rates) , 2)],        
                            "Hakan Öztürk": [45, 50, 55,round((45 * grade_rates[0] + 50 * grade_rates[1] + 55 * grade_rates[2]) / sum(grade_rates) , 2)],      
                            "Canan Taş": [80, 75, 82,round((80 * grade_rates[0] + 75 * grade_rates[1] + 82 * grade_rates[2]) / sum(grade_rates) , 2)]
                        }

                else:
                    incorrectly_entered = True
        elif select_menu == "2":
            max_student = list()
            max_grade = 0
            for student,grade in students.items():
                if len(max_student) == 0:
                    max_student.append(student)
                    max_grade = grade[3]
                elif grade[3] == max_grade:
                    max_student.append(student)
                elif grade[3] > max_grade:
                    max_student = [student]
                    max_grade = grade[3]
            print(max_student," Max Grade: ",max_grade)
            input("Press enter to continue...")
        elif select_menu == "3":
            alfabetic_students = list()
            unsorted_students = list()
            for student in students.keys():
                student_tuple = tuple(student.split(" "))
                unsorted_students.append(student_tuple)
            alfabetic_students = sorted(unsorted_students, key=lambda x: x[0])
            for student in alfabetic_students:
                print(student)
            input("Press enter to continue...")
        elif select_menu == "4":
            less_gab_students = set()
            for student,grade in students.items():
                if grade[3] < 70:
                    less_gab_students.add(student)
            for student in less_gab_students:
                print(student)
            input("Press enter to continue...")
        elif select_menu in ["s", "S"]:
            print("The value you enter for each grade will be taken as a multiplier. For example, if you enter the same value for all three, all grades will be evaluated equally. \n Please enter the new grade rates.")
            grade_rates[0] = float(input("Please enter the new midterm grade rate: "))
            grade_rates[1] = float(input("Please enter the new final grade rate: "))
            grade_rates[2] = float(input("Please enter the new homework grade rate: "))
            for student,grade in students.items():
                students[student][3] = round((grade[0] * grade_rates[0] + grade[1] * grade_rates[1] + grade[2] * grade_rates[2]) / sum(grade_rates) , 2)
        else:
            incorrectly_entered = True
