from tkinter import *
import tkinter.ttk as tk
import random
import re
from datetime import datetime

MINIMUM_PASSWORD_LENGTH = 8
MAXIMUM_PASSWORD_LENGTH = 12

def addPasswordToFile(finalPassword):
        now = datetime.now()
        errorFlag = 0
        try:
                f = open("Passwords_From_Generator.txt", "w")
                f.write("Password created on {} is   {}".format(now, finalPassword))
                f.close()
        except:
                errorFlag = 1
        if(errorFlag == 1):
                message = "Due to some error, Password was not written in File"
        elif(errorFlag == 0):
                message = "Password succesfully written in File"

        fileLabel = tk.Label(root, text = message, font = ("Helvetica", 12))
        fileLabel.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = (W))

        
def checkPasswordStrength(password):
        flag = 1
        message = ""
        if(len(password) >= 8):
                while True:  
        
                    if not re.search("[a-z]", password, re.IGNORECASE):
                        flag = -1
                        break
                    elif not re.search("[0-9]", password):
                        flag = -1
                        break
                    elif not re.search("[_@$#%=:!^&*]", password):
                        flag = -1
                        break
                    elif re.search("\s", password):
                        flag = -1
                        break
                    else:
                        flag = 0
                        break
        else:
                message = "Password Length less than 8 characters"

        if(flag == -1):
                message = "Password Strength is Weak"
        elif(flag == 0):
                message = "Password Strength is Strong"
        passwordStrengthLabel = tk.Label(root, text = message, font=("Helvetica", 12))
        passwordStrengthLabel.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = (W))
        addPasswordToFile(password)
        
        
        
def formatInput(oldstring):
        if(len(oldstring) > 10 and len(oldstring) != 10):
                oldstring = oldstring[:10]
        elif(len(oldstring) < 10):
                for j in range(10 - len(oldstring)):
                        oldstring += '_'
        

        newstring = []

        for i in oldstring:
                if(i != " "):
                        newstring.append(i);

                else:
                        newstring.append('_');
        
        return newstring

def createPassword():

        requiredPassword = ""
        wordsFromUser = input_from_user.get()
        formattedInput = formatInput(wordsFromUser)
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
        specialCharacters = ['@', '#', '$', '%', '=', ':', '!', '^', '&', '*']

        currentPasswordLength = random.randrange(MINIMUM_PASSWORD_LENGTH, MAXIMUM_PASSWORD_LENGTH)

        mainList = []
        
        for currentChar in range(currentPasswordLength):
                mainList.append(random.choice(formattedInput))
                mainList.append(random.choice(numbers))
                mainList.append(random.choice(specialCharacters))

                requiredPassword += random.choice(mainList)
                mainList = []
                
        NewPasswordLabel = tk.Label(root, text = "Password Created: " + requiredPassword, font=("Helvetica", 12))
        NewPasswordLabel.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = (W))

        checkPasswordStrength(requiredPassword)
        
        
        
        
root = Tk()
root.geometry("500x300")
root.title("Password Generator")

input_from_user = StringVar()

label1 = tk.Label(root, text = "Enter the words for Password:", font=("Helvetica", 12))
text1 = tk.Entry(root, textvariable = input_from_user, width = 30)
button1 = tk.Button(root, text = "Generate Password", command = createPassword)

label1.grid(row = 0, column = 0, padx = 5)
text1.grid(row = 0, column = 1)
button1.grid(row = 1, column = 0, sticky = (W), padx = 5, pady = 5)
                              
root.mainloop()
