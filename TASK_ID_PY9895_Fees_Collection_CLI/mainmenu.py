import os

print("Welcome User!")

while True:

    userchoice = input("Would you like to Sign Up [1] or Login In [2]?\nPress [3] to exit\nPlease Enter your Choice :")

    if(not(userchoice.isdigit())):
        print("Please Enter either 1, 2 or 3")
    else:
        userchoice = int(userchoice)
        if(userchoice != 1 and userchoice != 2 and userchoice != 3):
            print("Please do not enter Numbers except 1, 2 or 3\n")
        else:
        
            match userchoice:
                case 1:
                    os.system("python " + r"signup.py")
                    
                case 2:
                    os.system("python " + r"login.py")
                    
                case 3:
                    print("Exiting Program...\nPress any key to exit\n")
                    input()
                    quit()
                
