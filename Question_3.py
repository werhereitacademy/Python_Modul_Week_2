"""
Question 3: Customer Management System

Project Description: This project involves you creating a customer management system that you can use to manage your customers and perform basic transactions. 
This system will have basic functions such as storing customer information, adding new customers, updating customer information, deleting customers 
and viewing the customer list. Here are the basic steps of the project:

1-Use a dictionary structure to store customer information. Assign a unique customer identification (ID) for each customer 
and associate customer information with this ID. You can use a dictionary containing information such as name, surname, e-mail, phone number for each customer.
2-Provide a menu where the user can choose the following actions:

* Add new customers
* Updating customer information
* Delete customer
* List all customers
* Check out

3-Perform the relevant action according to the user's choice. For example, when adding a new customer, get the required information from the user and add a new customer to the dictionary.
4-When updating customer information, view the current information using the customer ID and save the updated information.
5-In the customer deletion process, get the customer ID from the user and delete this customer from the dictionary.
6-In the process of listing all customers, view the list of existing customers.
7-Repeat the process until the user logs out.
"""

import os
custID = 0

# this is a examble dictionary.
# customer = {
#     1 :{
#         "customerID":1,
#         "firstname":"firstname",
#         "surname":"surname", 
#         "telnumber":190,
#         "adres":"adres",
#         "email":"ga@ff.com"
#         },
#     2 :{
#         "customerID":2,
#         "firstname":"firstname",
#         "surname":"surname", 
#         "telnumber":13,
#         "adres":"adres",
#         "email":"ggg@fh.com",
#         }
# }
customer = {}

def addNewCustomer(firstname ,surname,telnumber,email,adres)-> None:
        
        global custID
        custID += 1 
        customer[custID]= {
        
        "customerID": custID,
        "firstname": firstname,
        "surname": surname,
        "telnumber": telnumber,
        "adres": adres,
        "email": email
        
        }
        
        print(f"Customer with ID {custID} has been added.")

def updateCustomerInformation(custID, n_firstname :None,n_surname : None,n_telnumber:None,n_email:None,n_adres :None)-> None:
    
        customer[custID]['firstname'] = n_firstname
        customer[custID]['surname'] = n_surname
        customer[custID]['telnumber'] = n_telnumber
        customer[custID]['email'] = n_email
        customer[custID]['adres'] = n_adres


def deleteCustomer():
    pass


def listAllCustomers():
   print(customer)

def IDcheck(ID:int)-> int:

    while ID not in customer:
        
        print("Customer ID is not found in the system.")
        ID = int(input(" Enter your again customer ID number : "))
        
    else :
       
        print("Customer ID found in the system.")
        print(customer[ID])
        return ID
        
                
    


def checkOut():
    os._exit


def mainMenu():
    while True:
        print(
        """  
1.   Add new customers
2.   Updating customer information 
3.   Delete customer
4.   List all customers
5.   Check out   

        """
)#pay attention to this because it is not number but a string
        select = input("Enter your slection between 1 - 5 : ").strip() 
    
        if select == "1":

            n_firstname = input("Enter your first name :").strip() or None
            n_surname = input("Enter your  sur name :").strip() or None
            n_telnumber =int(input("Enter your telefoon :")) or None
            n_email = input("Enter your  email adres :").strip() or None
            n_adres = input("Enter your  hous adres :").strip() or None
            addNewCustomer(n_firstname ,n_surname,n_telnumber,n_email,n_adres)
            

        if select == "2" :
            custID = int( input(" Enter your customer ID number : "))
            ID = IDcheck(custID)

            n_firstname = input("Enter your first name :").strip() or None
            n_surname = input("Enter your  sur name :").strip() or None
            n_telnumber =int(input("Enter your telefoon :")) or None
            n_email = input("Enter your  email adres :").strip() or None
            n_adres = input("Enter your  hous adres :").strip() or None

            updateCustomerInformation(ID,n_firstname,n_surname,n_telnumber,n_email,n_adres)
            

        if select == "3":
            pass

        if select == "4" :
            listAllCustomers()


        if select == "5":
            break
        


    


if __name__  == "__main__":
    mainMenu()


# Telefon numarasi ile mail adresini eslestrerek id numarasini ekrana yazdir.

