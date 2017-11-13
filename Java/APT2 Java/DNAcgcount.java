
public class DNAcgcount {
	 public double ratio(String dna)
	    {
		 double answer = 0.0;
		int count = 0; //fix this
		 for (char chrcter : dna.toCharArray()){ //this is wrong 
			 if (chrcter == 'c' || chrcter == 'g'){
				 count += 1; }}
		int lengthdna = dna.length();
if (lengthdna == 0) {
return answer;
}
		answer = ((double) count)/lengthdna;  
		return answer; //check your return type
				 
			 
	    }
	}

