class Newuser:
    username = ""
    emailid = ""
    password = ""
    totalAmount = 0
    balanceAmount = 0

    def setUsername(self, inputUsername):
        self.username = inputUsername.lower()

    def setEmailid(self, inputEmailid):
        self.emailid = inputEmailid.lower()

    def setPassword(self, inputPassword):
        self.password = inputPassword

    def setTotalAmount(self, inputTotalAmount):
        self.totalAmount = inputTotalAmount

    def setBalanceAmount(self, inputBalanceAmount):
        self.balanceAmount = inputBalanceAmount

    def getUsername(self):
        return self.username

    def getEmailid(self):
        return self.emailid

    def getPassword(self):
        return self.password

    def getTotalAmount(self):
        return self.totalAmount

    def getBalanceAmount(self):
        return self.balanceAmount

