userInfo={}
custInf={}
while True:
    userN=input('User Name ')
    pas=input('Password ')
    if (userN in userInfo and pas==userInfo[userN]):
        break
    elif userN not in userInfo:
        print ('User Name was not found, make a username and passwoord')
        userN=input('User Name ')
        pas=input('Password')
        userInfo[userN]=pas
        print("You made a username and password successfully !")
        break

while True:
    sel=input("\n---Customer Information Database---\n---Please Select an option---\n---List Customer information, L ---\n---Add Customer,A--- \n---Update Customer, U -----\n---Delete Customer, D ---\n---Quit Program, Q--").upper()
    if sel=="A":
        id=input("Customer ID ? ")
        ns=input ("Name and Surname ? ")
        tel=input ("Telephone? ")
        email=input ("E-mail? ")
        custInf[id]=[ns, tel,email]

    elif sel == "L":
        if custInf=={}:
            print("\nNo customers found ! ")
        else:
            for id,info in custInf.items():
                print(f"\n customer ID:{id}  Name and Surname:{info[0]}  Telephone:{info[1]}  E-mail :{info[2]}")


    elif sel == "U" :
        if custInf == {}:
            print("\nNo customers found ! ")
        else:
            for id,info in custInf.items():
                print(f" customer ID:{id}  Name and Surname:{info[0]}  Telephone:{info[1]}  E-mail :{info[2]}")

            ci=input('enter customer Id ? ')
            print(f" customer ID:{ci}  Name and Surname:{custInf[ci][0]}  Telephone:{custInf[ci][1]}  E-mail :{custInf[ci][2]}")
            sel=input("select customer data to be updated ? (for Name and Surname 0,| for Telephone 1,|  for E-mail 2,  ")
            
            if sel =="0":
                update=input('Name and Surname? ')
                (custInf[ci][0])=update
            
            elif sel =="1":
                update=input('Telephone? ')
                (custInf[ci][1])=update   
            
            if sel =="2":
                update=input('E-mail? ')
                (custInf[ci][2])=update      
    
    elif sel=='D':
        ci=input('enter customer Id to delete ? ')
        if ci not in custInf.keys():
             ci=input("Id doesn't exist, or wrong Id, enter customer Id again? ")
        else: 
            del custInf[ci]
            print ("Customer information was deleted from database")    
            
  
    elif sel=='Q':
            quit()
