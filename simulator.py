from fileinput import close
from logging import exception
import random  # import the library random


class SimulatorData:
    def __init__(self):
        self.value = 1
        self.maxvalue = 6
        self.msg = 'Rotate Data:'

    def Init(self):
        answer = input(self.msg)
        try:  # handle the exception
            if answer == 'yes' or 'y':
                self.GenerateValueData()
            elif answer == 'not' or 'n':
                exit()
            else:
                print('Please Yes or Not!! ')
        except:
            print('Erro!')

    def GenerateValueData(self):
        print(random.randint(self.value, self.maxvalue))


simulator = SimulatorData()
simulator.Init()
