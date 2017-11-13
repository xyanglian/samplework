import java.util.*;

public class IsomorphicWords {
	public int countPairs(String[] words) {

		ArrayList<String> alist = new ArrayList<String>();

		for (int i = 0; i < words.length; i++) {
			int count = 0;
			HashMap<Character, Integer> map = new HashMap<Character, Integer>();
			StringBuilder Build = new StringBuilder();

			for (char x : words[i].toCharArray()) {

				if (!map.containsKey(x)) {
					map.put(x, count);
					count++;
				}
				Build.append(map.get(x));

			}
			alist.add(Build.toString());

		}

		int counter = 0;

		for (int k = 0; k < alist.size() - 1; k++)

		{
			for (int j = k + 1; j < alist.size(); j++) {
				if (alist.get(k).equals(alist.get(j))) {
					counter++;

				}

			}
		}
		return counter;

	}

}
