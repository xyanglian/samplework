import java.util.ArrayList;
import java.util.Collections;

public class SpreadingNews {
    // Create an ArrayList to store subordinates' times
	// Does this go here as an instance variable 
	//   or as a local variable?
	// private ArrayList<Integer> subTime = new ArrayList<Integer>();

	public int minTime(int[] supervisors) {
	    // Helper method w the root that recursively calls itself
		return minBoss(0, supervisors);
	}
	 	
	private int minBoss(int boss, int[] supervisors) {
	    // Create an ArrayList to store subordinates' times
		// Does this go here as a local variable
		//   or as an instance variable?
		ArrayList<Integer> subTime = new ArrayList<Integer>();
		
		// Find the time it takes me... One call to each subordinate
		for (int subord = 0; subord < supervisors.length; subord++) {
			if (boss == supervisors[subord]) {
				subTime.add(minBoss(subord, supervisors));
			}
		}
		// Leaf = base case (if no subordinates)
		if (subTime.size() == 0) {
			return 0;
		}
		// Sort the subTimes, compute max of time + i
		Collections.sort(subTime, Collections.reverseOrder());
		int max = subTime.get(0) + 1;
		for (int i = 1; i < subTime.size(); i++) {
			if (max < subTime.get(i) + i + 1) {
				max = subTime.get(i) + i + 1;
			}
		}
		return max;
	
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] org = {-1,0,0};
		SpreadingNews sn = new SpreadingNews();
		int answer = sn.minTime(org);
		System.out.println(answer);
	}
}