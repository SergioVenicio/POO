public interface Queue {
    public void enqueue(Object obj);
    public Object dequeue();
    public boolean isEmpty();
    public Object peek();
}