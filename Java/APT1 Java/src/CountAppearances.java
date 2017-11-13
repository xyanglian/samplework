
public class CountAppearances {
	public int numberTimesAppear(int number, int digit) {
		int count = 0;
		String iDontKnowWhatIAm = number + "";
       for (char element : iDontKnowWhatIAm.toCharArray()){
    	   if (element == (digit + "").charAt(0)){
    		   count += 1; } } 
    return count;
 }
}

