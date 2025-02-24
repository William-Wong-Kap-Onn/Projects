#HomePage
car_column = ["CarID", "CarPlate", "Brand", "Model", "ManuYr", "SeatCap", "LastServ", "InsuPolNo", "InsuExp","RoadTaxExp", "RentStart", "RentReturn", "RentRatePD", "Availability"]
cus_column = ["CusID", "CusName", "NRIC", "Passport", "License", "Address", "Phone", "RegDate"]

from datetime import datetime
import time

#Manager (Tan Yen Hann TP073629)
# User File
try:
    with open("users.txt", "r") as user_file:
        data = user_file.read()
        if not data:
            with open("users.txt", "a") as user_file:
                user_file.write("")
                user_file.close()
except FileNotFoundError:
    with open("users.txt", "a") as user_file:
        user_file.write("")
        user_file.close()

# Customer File
try:
    with open("cusinfo.txt", "r") as cus_file:
        data = cus_file.read()
        if not data:
            with open("cusinfo.txt", "a") as cus_file:
                cus_file.write("")
                cus_file.close()
except FileNotFoundError:
    with open("cusinfo.txt", "a") as cus_file:
        cus_file.write("")
        cus_file.close()

# Car File
try:
    with open("carinfo.txt", "r") as car_file:
        data = car_file.read()
        if not data:
            with open("carinfo.txt", "a") as car_file:
                car_file.write("")
                car_file.close()
        car_file.close()
except FileNotFoundError:
    with open("carinfo.txt", "a") as car_file:
        car_file.write("")
        car_file.close()

# Main
def main_page():
    print("#######################################################")
    print ("\n*******WELCOME TO Super Crazy CAR RENTAL SERVICE*******\n")
    print ("#######################################################")
    print ()
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = input("Enter choice : ")
    if choice == "1":

        allusers = []
        with open("users.txt", "r") as user_file:
            for data in user_file:
                user_data = data.strip().split(",")
                allusers.append(user_data)
            user_file.close()
        user = login(allusers)

        if len(user) > 0:
            if user[3] == "car_s":
                crss(user, allusers)
            elif user[3] == "cus_s_I":
                cssI_page(user, allusers)
            elif user[3] == "cus_s_II":
                cssI_page(user, allusers)
            elif user[3] == "manager":
                update_profile(user, allusers)
        else:
            print("System has been disable for 1 minutes")
            time.sleep(60)
    
    elif choice == "2":
        register()
    elif choice == "3":
        print ()
        print("You have exited the program.")
        exit()
    else:
        print ()
        print ("Invalid Input.\n")
        main_page()

# Login
def login(alluser):

    flag = False
    for cnt in range(3):
        username = input("Enter username : ")
        password = input("Enter password : ")

        for i in range(len(alluser)):
            if username == alluser[i][0] and password == alluser[i][2]:
                user = alluser[i]
                flag = True
        if flag == True:
            break
        else:
            print("Incorrect username or password. Attempts left:", 2 - cnt)

    if flag == False:
        user = []
    return user

# Register
def register():
    username = input("Enter Username : ")
    name = input("Enter Name : ")
    password = input("Enter Password : ")
    reen_pass = input("Reenter Password : ")

    while password != reen_pass:
        print("Password not match")
        reen_pass = input("Reenter Password : ")

    print("Role")
    print("1. Car Service Staff \t 2. Customer Service Staff I \t 3. custemor service staff II\t 4. Manager")
    role = input("Enter role number : ")
    if role == "1":
        user_role = "car_s"
    elif role == "2":
        user_role = "cus_s_I"
    elif role == "3":
        user_role = "cus_s_II"
    elif role == "4":
        user_role = "manager"
    else:
        print()
        print("Invalid Input.\n")
        register()

    current_time =  datetime.datetime.now()

    with open("users.txt", "a") as user_file:
        user_file.write(f"{username},{name},{password},{user_role},{current_time}\n")
        user_file.close()
        print("Account Registered")

# Update Profile
def update_profile(user, alluser):
    print(f"Username : {user[0]}")
    print(f"Name     : {user[1]}")
    print(f"Password : {user[2]}")
    print("---------------------")
    print("1. Username")
    print("2. Name")
    print("3. Password")
    choice = input("Enter Choice : ")
    if choice == "1":
        prev_un = user[0]
        new_un = input("Enter new username : ")
        user[0] = new_un
        with open("users.txt", "w") as user_file:
            for i in range(len(alluser)):
                if alluser[i][0] == prev_un:
                    alluser[i][0] = new_un
                    user_file.write(",".join(alluser[i]) + "\n")
                else:
                    user_file.write(",".join(alluser[i]) + "\n")
        print("Username changed sucessfully")

    elif choice == "2":
        prev_n = user[1]
        new_n = input("Enter new name : ")
        user[1] = new_n
        with open("users.txt", "w") as user_file:
            for i in range(len(alluser)):
                if alluser[i][1] == prev_n:
                    alluser[i][1] = new_n
                    user_file.write(",".join(alluser[i]) + "\n")
                else:
                    user_file.write(",".join(alluser[i]) + "\n")
        print("Name changed successfully")

    elif choice == "3":
        prev_pass = user[2]
        new_pass = input("Enter new password : ")
        user[2] = new_pass
        with open("users.txt", "w") as user_file:
            for i in range(len(alluser)):
                if alluser[i][2] == prev_pass:
                    alluser[i][2] = new_pass
                    user_file.write(",".join(alluser[i]) + "\n")
                else:
                    user_file.write(",".join(alluser[i]) + "\n")
        print("Password changed successfully")
    else:
        print ()
        print ("Invalid Input.\n")
        update_profile()

# Delete User
def dlt_user(user, alluser):
    print("dlt user")
    print("Enter username to search : ")
    username = input("Enter Username : ")

    with open("users.txt", "w") as user_file:
        for i in range(len(alluser)):
            if username == alluser[i][0]:
                print("user has been deleted")
            else:
                user_file.write(",".join(alluser[i]) + "\n")
    update_profile(user, alluser)

#CSSIRole (Tan Yi Han TP070378)
def cssI_page(user, alluser):
    print("Welcome to the CSSI menu.")
    print("Please select the options below:")
    print("\t1. Register Customer Details \n\t2. Update Customer Details \n\t3. View Customer List \n\t4. Delete Customer Details")
    print("\t5. View Rental Transactions by Date\n\t6. Record Rental Details\n\t7. Check For Car Availability\n\t8. Back")

    cssI_Choice = input("Please enter the option shown above: ")

    if cssI_Choice == "1":
        print()
        reg_cus(user, alluser)

    elif cssI_Choice == "2":
        print()
        upd_cus(user, alluser)

    elif cssI_Choice == "3":
        print()
        view_cus(user, alluser)

    elif cssI_Choice == "4":
        print ()
        delete_cus(user, alluser)
    
    elif  cssI_Choice== "5":
        print ()
        view_rental_transactions_by_date(user, alluser) 

    elif cssI_Choice == "6":
        print ()
        record_rental_details(user, alluser)

    elif cssI_Choice == "7":
        print ()
        check_car_availability(user, alluser)

    elif cssI_Choice == "8":
        print ()
        main_page()

    else:
        print("\n*******Invalid Input*******\n")
        print("***Please try again.***")
        print()
        cssI_page(user, alluser)

def reg_cus(user, alluser):
    cusinfo = []
    cuslist = open('cusinfo.txt', 'r')
    for line in cuslist:
        line = line.rstrip()
        cusinfo.append(line.split(','))
    cuslist.close()
    cus_detail = []
    print ("Please register the following customer details:")
    cusid = len(cusinfo) + 1
    cusid = str(cusid)
    cus_detail.append(cusid)
    cus_Name = input ("Customer Name: ")
    cus_detail.append(cus_Name.upper())
    cus_NRIC = (input ("Customer NRIC No.(If foreigner enter null): "))
    cus_detail.append(cus_NRIC.upper())
    cus_Passport = input ("Customer Passport No.(If local enter null): ")
    cus_detail.append(cus_Passport.upper())
    cus_License = (input ("Customer License No.: "))
    cus_detail.append(cus_License.upper())
    cus_Address = input ("Customer Address: ")
    cus_detail.append(cus_Address.upper())
    cus_Phone = (input ("Customer Phone No.: "))
    cus_detail.append(cus_Phone.upper())
    cus_regDate = input ("Register Date: ")
    cus_detail.append(cus_regDate.upper())
    

    print("Customer detail:")
    print(cus_detail)

    cfm_cusdetail = input("Confirm Customer detail? (Y/N): ")

    if cfm_cusdetail.upper() == "Y":
        cusinfo.append(cus_detail)
        with open('cusinfo.txt','w') as cuslist:
            for row in cusinfo:
                for item in row:
                    for chr in str(item):
                        cuslist.write(chr)
                    if item != row[-1]:
                        cuslist.write(',')
                cuslist.write('\n')
            cuslist.close()

        print("\nCustomer detail is successfully added to the system.")
        print ("\nUpdated customer list:")
        for cus_list in (cusinfo):
            print(cus_list)

    else:
        print("\nCustomer detail is not added to system.")
    returnCssIpage = cssI_page(user, alluser)
    returnCssIpage = input("Press enter to return to CSSI menu: ")
    return returnCssIpage

def upd_cus(user, alluser):
    cusinfo = []
    cuslist = open('cusinfo.txt', 'r')
    for line in cuslist:
        line = line.rstrip()
        cusinfo.append(line.split(','))
    cuslist.close()
    print ("Welcome to customer detail update page.\n")
    print ("Customer List: \n")
    print (cus_column)
    for i in (cusinfo):
        print (i)
    print("Please enter the Cus ID of the customer that you wish the update.")
    cus_location = input("Enter Cus ID:")
    cus_location = int(cus_location) - 1
    upd_cus = (cusinfo[cus_location])
    print ("\nCustomer detail:\n")
    print (cus_column)
    print (upd_cus)

    print("\nSelect the option you want to update:")
    print ("1. Cus ID\n2. Name\n3. NRIC\n4. Passport\n5. License\n6. Address\n7. Phone\n8. RegDate")
    upd_cusdetail = input("Enter option: ")
    upd_cusdetail = int(upd_cusdetail) - 1
    cus_detail = upd_cus[upd_cusdetail]
    print ("\ncurrent detail:", cus_detail)
    upd_detail = input("Enter new value:")
    upd_cus[upd_cusdetail] = upd_detail
    print ("\nUpdated customer detail:")
    print (upd_cus)
    print ("\nUpdated customer list:")
    for i in (cusinfo):
        print (i)
    
    print()
    cfm_cusdetail = input("Confirm update customer detail into system?(Y/N): ")

    if cfm_cusdetail.upper() == "Y":
        with open('cusinfo.txt','w') as cuslist:
            for row in cusinfo:
                for item in row:
                    for chr in str(item):
                        cuslist.write(chr)
                    if item != row[-1]:
                        cuslist.write(',')
                cuslist.write('\n')
            cuslist.close()

        print("\nCustomer detail is successfully updated to the system.")

    else:
        print("\nCustomer detail is not updated to system.")
    returnCssIpage = cssI_page(user, alluser)
    returnCssIpage = input("Press enter to return to CSSI menu: ")
    return returnCssIpage

def view_cus(user, alluser):
    print()
    print("Welcome to the view menu.")
    print("\nSelect options:")
    print("\t1. View Customer List \n\t2. Back")

    view_choice = input("Enter option: ")

    if view_choice == "1":
        print()
        view_cuslist(user, alluser)

    elif view_choice == "2":
        print()
        cssI_page(user, alluser)
    
    else:
        print("\n*******Invalid Input*******\n")
        print("***Please try again.***")
        print()
        view_cus(user, alluser)

def view_cuslist(user, alluser):
    cusinfo =[]
    cuslist = open('cusinfo.txt', 'r')
    for line in cuslist:
        line = line.rstrip()
        cusinfo.append(line.split(','))
    cuslist.close()
    for cus_list in (cusinfo):
        print (cus_list)
    
    returnCssIpage = cssI_page(user, alluser)
    returnCssIpage = input("Press enter to return to CSSI menu: ")
    return returnCssIpage

def delete_cus(user, alluser):
    cusinfo =[]
    cuslist = open('cusinfo.txt', 'r')
    for line in cuslist:
        line = line.rstrip()
        cusinfo.append(line.split(','))
    cuslist.close()
    print()
    print("\nCustomer details to be deleted: \n")
    print(cus_column)
    for i in range(len(cusinfo)):
        if cusinfo[i][7] == "No Transaction":
            print(cusinfo[i])
    cfm_deletecus = input("Are you sure you want to delete this customer? (Y/N): ")
    if cfm_deletecus.upper() == "Y":
        cusinfo.remove(cusinfo[i])
        with open('cusinfo.txt','w') as cuslist:
            for row in cusinfo:
                for item in row:
                    for chr in str(item):
                        cuslist.write(chr)
                    if item != row[-1]:
                        cuslist.write(',')
                cuslist.write('\n')
            cuslist.close()

        print("\nCustomer detail is successfully deleted from the system.")
        print ("\nUpdated customer list:")
        for cus_list in (cusinfo):
                print(cus_list)

    else:
        print ("Customer details failed to be deleted from system.")
   
    returnCssIpage = cssI_page(user, alluser)
    returnCssIpage = input("Press enter to return to CSSI menu: ")
    return returnCssIpage

import datetime

#Car Service Staff (Wong Kap Onn TP074292)
def crss(user, alluser):
    print("Welcome to the Car Service Staff menu.")
    print("Please select the options below:")
    print("\t1. Add car details \n\t2. Modify car details \n\t3. View car \n\t4. Delete Car \n\t5. Back")
    

    crss_choice = input("Please enter the option shown above: ")

    if crss_choice == "1":
        print()
        add_car(user, alluser)

    elif crss_choice == "2":
        print()
        modify_car(user, alluser)

    elif crss_choice == "3":
        print()
        view_car(user, alluser)

    elif crss_choice == "4":
        print ()
        delete_car(user, alluser)
 
    elif crss_choice == "5":
        print()
        main_page()
    
    else:
        print("\n*******Invalid Input*******\n")
        print("***Please try again.***")
        print()
        crss(user, alluser)

def add_car(user, alluser):
    carinfo = []
    carlist = open('carinfo.txt', 'r')
    for line in carlist:
        line = line.rstrip()
        carinfo.append(line.split(','))
    carlist.close()
    car_detail = []
    print ("Welcome to the add car page.")
    print ("Please add the following car details:")
    carid = len(carinfo) + 1 #auto generate carid based on the length of the list.
    carid = str(carid)
    car_detail.append(carid)
    Car_plate = input ("Car Registration No: ")
    car_detail.append(Car_plate.upper())
    Car_Manufacturer = (input ("Car Manufacturer: "))
    car_detail.append(Car_Manufacturer.upper())
    Car_Model = input ("Car Model: ")
    car_detail.append(Car_Model.upper())
    Manufacturer_Year = input("Year of Manufacturer: ")
    car_detail.append(Manufacturer_Year.upper())
    Seat_Capacity = input(("Seating Capacity: "))
    car_detail.append(Seat_Capacity.upper())
    Last_Service_Date = input("Last service date (DD/MM/YY): ") 
    car_detail.append(Last_Service_Date.upper())
    InsurancePol_No = input("Insurance Policy Number: ")
    car_detail.append(InsurancePol_No.upper())
    InsuranceExp_Date = input("Insurance Expiry Date (DD/MM/YY): ")
    car_detail.append(InsuranceExp_Date.upper())
    RoadTaxExp_Date = input("Road Tax Expiry Date (DD/MM/YY): ")
    car_detail.append(RoadTaxExp_Date.upper())
    Rent_StartDate = input("Rent Start Date (DD/MM/YY): ")
    car_detail.append(Rent_StartDate.upper())
    Rent_ReturnDate = input("Rent Return Date (DD/MM/YY): ")
    car_detail.append(Rent_ReturnDate.upper())
    Renting_Rate_Day = input("Car Renting Rate per day (RM): ")
    car_detail.append(Renting_Rate_Day.upper())
    Availability = input("Rental Availability: ")
    car_detail.append(Availability.upper())
    #Every variable is capitalize for greater ease.

    print("Car detail:")
    print(car_detail)

    cfm_detail = input("Confirm add car detail into system?(Y/N): ")

    if cfm_detail.upper() == "Y":
        carinfo.append(car_detail)
        with open('carinfo.txt','w') as carlist:
            for row in carinfo:
                for item in row:
                    for chr in str(item):
                        carlist.write(chr)
                    if item != row[-1]:
                        carlist.write(',')
                carlist.write('\n')
            carlist.close()

        print("\nCar detail is successfully added to the system.")
        print ("\nUpdated car list:")
        for car_list in (carinfo):
            print(car_list)

    else:
        ("\nCar detail is not added to system.")
    
    print()
    returnpage = input("Press enter to return to admin menu: ")
    crss(user, alluser)

def modify_car(user, alluser):
    carinfo = []
    carlist = open('carinfo.txt', 'r')
    for line in carlist:
        line = line.rstrip()
        carinfo.append(line.split(','))
    carlist.close()
    print ("Welcome to the modify page.\n")
    print ("Car List: \n")
    print (car_column)
    for i in (carinfo):
        print (i)
    print("Please enter the car id of the car that you wish the modify.")
    car_location = input("Enter Car Id:")
    car_location = int(car_location) - 1 #Since car id is length of list + 1.
    mod_car =  (carinfo[car_location]) #To find the car through the use of index.
    print ("\nCar detail:\n")
    print (car_column)
    print (mod_car)

    print("\nSelect the option you want to change:")
    print ("1. Car ID\n2. Car Plate\n3. Car Manufacturer\n4. Car Model\n5. Manufacture Year\n6. Seat Capacity\n7. Last Service Date\n8. Insurance Policy No\n9. Insurance Expiry Date\n10. Road Tax Expiry Date\n11. Rent Start Date\n12. Rent Return Date\n13. Rent Rate Per Day\n14. Availability")
    mod_cardetail = input("Enter option: ")
    while mod_cardetail != "1" and mod_cardetail != "2" and mod_cardetail != "3" and mod_cardetail != "4" and mod_cardetail != "5" and mod_cardetail != "6" and mod_cardetail != "7" and mod_cardetail != "8" and mod_cardetail != "9" and mod_cardetail != "10" and mod_cardetail != "11" and mod_cardetail != "12" and mod_cardetail != "13" and mod_cardetail != "14":
        print ()
        mod_cardetail = input("Enter option provided: ")
    mod_cardetail = int(mod_cardetail) - 1 #As the first element of the list starts at 0.
    cur_detail = mod_car[mod_cardetail] #To find the specific element of the specific car list.
    print ("\ncurrent detail:", cur_detail)
    upd_detail = input("Enter new value:")
    upd_detail = upd_detail.upper()
    mod_car[mod_cardetail] = upd_detail #Replace the current value of the index of the list mod_car to the new value which is variable upd_detail.
    print ("\nUpdated car detail:")
    print (mod_car)
    print ("\nUpdated car list:")
    for i in (carinfo):
        print (i)
    
    print()
    cfm_detail = input("Confirm update car detail into system?(Y/N): ")

    if cfm_detail.upper() == "Y":
        with open('carinfo.txt','w') as carlist:
            for row in carinfo:
                for item in row:
                    for chr in str(item):
                        carlist.write(chr)
                    if item != row[-1]:
                        carlist.write(',')
                carlist.write('\n')
            carlist.close()

        print("\nCar detail is successfully updated to the system.")

    else:
        print("\nCar detail is not updated to system.")
    
    print ()
    returnpage = input("Press enter to return to admin menu: ")
    crss(user, alluser)

def view_car(user, alluser):
    print()
    print("Welcome to the view menu.")
    print("\nSelect options:")
    print("\t1. All record \n\t2. Available for Rent \n\t3. Rented \n\t4. Search \n\t5. Back")

    view_choice = input("Enter option: ")

    if view_choice == "1":
        print()
        view_allcar(user, alluser)

    elif view_choice == "2":
        print()
        view_availablecar(user, alluser)

    elif view_choice == "3":
        print()
        view_rentedcar(user, alluser)
    
    elif view_choice == "4":
        print()
        view_specificcar(user, alluser)

    elif view_choice == "5":
        print()
        crss(user, alluser)
    
    else:
        print("\n*******Invalid Input*******\n")
        print("***Please try again.***")
        print()
        view_car(user, alluser)

def view_allcar(user, alluser):
    carinfo = []
    carlist = open('carinfo.txt', 'r')
    for line in carlist:
        line = line.rstrip()
        carinfo.append(line.split(','))
    carlist.close()
    print ("\nCar List:\n")
    print (car_column)
    for car_list in (carinfo):
        print (car_list)
    
    returnpage = input("Press enter to return to view menu: ")
    view_car(user, alluser)

def view_availablecar(user, alluser):
    carinfo = []
    carlist = open('carinfo.txt', 'r')
    for line in carlist:
        line = line.rstrip()
        carinfo.append(line.split(','))
    carlist.close()
    print("\nAvailable Car to rent:\n")
    print(car_column)
    for i in range(len(carinfo)):
        if carinfo[i][13] == "AVAILABLE": #To only print the list that contains AVAILABLE in the 13th index of the list.
            print(carinfo[i])
    
    returnpage = input("Press enter to return to view menu: ")
    view_car(user, alluser)

def view_rentedcar(user, alluser):
    carinfo = []
    carlist = open('carinfo.txt', 'r')
    for line in carlist:
        line = line.rstrip()
        carinfo.append(line.split(','))
    carlist.close()
    print("\nRented Car:\n")
    print(car_column)
    for i in range(len(carinfo)):
        if carinfo[i][13] == "RENTED": #To only print the list that contains RENTED in the 13th index of the list.
            print(carinfo[i])
    
    returnpage = input("Press enter to return to view menu: ")
    view_car(user, alluser)

def view_specificcar(user, alluser):
    carinfo = []
    carlist = open('carinfo.txt', 'r')
    for line in carlist:
        line = line.rstrip()
        carinfo.append(line.split(','))
    carlist.close()
    print()
    print ("Welcome to view specific car page.")
    search_info = input("Enter Car Plate: ") 
    print("\nCar Detail: \n")
    print(car_column)
    for i in range(len(carinfo)):
        if carinfo[i][1] == search_info: #To only print the list that contains the user input data in the 1st index of the list.
            print(carinfo[i])
    
    print ()
    returnpage = input("Press enter to return to view menu: ")
    view_car(user, alluser)

def delete_car(user, alluser):
    carinfo = []
    carlist = open('carinfo.txt', 'r')
    for line in carlist:
        line = line.rstrip()
        carinfo.append(line.split(','))
    carlist.close()
    print()
    print("\nCar to be disposed:\n")
    print(car_column)
    for i in range(len(carinfo)):
        if carinfo[i][13] == "DISPOSED": #To only print the list that contains DISPOSED in the 13th index of the list.
            print(carinfo[i])
    cfm_delete = input("Are you sure you want to delete this car? (Y/N): ")
    if cfm_delete.upper() == "Y":
        carinfo.remove(carinfo[i]) #To remove the list from the master list.
        with open('carinfo.txt','w') as carlist:
            for row in carinfo:
                for item in row:
                    for chr in str(item):
                        carlist.write(chr)
                    if item != row[-1]:
                        carlist.write(',')
                carlist.write('\n')
            carlist.close()

        print("\nCar detail is successfully deleted from the system.")
        print ("\nUpdated car list:")
        for car_list in (carinfo):
                print(car_list)

    else:
        print ("Car failed to delete from system.")
    
    returnpage = input("Press enter to return to admin menu: ")
    crss(user, alluser)

#CSSIIRole (Timothy Tan Chern Tian TP074658)
def load_car_data(file_path):
    car_data = []
    with open(file_path, "r") as file:
        for line in file:
            car_info = line.strip().split(',')
            if car_info[0].isdigit():
                car_data.append({
                    "carid": int(car_info[0]),
                    "carplate": car_info[1],
                    "brand": car_info[2],
                    "model": car_info[3],
                    "manufactureryear": int(car_info[4]),
                    "seatcapacity": int(car_info[5]),
                    "lastservice": car_info[6],
                    "insurancepolicyno": car_info[7],
                    "insuranceexpirydate": car_info[8],
                    "roadtaxExpirydate": car_info[9],
                    "RentStartDate": car_info[10] if car_info[10] else None,
                    "RentReturnDate": car_info[11] if car_info[11] else None,
                    "Rentperday": float(car_info[12]),
                    "availability": car_info[13]
                })
    return car_data

car_data = load_car_data("carinfo.txt")

def view_rental_transactions_by_date(user, alluser):
    carinfo = []
    carlist = open('carinfo.txt', 'r')
    for line in carlist:
        line = line.rstrip()
        carinfo.append(line.split(','))
    carlist.close()
    print()
    search_info = input("Enter Rent Start Date (DD/MM/YY): ")
    print("\nCar Detail: \n")
    print(car_column)
    for i in range(len(carinfo)):
        if carinfo[i][10] == search_info:
            print(carinfo[i])
            
    returnCssIpage = input("Press enter to return to CSSI menu: ")
    return cssI_page(user, alluser)

def check_car_availability(user, alluser):
    num_passengers = int(input("Enter the number of passengers: "))
    available_cars = []

    for car in car_data:
        if car["seatcapacity"] >= num_passengers and car["availability"] == "AVAILABLE":
            available_cars.append(car)

    if available_cars:
        print(f"Available Cars for {num_passengers} passengers:")
        for car in available_cars:
            print(f"Car ID: {car['carid']}, Car Plate: {car['carplate']}, Brand: {car['brand']}, Model: {car['model']}")
    else:
        print(f"There are no cars available for {num_passengers} passengers.")

    returnCssIpage = input("Press enter to return to CSSI menu: ")
    return cssI_page(user, alluser)

def is_customer_registered(customer_id):
    with open("cusinfo.txt", "r") as file:
        for line in file:
            if line.strip():
                customer_info = line.strip().split(',')
                if customer_info[0] == customer_id:
                    return True
    return False

def record_rental_details(user, alluser):
    car_plate = input("Please enter the Car Plate: ")
    car_index = None
    for i, car in enumerate(car_data):
        if car["carplate"] == car_plate:
            car_index = i
            break

    if car_index is not None:
        car = car_data[car_index]
        if car["availability"] in ["RESERVED", "UNDERSERVICE", "DISPOSED"]:
            print("Car is not available for booking.")
            input("Press Enter to return to the CSSI menu...")
            return cssI_page(user, alluser)

        customer_ID = input("Please enter the Customer ID: ")
        if not is_customer_registered(customer_ID):
            print("Customer is not registered. Please register the customer before renting a car.")
            input("Press Enter to return to the CSSI menu...")
            return cssI_page(user, alluser)

        rental_date = input("Please enter the Car Rental Date (DD-MM-YYYY): ")
        return_date = input("Please enter the Car Return Date (DD-MM-YYYY): ")

        car["availability"] = "RESERVED"

        car["RentStartDate"] = rental_date
        car["RentReturnDate"] = return_date

        rental_days = calculate_rental_days(rental_date, return_date)
        rent_per_day = car["Rentperday"]
        total_rental = rental_days * rent_per_day

        rental_info = {
            "Car Plate": car_plate,
            "Customer ID": customer_ID,
            "Rental Date": rental_date,
            "Return Date": return_date,
            "Rental Days": rental_days,
            "Total Rental": total_rental
        }
        print("Rental details recorded correctly.")
        print("Rental Information:", rental_info)

        generate_bill(rental_info)
        payment_amount = accept_payment(total_rental)
        generate_receipt(rental_info, payment_amount, user, alluser)
    else:
        print("Car not found in the system. Please register the car before renting.")

    input("Press enter again to return to the CSSI menu...")
    return cssI_page(user, alluser)

def calculate_rental_days(start_date, end_date):
    try:
        start_day, start_month, start_year = map(int, start_date.split('-'))
        end_day, end_month, end_year = map(int, end_date.split('-'))
        start = datetime.datetime(start_year, start_month, start_day)
        end = datetime.datetime(end_year, end_month, end_day)
        return (end - start).days + 1
    except ValueError:
        print("Invalid date format. Please use the format DD-MM-YYYY.")

def generate_bill(rental_info):
    print("Generating bill...")
    print("Bill Information:")
    for key, value in rental_info.items():
        print(f"{key}: {value}")

def accept_payment(total_amount):
    payment = input("Please enter the payment amount: ")
    try:
        payment_amount = float(payment)
        if payment_amount >= total_amount:
            change = payment_amount - total_amount
            print(f"Payment accepted. Change: {change}")
            return payment_amount  
        else:
            print("Insufficient payment. Please enter the full amount.")
            return accept_payment(total_amount) 
    except ValueError:
        print("Invalid payment amount. Please enter a valid number.")
        return accept_payment(total_amount)  

def generate_receipt(rental_info, payment_amount, user, alluser):
    print("\n======================== RECEIPT ========================")
    print("Rental Information:")
    print(f"Car Plate: {rental_info['Car Plate']}")
    print(f"Customer ID: {rental_info['Customer ID']}")
    print(f"Rental Date: {rental_info['Rental Date']}")
    print(f"Return Date: {rental_info['Return Date']}")
    print(f"Rental Days: {rental_info['Rental Days']}")
    print(f"Total Rental Amount: RM{rental_info['Total Rental']}")

    if payment_amount > rental_info['Total Rental']:
        change = payment_amount - rental_info['Total Rental']
        print(f"Change: RM{change}")

    print("========================================================")
    print("Thank you for choosing our car rental service. Enjoy your ride!")
    print("========================================================")
    returnCssIpage = input("Press enter to return to CSSI menu: ")
    return returnCssIpage

while True:
    main_page()
