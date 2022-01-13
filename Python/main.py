from car import Car
from account import Account

if __name__=="__main__":
    print('Hola Mundo')

    car = Car("BAT001", Account("Batman","batiId"))
    print(vars(car))
    print(vars(car.driver))

    # car = Car()     # método constructor
    # car.license     = 'KILL007'
    # car.driver      = 'James Bond'
    # car.passenger   = 1
    # print(vars(car))

    # car2 = Car()
    # car2.license    = 'BAT001'
    # car2.driver     = 'Batman'
    # car2.passenger  = 1
    # print(vars(car2))