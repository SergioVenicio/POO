package chapter_4.Point;

public class TwoDimensionalPoint {
    private double x;
    private double y;

    public TwoDimensionalPoint(double x, double y) {
        this.x = x;
        this.y = y;
    }

    protected double getX() {
        return x;
    }

    protected double getY() {
        return y;
    }

    public String toString() {
        return "I'm a 2 dimensional point.\n" +
                "My x coordinate is: " + this.getX() + "\n" +
                "My y coordinate is: " + this.getY();
    }
}


public class ThreeDimensionalPoint extends TwoDimensionalPoint {
    private double z;
    public ThreeDimensionalPoint(double x, double y, double z) {
        super(x, y);
        this.z = z;
    }

    private double getZ() {
        return z;
    }

    public String toString() {
        return "I'm a 3 dimensional point.\n" +
                "My x coordinate is: " + this.getX() + "\n" +
                "My y coordinate is: " + this.getY() + "\n" +
                "My z coordinate is: " + this.getZ();
    }
}
