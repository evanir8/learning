public class HelloWorld {
  public static void main(String[] args) {
    String str = args.length == 0 ? "Hello World Java" : args[0];
    int starts = 0;
    int ends = str.length();
    while (true) {
      try {
        System.out.print(str.substring(starts, ends)+" "+str.substring(0, starts)+"\r");
        Thread.sleep(500);
        starts = starts == ends ? 0 : starts+1;
      }
      catch (Exception e) {
        break;
      }
    }
  }
}
