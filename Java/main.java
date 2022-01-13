class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        Car car = new Car("KILL007", new Account("James Bond","GUN123"));
        car.passenger = 1;
        //System.out.println("Car License " + car.license);
        car.printDataCar();


        Car car2 = new Car("BAT001", new Account("Batman", "batId"));
        car2.passenger = 1;
        //System.out.println("Car License " + car2.license);
        car2.printDataCar();
    }
}