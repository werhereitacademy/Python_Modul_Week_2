#Question 3
customers_information={}

def display_menu():
    print('1. Add new customers')
    print('2.Updating customer information')
    print('3.Delete customer')
    print('4.List all customers')
    print('5.Check out')

def add_customer():
    id=input('Enter unique customer ID: ')
    name=input('enter customer name: ')
    surname=input('Enter customer surname: ')
    email=input('Enter customer e-mail: ')
    phone_number=input('Enter customer phone number: ')
    customers_information[id]={
                               'Name':name,
                               'Surname':surname,
                               'Email':email,
                               'Phone_number':phone_number
                               }
    
def updating_customer_information():
    id=input('enter customer ID to update: ')
    if id in customers_information:
        name=input('Enter new name / leave blank to keep current: ')
        surname=input('Enter customer surname / leave blank to keep current: ')
        email=input('Enter customer e-mail / leave blank to keep current: ')
        phone_number=input('Enter customer phone number / leave blank to keep current: ')
        if name:
            customers_information[id]['Name']=name
            print('Update name is succesful! ')
        if surname:
            customers_information[id]['Surname']=surname
            print('Update surname is succesful!')
        if email:
            customers_information[id]['Email']=email
            print('Update email is succesful!')
        if email:
            customers_information[id]['Phone_number']=phone_number
            print('Update phone number is succesful!')
    else:
        print(' Customer is not found ')

def delete_customer():
    id = input ('Enter ID customer to delete: ')
    if id in customers_information:
        del customers_information[id]
        print('delete customer is succesful! ')
    else:
        print('customer is not found')

def list_all_customers():
    if customers_information:
        for id,info in customers_information.items():
            print('ID: ',id ,'-','Info: ', info)
    else: 
        print('no customers available')
        
while True:
    display_menu()
    choise=input('Enter your choise: ')
    if choise=='1':
        add_customer()
    elif choise=='2':
        updating_customer_information()
    elif choise=='3':
        delete_customer()
    elif choise=='4':
        list_all_customers()
    elif choise=='5':
        print('Exiting the system ')
        break
    else:
        print('Invalid choise, Try again!')
