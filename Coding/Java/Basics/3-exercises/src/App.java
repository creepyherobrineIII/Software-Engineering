import java.util.Scanner;

//Checking average of numbers given by user
public class App {
    public static void main(String[] args) throws Exception {
        addBinaryNum();

        /*Scanner userIn = new Scanner(System.in);

        //Getting user input: First number
        System.out.println("Enter first number: ");
        String num1 = userIn.nextLine();
        
        //Second number
        System.out.println("Enter second number: ");
        String num2 = userIn.nextLine();

        //Third number
        System.out.println("Enter third number: ");
        String num3 = userIn.nextLine();

        //Process numbers
        int n1 = Integer.parseInt(num1);
        int n2 = Integer.parseInt(num2);
        int n3 = Integer.parseInt(num3);

        double aveOfNum = (n1 + n2 + n3) / 3;

        System.out.println("Average of the numbers: "+ aveOfNum);
        */
        
    }

    //Adding binary numbers
    public static void addBinaryNum(){
        Scanner binNum = new Scanner(System.in);

        //Geting binary values
        System.out.println("Enter binary num 1: ");
        String bin1 = binNum.nextLine();

        System.out.println("Enter binary num 2: ");
        String bin2 = binNum.nextLine();

        int b1 = Integer.parseUnsignedInt(bin1, 2);
        int b2 = Integer.parseUnsignedInt(bin2, 2);


        System.out.println("The output is: " + Integer.toBinaryString((b1+b2)));
    }
}


