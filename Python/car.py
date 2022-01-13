class Car:
    id          = int
    license     = str
    driver      = str
    passenger   = int

    def __init__(self,license, driver):  # metodo constructor declarado
        self.license  = license
        self.driver   = driver