import csv

class Emailid:

    email_id_present = []
    
    def generateEmailidListFromFile(self, csvFileName):
        csvfile = open(csvFileName, "r")
        file_content = csv.reader(csvfile)

        fields = next(file_content)
    
        for row in file_content:
            if(row != []):
                self.email_id_present.append(row[1])

        csvfile.close()

