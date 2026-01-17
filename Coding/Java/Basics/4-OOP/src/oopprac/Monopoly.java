package oopprac;

import java.util.*;

class BoardGame {
    String gameName;
    double cost;
    String boardShape;
    String[] pieceTypes;
    String genre;
    int rating;
    int numOfPlayers;
    String edition;

    BoardGame(String gameName, String genre, double cost){
        this.gameName = gameName;
        this.genre = genre;
        this.cost = cost;

        System.out.println(gameName + " object has been created");
    }
    
    
}

public class Monopoly extends BoardGame{
    String[] properties;
    HashMap<String, String[]> playerProps; //Should probably be a class
    HashMap<String, Integer> playerAccounts;
    int dieRoll;
    int bankMoney;

    public Monopoly(){
        super("Monopoly","Strategy, Family/Party", 43.19);
    }

    /*Imagine getters & setters here ;) */
}

/* public class DungeonsNDragons extends BoardGame{
    HashMap<String, String[]> characters; //Should probably be a class
    String[] locations;
    int numOfCharacters;
    boolean isThereFinalBoss;
    
    public DungeonsNDragons(){
        super("Dungeons & Dragons", "Fantasy, Role-play, Tabletop", 29.99);
    }

    /*Imagine getters & setters here ;) //
}

public class Ludo extends BoardGame{
    //Need to find ways to: 1 - rename them accordingly & 2 - Better structure them

    HashMap<String, Integer> piecesOnBoard;
    HashMap<String, Integer> piecesAtBase; 
    HashMap<String, Integer> piecesComplete;
    int dieRoll;

    public Ludo(){
        super("Ludo", "Dice, Race", 25.99);
    }

    /*Imagine getters & setters here ;) 

} */
