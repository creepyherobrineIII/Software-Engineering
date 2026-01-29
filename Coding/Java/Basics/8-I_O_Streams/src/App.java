import java.io.*;

public class App {
    public static void main(String[] args) throws Exception {
      
       //fileInputOps();
       //fileOutputOps();
       //bufferedReadOps();
       bufferedWriteOps(); 
    }

    //FileInput Streams
    public static void fileInputOps(){
        //Reading from file (Text)
        try(FileInputStream input = new FileInputStream("src/lorem.txt")){
            int i;

            while((i = input.read()) != -1){
                System.out.print((char) i);
            }
        } catch (IOException e) {
            System.out.println("Error reading file");
            e.printStackTrace();
        }

        //Copying a binary file
        try(FileInputStream input = new FileInputStream("src/dr_tony.jpg");
            FileOutputStream output = new FileOutputStream("src/tony_copy.jpg")){

            int i;
            
            //No need to convert to char. Not a text file
            while((i = input.read()) != -1){
                output.write(i);
            }

            System.out.println("File copied Successfully");
        } catch (IOException e) {
            System.out.println("Error reading file");
            e.printStackTrace();
        }

    }

    //FileOutput Streams
    public static void fileOutputOps(){
        //Writing to a file (Text)
        String loremIpsum = "Pellentesque non sodales erat, non tincidunt mi. Etiam venenatis mauris.";
        try(FileOutputStream output = new FileOutputStream("src/ipsum.txt")){
            output.write(loremIpsum.getBytes()); //Converting string to bytes
            System.out.println("Successfully writen to file");

        } catch (IOException e){
            System.out.println("Error writing to file");
            e.printStackTrace();
        }

        //Copying a pdf
        try(FileInputStream input = new FileInputStream("src/Lorem.pdf");
            FileOutputStream output = new FileOutputStream("src/Ipsum.pdf")){

            int i;

            while((i = input.read()) != -1){
                output.write(i);
            }

            System.out.println("Successfully copied pdf file");
        } catch (IOException e){
            System.out.println("Error writing to file");
            e.printStackTrace();
        }
    }

    public static void bufferedReadOps(){
        //Reading a text file
        try(BufferedReader bInput = new BufferedReader(new FileReader("src/lorem.txt"))){
            String line;

            while ((line = bInput.readLine()) != null){
                System.out.println(line);
            }
        } catch (IOException e){
            System.out.println("Error reading file");
            e.printStackTrace();
        }
    }

    public static void bufferedWriteOps(){
        //Writing to a file

        try(BufferedWriter bWriter = new BufferedWriter(new FileWriter("src/ipsum.txt"))){
            String line;

            bWriter.write("Aenean efficitur ligula nec ullamcorper volutpat. Vestibulum fermentum turpis nulla, nec imperdiet diam malesuada ultrices.");
            bWriter.newLine();
            bWriter.write("Morbi placerat diam id orci tincidunt, sit amet porta leo viverra. Vivamus ornare congue enim.");
            System.out.println("Successfully written to file");
        } catch (IOException e){
            System.out.println("Error writing to file");
            e.printStackTrace();
        }

    }
}
