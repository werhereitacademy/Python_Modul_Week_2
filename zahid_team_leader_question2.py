# Question no 1 part 2
import sys
customers = {
    1001: {"name": "Ahmet", "surname": "Yilmaz", "email": "ahmet.yilmaz@example.com", "phone": "+905301112233"},
    1002: {"name": "Ayse", "surname": "Kaya", "email": "ayse.kaya@example.com", "phone": "+905301234567"},
    1003: {"name": "Mehmet", "surname": "Emir", "email": "mehmet.emir@example.com", "phone": "+905306789012"},
    1004: {"name": "Elif", "surname": "Aksoy", "email": "elif.aksoy@example.com", "phone": "+905308765432"},
    1005: {"name": "Zeynep", "surname": "Celik", "email": "zeynep.celik@example.com", "phone": "+905309876543"},
    1006: {"name": "Ali", "surname": "Kara", "email": "ali.kara@example.com", "phone": "+905304445566"},
    1007: {"name": "Fatma", "surname": "Yildiz", "email": "fatma.yildiz@example.com", "phone": "+905307778899"},
    1008: {"name": "Murat", "surname": "Aydin", "email": "murat.aydin@example.com", "phone": "+905302223344"},
    1009: {"name": "Hakan", "surname": "Oztiirk", "email": "hakan.oztiirk@example.com", "phone": "+905305556677"},
    1010: {"name": "Canan", "surname": "Tas", "email": "canan.tas@example.com", "phone": "+905309999000"}
}

menu = "Add new customers (Press 1)\nUpdating customer information ( Enter 2 ) \nDelete customer ( Enter 3 )\nList all customers ( Enter 4 )"
print(menu)
menu_choice = 0
try:
  menu_choice = int(input("Select a above numner to perform a action"))
except ValueError:
  print("Please enter only numbers")
  sys.exit()

def add_new_customer():
    try:
        fname = input("Enter your first name")
        sname = input("Enter your sur name")
        email = input("Enter your Email")
        phone = input("Enter your Phone")
        unique_id = max(sorted(customers.items()), key=lambda x: x[0])[0]+1
        customers.update({unique_id:{'name':fname,'surname':sname,'email':email,'phone':phone}})
        return customers
    except:
        print("There is some error")

def list_all_customer():
    try:
        for customer in customers:
            #print(customers[customer])
            print(f"Name: {customers[customer]['name']} {customers[customer]["surname"]} Email: {customers[customer]["email"]} Phone: {customers[customer]["phone"]}")
    except:
        return "Some Error in User List Printing"
    
def update_customer():
    try:
        id = int(input("Enter the Customer ID which you want to edit"))
        try:
            print(f"You are going to Change customer {customers[id]['surname']}")
            fname = input(f"Please Enter first name")
            sname = input(f"Please Enter sur name")
            email = input(f"Please Enter email")
            phone = input(f"Please Enter phone")
            if fname != "":
                customers[id]['name'] = fname
            if sname != "":
                customers[id]['surname'] = sname
            if email != "":
                customers[id]['email'] = email
            if email != "":
                customers[id]['phone'] = phone
            list_all_customer()
        except:
            return "Customer not find"
    except ValueError:
        return "Please enter numbers only"  
    
def delete_customer():
    id = int(input("Enter the Customer ID which you want to edit"))
    try:
        del customers[id]
        list_all_customer()       
    except ValueError:
        return "Please enter numbers only"  

def view_customer():
    return list_all_customer()
    
if menu_choice == 1:
    print(add_new_customer())
elif menu_choice == 2:
    print(update_customer())
elif menu_choice == 3:
    print(delete_customer())
elif menu_choice == 4:
    print(view_customer())
