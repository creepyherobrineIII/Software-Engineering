package oop.advanced;

public abstract class Server implements Computer{
    String mainProcessor;
    int numCores;
    double processingPower;
    String[] components;

    //Getters & Setters
    @Override
    public String getProcessor() {
        return mainProcessor;
    }

    @Override
    public void setProcessor(String processor) {
        this.mainProcessor = processor;
    }

    @Override
    public int getNumCores() {
        return numCores;
    }

    @Override
    public void setNumCores(int numCores) {
        this.numCores = numCores;
    }

    @Override
    public double getProcessingPower() {
        return processingPower;
    }

    @Override
    public void setProcessingPower(double processingPower) {
        this.processingPower = processingPower;
    }

    @Override
    public String[] getComponents() {
        return components;
    }

    @Override
    public void setComponents(String[] components) {
        this.components = components;
    }

    @Override
    //Methods
    public void bootUp(){
        System.out.println("System has booted up. Device is now on");
    }
}
