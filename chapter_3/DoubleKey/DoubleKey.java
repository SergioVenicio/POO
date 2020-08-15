public class DoubleKey {
    private String key1, key2;

    public DoubleKey() {
        this.key1 = "key1";
        this.key2 = "key2";
    }

    public DoubleKey(String key1, String key2) {
        this.key1 = key1;
        this.key2 = key2;
    }

    public String getKey1() {
        return this.key1;
    }

    public String getKey2() {
        return this.key2;
    }

    public void setKey1(String key1) {
        this.key1 = key1;
    }

    public void setKey2(String key2) {
        this.key2 = key2;
    }
}