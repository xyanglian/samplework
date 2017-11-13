import java.util.*;
public class TournamentRanker {
	String []names;
	String[] lost;


	public String[] rankTeams(String[] teams, String[] lostTo) {
		names = teams.clone();
		lost = lostTo.clone();
		Comparator<String> comparator = new Comparator<String>() {
			public int compare(String one, String two) {
				int count = 0;
				int counttwo = 0;
				for (int i=0;i<lost.length;i++){

					if (lost[i].equals(one)){
						count++;
					}
					if (lost[i].equals(two)){
						counttwo++;
					}
				}

				if (count!=counttwo){
					return counttwo - count;
				}
				else{
					return compare(lost[Arrays.asList(names).indexOf(one)],lost[Arrays.asList(names).indexOf(two)]);
				}

			}

				
			};
		Arrays.sort(teams, comparator);
		return teams;
	}
}