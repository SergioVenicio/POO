public class Item {
    private double unit_price;
    private double discount;
    private int quantity;
    private String description;
    private String id;

    public Item(String id, String description, int quantity, double price) {
        this.id = id;
        this.description = description;
        this.unit_price = price;

        if (quantity > 0) {
            this.quantity = quantity;
        } else {
            this.quantity = 0;
        }
    }

    public double getTotal() {
        double partialDiscount = this.unit_price * this.discount;
        double total = (unit_price * quantity) - partialDiscount;
        return total;
    }

    public double getDiscount() {
        return discount;
    }

    public void setDiscount(double discount) {
        if (discount <= 1.0) {
            this.discount = discount;
        } else {
            this.discount = 0.0;
        }
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        if (quantity > 0) {
            this.quantity = quantity;
        } else {
            this.quantity = 0;
        }
    } 

    public String getProductID() {
        return id;
    }

    public String getDescription() {
        return description;
    }


    public static void main(String [] args) {
        Item milk = new Item("Milk", "1 Gallon Milk", 2, 2.5);
        Item yogurt = new Item("Yogurt", "Peach Yogurt", 4, 0.68);
        Item bread = new Item("Bread", "Sliced Bread", 1, 2.55);
        Item soap = new Item("Soap", "6 Pack Soap", 1, 4.51);
    
        milk.setDiscount(0.15);

        double milkTotal = milk.getTotal();
        double yougurtTotal = yogurt.getTotal();
        double breadTotal = bread.getTotal();
        double soapTotal = soap.getTotal();
        double total = milkTotal + yougurtTotal + breadTotal + soapTotal;
    
        System.out.println("Thank You For Your Purchase.");
        System.out.println("Please Come Again!");
        System.out.println(milk.getDescription() + "\t $" + milkTotal);
        System.out.println(yogurt.getDescription() + "\t $" + yougurtTotal);
        System.out.println(bread.getDescription() + "\t $" + breadTotal);
        System.out.println(soap.getDescription() + "\t $" + soapTotal);
        System.out.println("Total Price \t $" + total);
    }

}