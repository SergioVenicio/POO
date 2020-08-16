public class Employee {
    private String first_name;
    private String last_name;
    private double wage;

    public Employee(String first_name, String last_name, double wage) {
        this.first_name = first_name;
        this.last_name = last_name;
        this.wage = wage;
    }

    public String getFirstName() {
        return first_name;
    }

    public String getLastName() {
        return last_name;
    }

    public double getWage() {
        return wage;
    }
}

public class CommissionedEmployee extends Employee {
    private double commision;
    private int units;

    public CommissionedEmployee(String first_name, String last_name, double wage, double commision) {
       super(first_name, last_name, wage);
       this.commision = commision;
    }

    public double calculatePay() {
        return getWage() + (commision * units);
    }

    public void addSales(int units) {
        this.units += units;
    }

    public void resetSales() {
        this.units = 0;
    }
}