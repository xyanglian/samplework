import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class NumberPrinter {

	public static void printSmallNumbers(Scanner source) {
		while (source.hasNext()) {
			int nextInt = source.nextInt();
			if (source.hasNext()) {
				if ((nextInt = source.nextInt()) <= 5) {
					System.out.println(nextInt);
				}
			} else {
				source.next();
			}
		}
	}

	public static void main(String[] args) {
		try {
			Scanner input = new Scanner(new File("Discussion3/src/input.txt"));
			printSmallNumbers(input);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

}
