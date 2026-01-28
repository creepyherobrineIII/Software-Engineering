import oop.advanced.Server;

public class App {
    public static void main(String[] args) throws Exception {
        WebServer htmlServer = new WebServer();

        htmlServer.bootUp();

        GameServer amoungUs = new GameServer(){
            public void bootUp(){
                System.out.println("Game server is now online");
            }
        };

        amoungUs.bootUp();
        Difficulty gameDifficulty = Difficulty.Normal;
    }

    //Enum (Can be used like classes - except that members are public, static and final)
        enum Difficulty{
            Easy,
            Normal,
            Hard,
            Very_Hard,
            Extreme
        };
    
}

class WebServer extends Server{
};

//Anonymous Class
class GameServer extends Server{

    //Inner Class
    class Game{
        String name;
        String serialNum;
    }
;}

