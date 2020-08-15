public class Account {
    private double balance;

    public Account () {}

    public Account (double amount) {
        this.balance = amount;
    }

    public double withdrawFunds(double amount) {
        if (amount > this.balance) {
            amount = this.balance;
        }

        this.balance -= amount;
        return amount;
    }

    public void depositFunds(double amount) {
        this.balance += amount;
    }

    public double getBalance() {
        return this.balance;
    }

    public static void main (String [] args)  {
        Account a = new Account(250.0);
        Account b = new Account(999.0);
        Account c = new Account(8850.0);

        System.out.println("I have three accounts.");
        System.out.println("Account 1 has the prope balance of " + a.getBalance() + ".");
        System.out.println("Account 2 has the prope balance of " + b.getBalance() + ".");
        System.out.println("Account 3 has the prope balance of " + c.getBalance() + ".");
    }
}
