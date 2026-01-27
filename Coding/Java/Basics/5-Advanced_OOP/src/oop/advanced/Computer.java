package oop.advanced;

interface Computer {
    
    //Getters & Setters
    public String getProcessor();

    public void setProcessor(String processor);

    public int getNumCores();

    public void setNumCores(int numCores);

    public double getProcessingPower();

    public void setProcessingPower(double processingPower) ;

    public String[] getComponents();

    public void setComponents(String[] components);

    //Methods
    public void bootUp();
}
