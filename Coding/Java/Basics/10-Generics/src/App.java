import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        //Creating objects of different types
        UserId<String> userName = new UserId<>();
        UserId<Character[]> entryId = new UserId<>();

        //String Username
        userName.set("creepyHeroBrine#68");
        System.out.println("Username: " + userName.get());

        //Character Id Identifier
        String strUserId = "yia7efhi73#$";
        char[] temp = strUserId.toCharArray();
        Character[] charArr = new Character[temp.length];

        for (int i = 0; i < temp.length; i++){
            charArr[i] = temp[i];
        }

        entryId.set(charArr);
        System.out.println("Entry ID: " + Arrays.toString(entryId.get()));
        
    }

    
}

class UserId<T>{ //A way to identify someone (Via username or unique characters)
    T value;

    void set(T value){
        this.value = value;
    }

    T get(){
        return this.value;
    }
}

