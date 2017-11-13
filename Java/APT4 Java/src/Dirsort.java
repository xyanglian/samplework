import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class Dirsort {
	public String[] sort(String[] dirs) {
		Comparator<String> comparator = new Comparator<String>() {
			@Override
			public int compare(String one, String two) {
				int slash = 0;
				int slash2 = 0;
				for (int i = 0; i < one.length(); i++) {
					if (one.charAt(i) == '/') {

						slash++;
					}

				}
				for (int i = 0; i < two.length(); i++) {
					if (two.charAt(i) == '/') {
						slash2++;

					}
				}
				if (slash != slash2) {
					return slash - slash2;
				} else {
					return one.compareTo(two);
				}
			}
		};
		
		ArrayList<String> answer = new ArrayList<String> (Arrays.asList(dirs));	
		Collections.sort(answer,comparator);
        return answer.toArray(new String[answer.size()]);
	}
}
