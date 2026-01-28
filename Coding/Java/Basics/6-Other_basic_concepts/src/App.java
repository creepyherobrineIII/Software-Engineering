import java.time.*; //DateTime
import java.time.format.DateTimeFormatter; // Datetime formatter 
import java.util.Scanner; //For user input

public class App {
    public static void main(String[] args) throws Exception {
        Scanner userIn = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = userIn.nextLine();

        //Date & Time
        LocalDateTime objDateTime = LocalDateTime.now();
        DateTimeFormatter objFormatter = DateTimeFormatter.ofPattern("E, MMM dd yyyy HH:mm:ss");

    
        //Output
        System.out.println("Hello " + name);
        System.out.println("It is currently: " + objDateTime.format(objFormatter));
    }

    
}
