import java.util.Scanner;

//Checking average of numbers given by user
public class App {
    public static void main(String[] args) throws Exception {
        //addBinaryNum();

        //BubSort();

        //selectSort();

        //insertSort();

        //reverseString();

        //evenOrOdd();
        checkPalindrome();
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

    //Bubble Sort
    static void BubSort(){
        int[] nums = {7, 3, 9, 12, 11, 5, 3, 8, 66};

        for (int i = 0; i < nums.length; i++){
            for (int j = 0; j < nums.length - 1; j++){
                int compVal = nums[j+1];

                if (compVal < nums[j]){
                    nums[j+1] = nums[j];
                    nums[j] = compVal;  
                }
            }
        }

        for (int num: nums){
            System.out.print(num + ", ");
        }
        
    }

    //Selection Sort (lowest value)
    static void selectSort(){
        int[] nums = {7, 3, 9, 12, 11, 5, 3, 8, 66};

        for (int i = 0; i < nums.length; i++){

            int minIndex = i;

            for (int j = i + 1; j < nums.length ; j++){
                
                if (nums[j] < nums[minIndex]){
                    minIndex = j;
                }
            }

            int temp = nums[i];
            nums[i] = nums[minIndex];
            nums[minIndex] = temp;
        }

        for (int num: nums){
            System.out.print(num + ", ");
        }

    }

    //Insertion Sort
    static void insertSort(){
        int[] nums = {64, 34, 25, 12, 22, 11, 90, 5};

        for (int i = 1; i < nums.length; i++){
            int insertIndex = i;
            int cVal = nums[i];

            for (int j = i - 1; j >= 0 ; j--){
                if (nums[j] > cVal){
                    nums[j+1] = nums[j];
                    insertIndex = j;
                }
            }

            nums[insertIndex] = cVal;
        }

        for (int num: nums){
            System.out.print(num + ", ");
        }
    }


    //Reverse a string
    static void reverseString(){
        String name = "Alejandro";
        StringBuilder reverse = new StringBuilder();

        for (int i = name.length()-1; i >=0; i--){
            char temp = name.charAt(i);
            reverse.append(temp);
        }

        System.out.println(reverse);

    }

    //Even or odd
    static void evenOrOdd(){
        int num = 5;

        if (num % 2 == 0){
            System.out.println("Even");
        }
        else{
            System.out.println("Odd");
        }
    }

    //Palindrome Check
    static void checkPalindrome(){
        StringBuilder check = new StringBuilder("racecar");
        boolean pCheck = true;

        for (int i = check.length() -1; i > 0; i--){
            int index = (check.length()-1) - i;
            
            if (check.charAt(index) == check.charAt(i)){
                System.out.println(check.charAt(i) + ": Match");

                continue;
            }
            else{
                System.out.println(check.charAt(i) + ": No Match");
                pCheck = false;
            }

           
        }

        if (pCheck){
            System.out.println("String is a palindrome");
        }else{
            System.out.println("String is NOT a palindrome");
        }
    }

    static void debugTest(String[] strArr){
         
    
         // code goes here
    StringBuilder arrElement = new StringBuilder();
    StringBuilder arrCompElement = new StringBuilder();
    StringBuilder strOut = new StringBuilder();
    }


    //Adding binary numbers
    static void addBinaryNum(){
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


