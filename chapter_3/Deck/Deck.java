package chapter_3.Deck;

import java.utl.LinkedList;

public class Deck {
    private java.util.LinkedList deck;

    public Deck() {
        buildCards();
    }

    public Card get(int index) {
        if (index < deck.size()) {
            return (Card)deck.get(index);
        }

        return null;
    }

    public void replace(int index, Card card) {
        deck.set(index, card);
    }

    public int size() {
        return deck.size();
    }

    public Card removeFromFront() {
        if (deck.size() > 0) {
            Card card = (Card) deck.removeFirst();
            return card;
        }

        return null;
    }

    public void returnToBack(Card card) {
        deck.add(card);
    }

    private void buildCards() {
        deck = new java.util.LinkedList();
        deck.add(new Card(Card.CLUBS, Card.TWO));
    }
}