class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        Car car = new Car();
        car.driver = "James Bond";
        car.license = "KILL007";
        car.passenger = 1;
        //System.out.println("Car License " + car.license);
        car.printDataCar();


        Car car2 = new Car();
        car2.driver = "Batman";
        car2.license = "BAT001";
        car2.passenger = 1;
        //System.out.println("Car License " + car2.license);
        car2.printDataCar();
    }
}