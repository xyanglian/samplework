
public class SoccerLeagues {
	public int[] points(String[] matches) {

		int[] emarray = new int[matches.length];
		for (int i = 0; i< matches.length; i++) {
			for (int j =0; j<matches.length; j++){
				if (matches[i].charAt(j)== 'W') {
					emarray[i] += 3 ; }
				if (matches[i].charAt(j)== 'D') {
					emarray[i] += 1 ; emarray[j] +=1; }
				if (matches[i].charAt(j)== 'L') {
					emarray[j] +=3; }
			
				
				

			}
		} return emarray;
	} // you write code here
}
