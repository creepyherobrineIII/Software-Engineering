import java.io.*;
import java.util.*;

public class App {
    public static void main(String[] args) throws Exception {
        File myFile = new File("Test.txt");
        
        //Add "true" to constructor to append to file, not overwrite by default
        try (FileWriter myFileWriter = new FileWriter("Test.txt", true)) {
            //Create File
             
            if (myFile.createNewFile()){
                System.out.println("File Created: " + myFile.getName());
            }else{
                System.out.println("File already exists");
            }
                
            //Write to file
            myFileWriter.write("Hola senor. Soy Hans");
            System.out.println("Written new line in file");

            //Append text
            myFileWriter.write("\nDonda el bibliotecha?");
            System.out.println("New line added in file");
            
        } catch (IOException e) {
            System.out.println("An error has happened");
            e.printStackTrace();
        } 

        //Read file
        try(Scanner fileReader = new Scanner(myFile)){
            System.out.println("===========================");
            while (fileReader.hasNextLine()){
                String fileLine = fileReader.nextLine();
                System.out.println(fileLine);
            }
            System.out.println("===========================");
        } catch (FileNotFoundException e){
            System.out.println("An error has happened");
            e.printStackTrace();
        }
        /*
        //Delete file
        try {
           if(myFile.delete()){
            System.out.println("File has been deleted: " + myFile.getName());
           }else{
            System.out.println("Could not delete file");
           }
        } catch (Exception e) {
            System.out.println("An error has happened");
            e.printStackTrace();
        } */
    }
}
