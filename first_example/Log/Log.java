public class Log {
    public void debug(String message) {
        print("DEGUB ", message);
    }

    public void info(String message) {
        print("INFO ", message);
    }

    public void warning(String message) {
        print("WARNING ", message);
    }

    public void error(String message) {
        print("ERRROR ", message);
    }

    public void fatal(String message) {
        print("Fatal ", message);
        System.exit(1);
    }

    public void print(String message, String severity) {
        System.out.println(severity + ": " + message);
    }

    public static void main(String[] args) {
        Log log = new Log();
        log.debug("Test");
    }
}