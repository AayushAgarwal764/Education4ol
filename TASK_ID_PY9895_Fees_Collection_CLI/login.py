import re
import csv

from Classes import Emailid


CSV_FILE_NAME = "MasterCSVFile_created_by_program.csv"
required_row = []
paymentChoice = ""

emailidObj = Emailid.Emailid()
emailidObj.generateEmailidListFromFile(CSV_FILE_NAME)

print("Welcome to the Login Window!\n")

while True:
    errorflagemailid = 0
    temp_emailid = input("Enter Email ID :")

    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
       
    if(temp_emailid == "Q" or temp_emailid == "q"):
        print("Exiting the Program\n Press any key to exit\n")
        input()
        quit()

    if(bool(re.fullmatch(regex, temp_emailid)) == False):
        print("Plase enter Valid Email ID [(username)@(domainname).(top-leveldomain)]\n")
        errorflagemailid = 1

    else:
        temp_emailid = temp_emailid.lower() 

        if(not(temp_emailid in emailidObj.email_id_present)):
            print("Email ID is not present in the Records. Please Try Again\nEnter Q to exit the Program\n")
            errorflagemailid = 1
        
    if(errorflagemailid == 0):
        break

while True:
    errorflagPassword = 0
    temp_password = input("Enter the Password :")

    csvfile = open(CSV_FILE_NAME, "r")
    file_content = csv.reader(csvfile)

    fields = next(file_content)
    
    for row in file_content:
        if(row != []):
            if(temp_emailid in row):
                required_row = row
                

    if(temp_password == "Q" or temp_password == "q"):
        print("Exiting the Program\n Press any key to exit\n")
        input()
        quit()
    
    if(not(temp_password == required_row[2])) :
       print("Invalid Password. Please Try Again.\nEnter Q to exit the Program\n")
       errorflagPassword = 1

    
    if(errorflagPassword == 0):
        break

print("\nWelcome", required_row[0])
print("Your Details are as Follows:\n")
print("Total Amount :", required_row[3])
print("Pending Amount :", required_row[4] + "\n")


while True:
    paymentChoice = input("Do you want to make a payment? [Y/N]\nEnter your Choice :")

    if(paymentChoice == "Y" or paymentChoice == "y"):
        break
    
    elif(paymentChoice == "N" or paymentChoice == "n"):
    
        print("Press any key to continue\n")
        input()
        break
    
    else:
        print("Please Enter either Y or N\n")
