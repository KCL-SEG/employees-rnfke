"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractType,pay,comissionType=""):
        self.totalpay = 0
        self.name = name
        self.contractType = contractType
        self.comissionType = comissionType
        self.hours = 0
        self.pay = pay
        self.contNum = 0
        self.contPay = 0
        self.bonus = 0


    def get_pay(self):
        if self.contractType == "monthly salary":
            totalpay = self.pay
        if self.contractType == "contract":
            totalpay = self.pay*self.hours
        if self.comissionType=="fixed":
            totalpay = totalpay + (self.contNum*self.contPay)
        if self.comissionType=="bonus":
            totalpay = totalpay + self.bonus
        self.totalpay = totalpay
        return totalpay

    def __str__(self):
        phrase = f"{self.name} works on a {self.contractType} of "
        if self.contractType == "monthly salary":
            phrase = phrase + f"{self.pay}"
        if self.contractType == "contract":
            phrase = phrase + f"{self.hours} hours at {self.pay}/hour"
        if self.comissionType=="fixed":
            phrase = phrase + f" and receives a commission for {self.contNum} contract(s) at {self.contPay}/contract"
        if self.comissionType=="bonus":
            phrase = phrase + f" and receives a bonus commission of {self.bonus}"

        phrase = phrase + f".  Their total pay is {self.get_pay()}."
        return phrase


# Billie works on a monthly  salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',"monthly salary",4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',"contract",25)
charlie.hours = 100
# Renee works on a monthly  salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',"monthly salary",3000,"fixed")
renee.contNum = 4
renee.contPay = 200
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',"contract",25,"fixed")
jan.hours = 150
jan.contNum = 3
jan.contPay = 220
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',"monthly salary",2000,"bonus")
robbie.bonus = 1500
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',"contract",30,"bonus")
ariel.hours = 120
ariel.bonus = 600
print (str(jan))
