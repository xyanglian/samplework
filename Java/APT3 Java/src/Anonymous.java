import java.util.HashMap;

public class Anonymous {
	private HashMap<Character,Integer> avail;	
	private HashMap<Character,Integer> need;
	
	public Anonymous(){
		avail = new HashMap<Character,Integer>();
		need = new HashMap<Character,Integer>();
	}
	
	public int howMany(String[] headlines, String[] messages) {
		int total =0;
		initializeAvail(headlines, avail);
		for (int msgNum = 0; msgNum < messages.length; msgNum++){
			initializeNeed(messages[msgNum], need);
		    if (canWrite(avail, need)) {
		    	total++;
		    }
		}
        return total;
	}


	private void initializeAvail(String[] headlines, 
			HashMap<Character, Integer> avail2) {
		for (int sentence=0; sentence < headlines.length; sentence++){
			for (int letr = 0; letr < headlines[sentence].length(); letr++){
				Character current = headlines[sentence].charAt(letr);
				current = Character.toUpperCase(current);
				
				if (Character.isUpperCase(current)) {
					if (avail.containsKey(current)) {
						Integer count = avail.get(current);
						count++;
						avail.put(current, count);
					} else {
						avail.put(current, (Integer) 1);
;					}
				}
			}
		}
	}

	private void initializeNeed(String message, HashMap<Character,Integer> need) {
		need.clear();
		int count = 0;
	
		for (int letter = 0; letter < message.length(); letter++) {
			char currentChar = Character.toUpperCase(message.charAt(letter));
			
			if (Character.isUpperCase(currentChar)) {
				Character current = (Character) currentChar;
				if (need.containsKey(current)) {
					count = need.get(currentChar);
					count++;
				} else {
					count = 1;
				}
				need.put(current, (Integer) count);
			}
		}
	}


	private boolean canWrite(HashMap<Character,Integer> avail, 
			HashMap<Character,Integer> need) {
		for (Character key : need.keySet() ) {
	    	if (avail.containsKey(key)) {
	    		if (need.get(key) > avail.get(key)) {
	    			return false;
	    		}
	    	} else {
	    		return false;
	    	}
		}
		return true;
	}

}
