package chapter_4.Moody;

public abstract class Moody {
    protected abstract String getMood();

    public void queryMood() {
        System.out.println("I feel " + getMood() + " today!");
    }
}

public class Sad() {
    protected String getMood() {
        return "sad";
    }

    public void cry() {
        System.out.println("boo hoo");
    }
}

public class Happy() {
    protected String getMood() {
        return "happy";
    }

    public void laugh() {
        System.out.println("hahahahaha");
    }
}