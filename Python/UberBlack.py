from car import Car

class UberBlack(Car):
    typeCarAccepted = []
    seatsMaterial   = []


    def __init__(self, license, driver, typeCarAccepted, SeatsMaterial):
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial  = SeatsMaterial