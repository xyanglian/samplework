
public class PassObject {
  static Test monitor = new Test();
  public static void main(String[] args) {
    int i = 1;
    System.out.println("i-- : " + i--); // Post-decrement
    System.out.println("++i : " + ++i); // Pre-increment
    System.out.println("i++ : " + i++); // Post-increment
    System.out.println("--i : " + --i); // Pre-decrement

  }
}