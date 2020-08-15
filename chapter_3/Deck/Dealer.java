package chapter_3.Deck;

public class Dealer {
    private Deck deck;

    public Dealer(Deck d) {
        deck = d;
    }

    public void shuffle() {
        int num_cards = deck.size();

        for (int i = 0; i < num_cards; i++) {
            int index = (int)(Math.random() * num_cards);
            Card card_i = (Card)deck.get(i);
            Card card_index =  (Card)deck.get(index);
            deck.replace(i, card_index);
            deck.replace(index, card_i);
        }
    }

    public Card dealCard() {
        if (deck.size() > 0) {
            return deck.removeFromFront();
        }

        return null;
    }
}