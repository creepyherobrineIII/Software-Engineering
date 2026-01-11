
public class App {
    public static void main(String[] args) throws Exception {
        int trhe;
        float test1;
        double test2;
        char test3;


        trhe = 35 + 67;
        test1 = 24.584565f;
        test2 = 67.25d; //Remember
        test3 = 254;
        var test4 = "TRACKING"; 


        System.out.println(trhe + " Yurr");
        System.out.println(test1);
        System.out.println(test2);
        System.out.println(test3);
        System.out.println(test4);
    }
}

/*
    Variables:
    Primitive = simple value stored dircetly in memory (stack)
    Reference = memory address (stack) that points to the heap

    Primitive   vs      Reference
    -----------------------------
    int                 string
    double              array
    char                object
    boolean
*/
