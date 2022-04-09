import re

from Classes import Newuser
from Classes import Record
from Classes import Emailid

CSV_FILE_NAME = "MasterCSVFile_created_by_program.csv"

newUserObj = Newuser.Newuser()
emailidObj = Emailid.Emailid()

emailidObj.generateEmailidListFromFile(CSV_FILE_NAME)

print("Welcome to the Create New User Account Window!\n")

while True:
    new_username = str(input("Enter your name :"))

    if(new_username.isalpha() == False):
        print("Please Enter Alphabets only\n")
    
    else:
        newUserObj.setUsername(new_username)
        break


while True:
    new_emailid = str(input("Enter your Email ID :"))

    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    
    if(bool(re.fullmatch(regex, new_emailid)) == False):
       print("Plase enter Valid Email ID [(username)@(domainname).(top-leveldomain)]\n")

    else:
        new_emailid = new_emailid.lower()
        
        if(new_emailid in emailidObj.email_id_present):
            print("This Email ID is already registered\nPlease try another Email ID\n")

        else:
            newUserObj.setEmailid(new_emailid)
            break



while True:
    new_password = str(input("Enter your Password :"))
    
    errorflagPassword = 1
    lowercaseletter = 1
    uppercaseletter = 1
    specialsymbol = 1
    numberpresent = 1
    
    if(len(new_password) >= 8 or len(new_password) <= 20):
        if not any(char.isdigit() for char in new_password):
            print('Password should have at least one numeral\n')
            errorflagPassword = 1
            numberpresent = 0
            
        if not any(char.isupper() for char in new_password):
            print('Password should have at least one uppercase letter\n')
            errorflagPassword = 1
            uppercaseletter = 0
            
        if not any(char.islower() for char in new_password):
            print('Password should have at least one lowercase letter\n')
            errorlflagPassword = 1
            lowercaseletter = 0
            
        if not any(char in "!@#$%^&*_" for char in new_password):
            print('Password should have at least one of the symbols [ !@#$%^&*_ ]\n')
            errorflagPassword = 1
            specialsymbol = 0
            
        
    else:
        if(len(new_password) < 8):
            print("Password Length must be greater than 8 charachters\n")
            errorflagPassword = 1
        elif(len(new_password) > 20):
            print("Password Length must be less than 20 characters\n")
            errorflagPassword = 1

    if(numberpresent and uppercaseletter and lowercaseletter and specialsymbol):
        errorflagPassword = 0
        
    if(errorflagPassword == 0):
        newUserObj.setPassword(new_password)
        break


while True:
    totalAmount = input("Enter the Total Amount :")
    errorflagTA = 0
    
    if(not(totalAmount.isdigit())):
        print("Please Enter Numbers only\n")
        errorflagTA = 1
    else:
        totalAmount = int(totalAmount)
        errorflagTA = 0
        
    if(errorflagTA == 0):
        newUserObj.setTotalAmount(totalAmount)
        break
    
    
while True:
    balanceAmount = input("Enter the Balance Amount :")
    errorflagBA = 0
    tempvar = str(balanceAmount)
    if(not(balanceAmount.isdigit())):
        print("Please Enter Numbers only\n")
        errorflagBA = 1

    else:
        balanceAmount = int(balanceAmount)
        if(not(balanceAmount <= totalAmount)):
            print("Balance Amount cannot be greater than Total Amount")
            errorflagBA = 1

    if((tempvar.isdigit()) and (balanceAmount <= totalAmount)):
        errorflagBA = 0
        
    if(errorflagBA == 0):
        newUserObj.setBalanceAmount(balanceAmount)
        break


recordObj = Record.Record()
recordObj.addNewUser(newUserObj, CSV_FILE_NAME)



































