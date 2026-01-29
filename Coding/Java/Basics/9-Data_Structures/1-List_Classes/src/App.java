import java.util.*;

public class App {
    public static void main(String[] args) throws Exception {
        //arrayListOps();
        linkedListOps();
    }

//ArrayList Operations
    public static void arrayListOps(){
        ArrayList<String> cars = new ArrayList<String>(); //Can be any other data stype (Wrapper Class must be used)
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");
        cars.add(0,"Mazda"); //Can insert at a specific position
        System.out.println("Unsorted");
        System.out.println(cars);

        /*
        //Access element
        System.out.println("Car 3: " + cars.get(2));

        //Change an element
        cars.set(1, "Opel");
        System.out.println("Changed element");

        System.out.println(cars);

        //Delete an element
        cars.remove(3);
        System.out.println("Deleted element");

        System.out.println(cars);
        
        //Clear ArrayList
        //cars.clear();
        */

        //ArrayList Size
        
        System.out.println("ArrayList Size: " + cars.size());

        //Looping through ArrayList
        for(String car: cars){
            System.out.println(car);
        }

        //Sorting ArrayList
        System.out.println(" ");
        System.out.println("============================");
        System.out.println("Sorting ArrayList...");
        System.out.println("============================");

        Collections.sort(cars);
        System.out.println("Sorted!");
        System.out.println(cars);

        /* Possible code
            List<String> cars = new ArrayList<>();

            Is possible because ArrayList implements the List Interface
                *Used to change types if necessary*
         */
    }

//LinkedList Operations
    public static void linkedListOps(){
        LinkedList<String> cars = new LinkedList<String>();
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");
        cars.add("Mazda");
        System.out.println(cars);

        //Same operations as ArrayList

        //Unique operations

        //Adding
        System.out.println("============================");
        System.out.println("Updating first and last elements");
        cars.addFirst("Mercedes");
        cars.addLast("Opel");
        System.out.println("Updated!");
        System.out.println(cars);
        System.out.println("============================");

        //Getting
        System.out.println("First element: " + cars.getFirst());
        System.out.println("Last element: " + cars.getLast());

        //Removing
        System.out.println("============================");
        System.out.println("Removing first and last elements");
        cars.removeFirst();
        cars.removeLast();
        System.out.println("Removed!");
        System.out.println("============================");

        System.out.println(cars);

    //Sorting (applies to ArrayList as well)
        System.out.println("============================");
        System.out.println("Sorting elements (reverse order)");
        Collections.sort(cars, Collections.reverseOrder()); //Reverses order of list

        for (String car: cars){
            System.out.print(car + ", ");
        }
        System.out.println(" ");
        System.out.println("============================");
    }
}
