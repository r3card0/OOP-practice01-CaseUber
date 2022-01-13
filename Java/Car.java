public class Car {
    Integer  id;
    String license; // placa del carro
    Account driver; // herencia de la clase Account
    Integer passenger;

    // método constructor
    public Car(String license, Account driver){
        this.license    = license;
        this.driver     = driver;

    }

    void printDataCar(){
        System.out.println("License: " + license + " Driver: " + driver.name);
    }
}
