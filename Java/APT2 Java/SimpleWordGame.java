import java.util.*;
public class SimpleWordGame {

	public int points(String[] player, String[] dictionary) {
		int count = 0;
		HashSet<String> playerSet = new HashSet<String>();
		//add elements to set 
		for (int i=0; i<player.length;i++){
			
		playerSet.add(player[i]);}
		HashSet<String> dictionarySet = new HashSet<String>();
		for (int i=0; i<dictionary.length;i++){
			dictionarySet.add(dictionary[i]);}
		for (String p: playerSet){
			for (String d: dictionarySet)
			{
				if (p.equals(d)) {count+=p.length()*p.length(); break;}
				
			}
		}
		
		return count;

	
}
}