# Python_Modul_Week_2

# Library Project
- In this project, we want you to write a library program using the Python information you have learned so far, error catching - file operations, especially the Json module and file information.
- In a library; There are two main parts: Membership transactions and Book transactions.
- Membership transactions include information on adding a member, deleting a member, checking a member, giving a book to a member, and receiving a returned book from a member. A database or file where membership data is recorded is also required.
- We can say similar things about book transactions.
# 📚 Mini Book Management System

#### To detail the project:
 * It will consist of main.py, Kitap_transactions.py, Member_Transactions.py, Zaman.py files.
##### Main.py:
* The main file of our project will be the main.py file. Operations will be executed from this file, other Python files will be called from this section as a module. For example, adding a book, deleting a book, adding a member, giving a book to a member, and member control will be done here.
This project is a beginner-friendly book management system built with Python. It allows users to manage a collection of books through a simple command-line interface. All data is stored in a JSON file for persistence.

![image](https://github.com/user-attachments/assets/a27bdecd-d799-4868-8241-cd559c560747)
## 🚀 Features


- Add a book (interactive input for each field)
- Remove a book (by title)
- Update book details
- Search for a book (by title)
- List all books

* Below you will see a run output of this project. You can run the functions in the book_transactions and membership_transactions modules via inputs on the main page.
## 🗂️ Book Format

![image](https://github.com/user-attachments/assets/2d30ee9c-61f1-4f25-bc79-0047ddb20dd3)
Each book is stored in the following format inside the `books.json` file:

```json
{
  "title": "1984",
  "author": "George Orwell",
  "year": 1949,
  "genre": "Dystopian"
}
```

## 🛠️ Technologies Used

##### book_transactions.py :
* In this module, you will write book information (registered books and total number), add, delete, search and update functions. We will save our data in the book.json file. The Kitap.json file will be given to you (you can create it yourself if you wish). File control must be done with the Os Module. Below you can find function examples for book transactions, but you do not have to follow them, you can make your own planning.
- Python 3.x
- JSON module (built-in)

 ![image](https://github.com/user-attachments/assets/b348be3e-e595-4e4c-9e2d-7913b81404ae)
## 📁 File Structure

```
mini_book_system.py       # Main script
books.json                # Data file storing all books
```

* There is a lot of data in the Kitap.json file. We will work with the following data. We will use these as basis when adding new data or searching.
## 📌 Installation & Usage

 ![image](https://github.com/user-attachments/assets/8d10fede-3e71-49da-88ad-8bfef0941422)
1. Make sure Python 3 is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/yourUsername/mini_book_system.git
   ```
3. Run the script:
   ```bash
   python mini_book_system.py
   ```

## 📄 How It Works

##### Book.json :
sample output is as follows
When you run the program, you'll be presented with a menu:

![image](https://github.com/user-attachments/assets/3780f27f-bb09-4217-add2-33195611a27b)
```
1. Add a book
2. Remove a book
3. Update a book
4. Search for a book
5. List all books
6. Exit
```

### ➕ Add a Book

##### Membership_transactions.py:
* Here, operations such as member information (member names and total number of members), member updating, adding members, searching for members, deleting members, lending books and returning books will be performed. Additionally, members must be saved in the uye.Json file. When lending a book, it is absolutely
* - The date and time the book was lent and the date to return it after 2 weeks should be added and this information should be saved in the taksi.json file.
You will be prompted to enter each field one by one:

![image](https://github.com/user-attachments/assets/58ee969c-ea74-49bc-a03c-ee63e2ad4413)
```
Enter book title:
Enter author name:
Enter publication year:
Enter genre:
```

The book will be saved in `books.json`.

* We will do this from the py module when we create it ourselves.
* - After being saved in the taksi.json file, the loaned book should be deleted from Kitap.json so that it does not appear when someone else wants to buy it.
##### Note: You will create the user.json and tracking.json file yourself.
### ➖ Remove a Book

![image](https://github.com/user-attachments/assets/5990440f-ad1f-4610-9876-72567d88c6de)
You will be asked to enter the title of the book to remove. If found, it will be deleted from the JSON file.

### ✏️ Update a Book

* The data you will save to Uye.json should be as follows:
You can update any field of a book by entering its title and then choosing which field to modify.

 ![image](https://github.com/user-attachments/assets/476e0143-9948-4cb1-a835-c2516c02b838)
### 🔍 Search for a Book

Search by title. If found, the book's details will be displayed.

##### time.py :
* We lend our books to our members for 2 weeks. Therefore, we will record the time and date of the loan and the date when it should be returned, thanks to this module.
When we run this module, we want it to return the current time and the time 2 weeks later.
### 📋 List All Books

![image](https://github.com/user-attachments/assets/4edebd25-8af2-4410-83db-a04ed2a84069)
Displays all books currently stored in the JSON file.

## 🎯 Purpose

##### The data you will save in tracking.json should be as follows:
This project is ideal for Python learners who want to practice:

![image](https://github.com/user-attachments/assets/da7fc6ed-900e-4ac2-87fb-e374bdae41ef)
- File handling with JSON
- User input and validation
- Basic CRUD operations
- Modular and interactive programming

## 📬 Contribute

## Hackerrank Questions
Feel free to fork the project and submit pull requests to improve functionality or add new features!

1. Diagonal Difference: https://www.hackerrank.com/challenges/diagonal-difference/problem
---

2. Left Rotation: https://www.hackerrank.com/challenges/array-left-rotation/problem

3. Counter game: https://www.hackerrank.com/challenges/counter-game/problem

4. Time Delta: https://www.hackerrank.com/challenges/python-time-delta/problem
