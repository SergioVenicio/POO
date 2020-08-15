package chapter_3.Deck;

public class Card {
    private int rank;
    private int suit;
    private boolean face_up;

    public static final int DIAMONDS = 4;
    public static final int HEARTS = 3;
    public static final int SPADES = 6;
    public static final int CLUBS = 5;


    public static final int TWO = 2;
    public static final int THREE = 3;
    public static final int FOUR = 4;
    public static final int FIVE = 5;
    public static final int SIX = 6;
    public static final int SEVEN = 7;
    public static final int EIGHT = 8;
    public static final int NINE = 9;
    public static final int TEN = 10;
    public static final int JACK = 74;
    public static final int QUEEN = 81;
    public static final int KING = 75;
    public static final int ACE = 65;

    public Card(int suit, int rank) {
        this.suit = suit;
        this.rank = rank;
    }

    public int getSuit() {
        return suit;
    }

    public int getRank() {
        return rank;
    }

    public void faceUp() {
        face_up = true;
    }

    public void faceDown() {
        face_up = false;
    }

    public boolean isFaceUp() {
        return face_up;
    }

    public String display() {
        String display;

        if (rank > 10) {
            display = String.valueOf(this.rankToChar());
        } else {
            display = String.valueOf(rank);
        }

        return display + this.suitToChar();
    }

    private char rankToChar() {
        return (char)rank;
    }

    private char suitToChar() {
        return (char)suit;
    }
}