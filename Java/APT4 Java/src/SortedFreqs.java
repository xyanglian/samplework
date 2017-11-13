import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;

public class SortedFreqs {
	public int[] freqs(String[] data) {
		ArrayList<String> array;

		HashMap<String, Integer> map = new HashMap<String, Integer>();
		for (int i = 0; i < data.length; i++) {
			if (!map.containsKey(data[i])) {
				map.put(data[i], 1);
			} else {
				map.put(data[i], map.get(data[i]) + 1);
			}
		}

		array = new ArrayList<String>(map.keySet());
		Collections.sort(array);
		int[] newarray = new int[array.size()];
		for (int i = 0; i < array.size(); i++) {
			map.get(array.get(i));
			newarray[i] = map.get(array.get(i));
		}
		return newarray;
	}
}
