import smtplib

currentUsername = "DemoUsername"
transactionAmount = 10000
ourGmailId = 'senderEmailId@example.com'
ourGmailPassword = 'senderPassword'

sentFrom = ourGmailId

to = 'receiveremailId@example.com'

subject = 'Successful Payment'
body = 'Dear {},\n\nYou have successfully completed the Transaction of Rs.{}.\n\nThis is an auto-generated email to confirm your Transaction.\n\nThank You.'.format(currentUsername, transactionAmount)

email_text = """\
From: {}
To: {}
Subject: {}

{}
""".format(sentFrom, to, subject, body)

try:
    
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(ourGmailId, ourGmailPassword)
    smtp_server.sendmail(sentFrom, to, email_text)
    smtp_server.close()
    
    print ("Email sent successfully!")
except Exception as ex:
    
    print ("Something went wrong….",ex)
