import java.util.Arrays;
import java.util.Comparator;

public class TheBestName {

	public class LengthAlpha implements Comparator<String> {

		@Override
		public int compare(String o1, String o2) {
			if (o1.equals("JOHN")) {
				return -10;
			}

			if (o2.equals("JOHN")) {
				return 10;
			}
			int score = 0;
			for (int i = 0; i < o1.length(); i++) {
				score += o1.charAt(i) - 64;
			}

			int score2 = 0;
			for (int j = 0; j < o2.length(); j++) {
				score2 += o2.charAt(j) - 64;
			}

			if (score2 == score) {
				return o1.compareTo(o2);
			}
			return score2 - score;

		}

	}

	public String[] sort(String[] names) {
		Arrays.sort(names, new LengthAlpha());
		return names;
	}

}
