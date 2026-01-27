import oop.advanced.Server;

public class App {
    public static void main(String[] args) throws Exception {
        WebServer htmlServer = new WebServer();

        htmlServer.bootUp();
    }

    
}

class WebServer extends Server{
};
