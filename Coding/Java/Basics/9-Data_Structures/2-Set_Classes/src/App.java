import java.util.*;

public class App {
    public static void main(String[] args) throws Exception {
        //hashSetOps();
        //treeSetOps();
        linkedHashSetOps();
    }
//Sets - For non-duplicate elements
    //Fast and unordered - HashSet
    public static void hashSetOps(){
        HashSet<String> cars = new HashSet<>();
        
    //Methods
        //Add
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford"); 
        cars.add("BMW"); //Duplicate for example (elements only appear once)
        cars.add("Mazda");
        cars.add("Opel");

        System.out.println(cars);

        //Remove
        System.out.println("====================");
        System.out.println("Removing car from set....");
        cars.remove("Opel");
        System.out.println("====================");

        System.out.println(cars);

        //Contains
        System.out.println("====================");
        System.out.println("Checking for \"Opel\" in set....");
        boolean hasCar = cars.contains("Opel");
        System.out.println("Contains car \"Opel\": " + hasCar);


        //Size
        System.out.println("====================");
        int setSize = cars.size();
        System.out.println("Size of set: " + setSize);

        //Clear
        //cars.clear();
        
    }


    //Sorted set (automatic sorting) - TreeSet (slower than HashSet)
    public static void treeSetOps(){
        TreeSet<String> cars = new TreeSet<>();

        //Methods
        //Add
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford"); 
        cars.add("BMW"); //Duplicate for example (elements only appear once)
        cars.add("Mazda");
        cars.add("Opel");

        System.out.println(cars);

        //Remove
        System.out.println("====================");
        System.out.println("Removing car from set....");
        cars.remove("Opel");
        System.out.println("====================");

        System.out.println(cars);

        //Contains
        System.out.println("====================");
        System.out.println("Checking for \"Opel\" in set....");
        boolean hasCar = cars.contains("Opel");
        System.out.println("Contains car \"Opel\": " + hasCar);


        //Size
        System.out.println("====================");
        int setSize = cars.size();
        System.out.println("Size of set: " + setSize);

        //Clear
        //cars.clear();
    }

//LinkedHashSet = Unique elements, insertion order maintained (slightly slower than HashSet)
    public static void linkedHashSetOps(){
        Set<String> cars = new LinkedHashSet<>(); //Used to change types later

        //Methods
        //Add
       
        cars.add("Opel");
        cars.add("Ford"); 
        cars.add("BMW");
        cars.add("BMW"); //Duplicate for example (elements only appear once)
        cars.add("Mazda");
        cars.add("Volvo");
        

        System.out.println(cars);

        //Remove
        System.out.println("====================");
        System.out.println("Removing car from set....");
        cars.remove("Opel");
        System.out.println("====================");

        System.out.println(cars);

        //Contains
        System.out.println("====================");
        System.out.println("Checking for \"Opel\" in set....");
        boolean hasCar = cars.contains("Opel");
        System.out.println("Contains car \"Opel\": " + hasCar);


        //Size
        System.out.println("====================");
        int setSize = cars.size();
        System.out.println("Size of set: " + setSize);

        //Clear
        //cars.clear();
    }
}
