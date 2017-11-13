import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class ClientsList {

	public String[] dataCleanup(String[] names) {
		String[] array = new String[names.length];
		for (int i = 0; i < names.length; i++) {

			String[] part = names[i].split(",");
			

			if (names[i].contains(",")) {
				String s;
				s = part[0] + " " + part[1].substring(1);
				array[i] = s;
				//System.out.println(array[i]);

			} else {
				String[] part2 = names[i].split(" ");
				String v;
				v = part2[1] + " " + part2[0];
				array[i] = v;

			}
		}

			Arrays.sort(array);
			String[] answer = new String[array.length];
			for (int k = 0; k < array.length; k++) {
				String[] part3 = array[k].split(" ");
				String w;
				w = part3[1] + " " + part3[0];
				answer[k] = w;

			}

		
		return answer;

	}
	
}