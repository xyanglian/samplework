import java.util.*;

public class SortByFreqs {
	public String[] sort(String[] data) {

		ArrayList<String> array;




		HashMap<String, Integer> map = new HashMap<String, Integer>();
		for (int i=0; i<data.length;i++){
			if (!map.containsKey(data[i])) {
				map.put(data[i], 1);}
			else { 
				map.put(data[i], map.get(data[i]) + 1);
			}
		}

		Comparator<String> comparator = new Comparator<String>(){
			@Override
			public int compare(String one, String two){
				int frequency = map.get(one);
				int frequency2 = map.get(two);
				if (frequency>frequency2){
					return -1;	    			
				}
				else if (frequency2>frequency){
					return 1;
				}
				else {
					return one.compareTo(two);
				}}};
			
				array = new ArrayList<String>(map.keySet());
				Collections.sort(array,comparator);
                return array.toArray(new String[array.size()]);
               

           	 

		}
	}
