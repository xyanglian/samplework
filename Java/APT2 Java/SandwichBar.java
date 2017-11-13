import java.util.HashSet;

public class SandwichBar {

	public int whichOrder(String[] available, String[] orders) {
		HashSet<String> availableSet = new HashSet<String>();
		for (String s : available){
			availableSet.add(s);
		}
		String[] newArray = new String[availableSet.size()];
		int l = 0;
		for (String s: availableSet) {
			newArray[l]= s;
			l++;
		}
		int count = 0;
		
		for (int i = 0; i < orders.length; i++) {
            count = 0;  

			String[] myorder = orders[i].split(" ");
            
			for (int k = 0; k < myorder.length; k++) {

				for (int j = 0; j < newArray.length; j++) {
					if (newArray[j].equals(myorder[k])) {
						count += 1;
					}
					

				}
				
			}
			
			if (count == myorder.length){
				return i ;
				
			}
		}
	
	return -1 ;

}
	
}