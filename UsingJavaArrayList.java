import java.util.ArrayList;

class UsingJavaArrayList {
  
  public static void main(String[] args) {
    ArrayList<String> cars = new ArrayList<String>();
    cars.add("Range Rover");
    cars.add("Prius");
    cars.add("Porsche");
    cars.add("Audi");
    cars.add("Mercedes");
    System.out.println(cars);
    System.out.println(cars.size());
    System.out.println(cars.get(2));
    System.out.println(cars.set(1, "BMW"));
    System.out.println(cars.remove("Audi"));
    System.out.println(cars.indexOf("Mercedes"));

  }
  
}
