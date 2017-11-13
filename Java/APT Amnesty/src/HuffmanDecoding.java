import java.util.*;

public class HuffmanDecoding {

	public String decode(String archive, String[] dictionary) {
		String answer = "";
		String empty = "";
		List<String> dict = Arrays.asList(dictionary);
		for (int I = 0; I < archive.length(); I++) {
			empty += archive.charAt(I);
			if (dict.contains(empty)) {
				answer +=  (char) (dict.indexOf(empty) + 'A');
				empty = "";

			}
		}
		return answer;
	}

//	public static void main(String[] args) {
//		HuffmanDecoding tester = new HuffmanDecoding();
//		String a = "101101";
//		String[] b = { "00", "10", "01", "11" };
//		System.out.println(tester.decode(a, b));
//	}
}