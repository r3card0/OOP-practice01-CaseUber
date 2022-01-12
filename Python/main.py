from car import Car

if __name__=='__main__':
    print('Hola Mundo')
    car = Car()
    car.license     = 'KILL007'
    car.driver      = 'James Bond'
    car.passenger   = 1
    print(vars(car))

    car2 = Car()
    car2.license    = 'BAT001'
    car2.driver     = 'Batman'
    car2.passenger  = 1
    print(vars(car2))