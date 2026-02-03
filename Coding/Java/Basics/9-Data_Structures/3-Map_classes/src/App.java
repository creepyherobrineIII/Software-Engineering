import java.util.*;

public class App {
    public static void main(String[] args) throws Exception {
        //hashMapOps();
        //treeMapOps();
        linkedHashMapOps();
    }

//HashMap - Fast & Unsorted (Fastest)
    public static void hashMapOps(){
        HashMap<String, String> capitalCities = new HashMap<>();

        //Mathods
        //Put
        capitalCities.put("England", "London");
        capitalCities.put("India", "New Delhi");
        capitalCities.put("Austria", "Wien");
        capitalCities.put("Norway", "Oslo");
        capitalCities.put("Norway", "Oslo"); //Duplicate
        capitalCities.put("USA", "Washington DC");
        capitalCities.put("Turkey", "Ankara");

        System.out.println(capitalCities);

        //Get
        System.out.println("==========================");
        System.out.println(capitalCities.get("USA"));

        //Remove
        System.out.println("==========================");
        System.out.println("Removing an element....");
        capitalCities.remove("Turkey");
        System.out.println(capitalCities);

        //Size
        System.out.println("==========================");
        System.out.println("Map size: " + capitalCities.size());

        //Loop through (keys)
        System.out.println("==========================");
        System.out.println("Map keys");
        for (String country: capitalCities.keySet()){
            System.out.print(country + ", ");
        }
        System.out.println(" ");

        //Loop through (values)
        System.out.println("==========================");
        System.out.println("Map values");
        for (String city: capitalCities.values()){
            System.out.print(city + ", ");
        }
    }

//TreeMap - Sorted in natural order, by key (keeps automatic sort)
    public static void treeMapOps(){
        TreeMap<String, String> capitalCities = new TreeMap<>();

        //Mathods
        //Put
        capitalCities.put("England", "London");
        capitalCities.put("India", "New Delhi");
        capitalCities.put("Austria", "Wien");
        capitalCities.put("Norway", "Oslo");
        capitalCities.put("Norway", "Oslo"); //Duplicate
        capitalCities.put("USA", "Washington DC");
        capitalCities.put("Turkey", "Ankara");

        System.out.println(capitalCities);

        //Get
        System.out.println("==========================");
        System.out.println(capitalCities.get("India"));

        //Remove
        System.out.println("==========================");
        System.out.println("Removing an element....");
        capitalCities.remove("England");
        System.out.println(capitalCities);

        //Size
        System.out.println("==========================");
        System.out.println("Map size: " + capitalCities.size());

        //Loop through (keys)
        System.out.println("==========================");
        System.out.println("Map keys");
        for (String country: capitalCities.keySet()){
            System.out.print(country + ", ");
        }
        System.out.println(" ");

        //Loop through (values)
        System.out.println("==========================");
        System.out.println("Map values");
        for (String city: capitalCities.values()){
            System.out.print(city + ", ");
        }

    }

//LinkedHashMap - Maintains insertion order
    public static void linkedHashMapOps(){
        LinkedHashMap<String, String> capitalCities = new LinkedHashMap<>();

        //Mathods
        //Put
        capitalCities.put("England", "London");
        capitalCities.put("India", "New Delhi");
        capitalCities.put("Austria", "Wien");
        capitalCities.put("Norway", "Oslo");
        capitalCities.put("Norway", "Oslo"); //Duplicate
        capitalCities.put("USA", "Washington DC");
        capitalCities.put("Turkey", "Ankara");

        System.out.println(capitalCities);

        //Get
        System.out.println("==========================");
        System.out.println(capitalCities.get("USA"));

        //Remove
        System.out.println("==========================");
        System.out.println("Removing an element....");
        capitalCities.remove("Turkey");
        System.out.println(capitalCities);

        //Size
        System.out.println("==========================");
        System.out.println("Map size: " + capitalCities.size());

        //Loop through (keys)
        System.out.println("==========================");
        System.out.println("Map keys");
        for (String country: capitalCities.keySet()){
            System.out.print(country + ", ");
        }
        System.out.println(" ");

        //Loop through (values)
        System.out.println("==========================");
        System.out.println("Map values");
        for (String city: capitalCities.values()){
            System.out.print(city + ", ");
        }

    }
}
