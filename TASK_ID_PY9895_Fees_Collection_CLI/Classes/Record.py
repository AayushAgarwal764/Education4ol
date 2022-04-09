import csv

class Record:

    def addNewUser(self, newUserObj, csvFileName):
        dataEntryErrorFlag = 0
        row = []
        
        try:

            row.append(newUserObj.getUsername())
            row.append(newUserObj.getEmailid())
            row.append(newUserObj.getPassword())
            row.append(newUserObj.getTotalAmount())
            row.append(newUserObj.getBalanceAmount())

            filename = csvFileName
            with open(filename, 'a', newline = "") as mainFile:
                mainWriter = csv.writer(mainFile)
                mainWriter.writerow(row)

        except:

            dataEntryErrorFlag = 1

        if(dataEntryErrorFlag == 1):
            print("Due to some error, new user could not be added\nPress any key to continue\n")
            print(row)
            input()

        else:
            print("New User successfully added!\nPress any key to continue\n")
            input()
