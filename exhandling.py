
'''def f(a,b):
    try:
        x=a//b
        print(a)
    except:
        print("not devisble by 0")
f(1,'u')'''
class negativeex(Exception):
    def __str__(self):
        return "withdrawl amount greater than avilable balance"
class grater(Exception):
    def __str__(self):
        return "ddepoit amount can not be greater than 1000"

class bank:
    def __init__(self,av_bal):
        self.av_bal=av_bal
    def withdrawl(self,amount):
        try:
            if amount > self.av_bal:
                raise negativeex
            else:
                print("withdrawl suscssed")
        except negativeex as ex:
            print(ex)

    def deposit(self,amount):
        try:
            if amount > 1000:
                raise grater
            else:
                self.av_bal+=amount
                print("amount sucsesfully deposited")
        except grater as ex:
            print(ex)

    def balance(self):
        print("av_bal",self.av_bal)

o=bank(200)
o.withdrawl(300)