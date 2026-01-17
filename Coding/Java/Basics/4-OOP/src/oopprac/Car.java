package oopprac;

public class Car {
    
    //Attributes
    private String[] engine;
    private double horsepower;
    private double topSpeed;
    private String model;
    private String brand;
    private String drivetrain; //Change to enum: RWD, FWD, AWD, 4X4
    private char gearboxType;
    private boolean cruiseControl;

    //Constructor
    public Car(String Model, String Brand){
        this.model = Model;
        this.brand = Brand;
    }


    //Getters & Setters
     public String[] getEngine() {
        return engine;
    }

    public void setEngine(String[] engine) {
        this.engine = engine;
    }

    public double getHorsepower() {
        return horsepower;
    }

    public void setHorsepower(double horsepower) {
        this.horsepower = horsepower;
    }

    public double getTopSpeed() {
        return topSpeed;
    }

    public void setTopSpeed(double topSpeed) {
        this.topSpeed = topSpeed;
    }

    public String getDrivetrain() {
        return drivetrain;
    }

    public void setDrivetrain(String drivetrain) {
        this.drivetrain = drivetrain;
    }

    public char getGearboxType() {
        return gearboxType;
    }

    public void setGearboxType(char gearboxType) {
        this.gearboxType = gearboxType;
    }

    public boolean getCruiseControl() {
        return cruiseControl;
    }

    public void setCruiseControl(boolean cruiseControl) {
        this.cruiseControl = cruiseControl;
    }
    

    //Methods
   public void printCarDetails(){
    System.out.println("Car: " + this.brand + " " + this.model);
    System.out.println("Drivetrain Type: " + this.drivetrain);
   }

    

}
