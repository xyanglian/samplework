import java.util.*;
public class FriendScore {
	ArrayList<ArrayList<Integer>> friendlist = new ArrayList<ArrayList<Integer>>();

	public int highestScore(String[] friends) {
		
		for (int q=0; q<friends.length;q++){

			friendlist.add([]);

		for (int i=0; i<friends.length;i++){
			for (int k=0;k<friends.length;k++){
				if (friends[i].charAt(k) == 'Y'){
					friendlist.get(k).add(i);	  
				}
				for (int j=0;j<friends.length;j++){
					if (friends[k].charAt(j) == 'Y' && friends[i].charAt(j)=='N' && j!=k){
						if (friendlist.get(k).get(j) =='N'){
							friendlist.get(k).add(j);
						}
					}
				}
			}
		}
		ArrayList<Integer> countlist = new ArrayList<Integer>();
		for (int i=0;i<friendlist.size();i++){
			countlist.add(friendlist.get(i).size());
			Collections.sort(countlist);
		}
			return countlist.get(countlist.size()-1);
		
	}


}

