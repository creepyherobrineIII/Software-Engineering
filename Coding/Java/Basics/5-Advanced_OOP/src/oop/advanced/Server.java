package oop.advanced;

public abstract class Server implements Computer{
    String mainProcessor;
    int numCores;
    double processingPower;
    String[] components;

    //Getters & Setters
    public String getProcessor() {
        return mainProcessor;
    }

    public void setProcessor(String processor) {
        this.mainProcessor = processor;
    }

    public int getNumCores() {
        return numCores;
    }

    public void setNumCores(int numCores) {
        this.numCores = numCores;
    }

    public double getProcessingPower() {
        return processingPower;
    }

    public void setProcessingPower(double processingPower) {
        this.processingPower = processingPower;
    }

    public String[] getComponents() {
        return components;
    }

    public void setComponents(String[] components) {
        this.components = components;
    }

    //Methods
    public void bootUp(){
        System.out.println("System has booted up. Device is now on");
    }
}
