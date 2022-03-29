import random


class KickNumber:
    def __init__(self):
        self.RandomValue = 0
        self.Value = 1
        self.MaxValue = 100
        self.again = True

    def Iniciar(self):
        self.GenerateRandomNumber()
        self.AskNewValue()
        while self.again == True:
           if int(self.value_kick) > self.RandomValue:
                print('Kick a Number!! ')
                self.AskNewValue()

            elif int(self.value_kick) < self.RandomValue:
                print('Kick a new Number')
                self.AskNewValue()
            self.again = False
            print('OK!')

    def AskNewValue(self):
        self.value_kick = input('Kick a Number: ')

    def GenerateRandomNumber(self):
        self.RandomValue = random.randint(self.Value, self.MaxValue)



