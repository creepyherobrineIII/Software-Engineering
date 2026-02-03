import java.util.*;

public class App {
    public static void main(String[] args) throws Exception {
        //treeSetIter();
        collectionsAlgos();
    }

//Works for List and Set interfaces and classes
    public static void treeSetIter(){
        TreeSet<String> capitalCities = new TreeSet<>();

        capitalCities.add("London");
        capitalCities.add("New Dehli");
        capitalCities.add("Wien");
        capitalCities.add("Oslo");
        capitalCities.add("Oslo"); // Duplicate
        capitalCities.add("Washington DC");

        System.out.println(capitalCities);
        
        //Creating an iterator
        Iterator setIterator = capitalCities.iterator();

        //Looping through iterator
        while(setIterator.hasNext()){
            //Removing an instance
            if (setIterator.next() == "Oslo"){ //Removes any duplicates as well
                setIterator.remove();
            }
        }

        System.out.println(capitalCities);
    }

    public static void collectionsAlgos(){
        ArrayList<Integer> numbers = new ArrayList<>();

        //Adding elements to ArrayList
        numbers.add(1);
        numbers.add(34);
        numbers.add(90);
        numbers.add(12);
        numbers.add(22);
        numbers.add(22);
        numbers.add(22); //Duplicates to see frequency
        numbers.add(67); //lol

    //Alogorithms
        //Binary Search (find elements in a SORTED list)
        Collections.sort(numbers);

        System.out.println("==========================");
        System.out.println("Sorted list: " + numbers);

        int index = Collections.binarySearch(numbers, 34);
        System.out.println("The number 34 is at index: " + index);

        //Sorting (done in previous step)
        Collections.sort(numbers);

        //Sorting (Descending)
        Collections.sort(numbers, Collections.reverseOrder());
        System.out.println("==========================");
        System.out.println("Reverse sorted list: " + numbers);

        //Max (Find largest element)
        System.out.println("==========================");
        System.out.println("Biggest number in list: " + Collections.max(numbers));

        //Min (Find smallest element)
        System.out.println("==========================");
        System.out.println("Smallest number in list: " + Collections.min(numbers));

        //Shuffle (Randomly shuffles elements)
        System.out.println("==========================");
        Collections.shuffle(numbers);
        System.out.println("Shuffled list: " + numbers);

        //Frequency (Counts how many times an element appears)
        System.out.println("==========================");
        int selectedNum = 22;
        int numFrequency = Collections.frequency(numbers, selectedNum);
        System.out.println("Frequency of number " + selectedNum + " : " + numFrequency);

        //Swap (Swap two elements in a list)
        Collections.shuffle(numbers);
        System.out.println("==========================");
        System.out.println("Unchanged list: " + numbers);
        Collections.swap(numbers, 0, 5);
        System.out.println("==========================");
        System.out.println("List with swapped positions (0 and 5): " + numbers);


    }
}
