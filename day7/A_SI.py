class bank_interest_calculator:

    __interest_rate = 8.6
    __interest_rate_seniorcitizen = 8.4

    def __init__(self,p_amount,duration,seniorCitizen):
        self.p_amount = p_amount
        self.duration = duration
        self.seniorCitizen = seniorCitizen

    def simple_interest_calculator(self):
        if self.seniorCitizen == True:
            self.__interest_rate= self.__interest_rate_seniorcitizen
            print((self.p_amount*self.__interest_rate*self.duration)/100)
        else:
            self.__interest_rate=self.__interest_rate
            print((self.p_amount * self.__interest_rate * self.duration) / 100)



if __name__ == '__main__':

    bank1 = bank_interest_calculator(30000,5,True)
    bank2 = bank_interest_calculator(50000,10,False)

    bank1.simple_interest_calculator()
    bank2.simple_interest_calculator()

