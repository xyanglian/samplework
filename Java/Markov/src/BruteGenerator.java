import java.util.*;

public class BruteGenerator implements TextGenerator{

	private TrainingText text;
	 Random rand;

	 BruteGenerator() {
		 
		 //constructs a Random object
		 
		  rand = new Random();
		  }
	 
	 BruteGenerator(int n) {
		 
		 //initializes a Random Object with seed n 
		 
		    rand = new Random(n);
		  }
	 
	public int train(Scanner source, String delimiter, int k) {
		
		//initializes the TrainingText object "text" and returns the size of the TrainingText object
		
		text = new TrainingText(source, delimiter, k);
		Set<NGram> newSet = new HashSet<NGram>();
		for (int i = 0; i < text.size(); i++) {
			newSet.add(text.get(i));
		}
		return newSet.size();
	}

	public String generateText(int length){
		
		//generates random text based on the text file
		
		NGram seed = text.get(rand.nextInt(text.size()));
		
		//determines a start state (seed)
		
		String string = "";
		for (int i=0;i<length;i++){
			ArrayList <NGram> NGramlist = new ArrayList<NGram> ();
			for (int j=0; j<text.size()-1;j++){
				if (seed.equals(text.get(j))){
					NGramlist.add(text.get(j+1));
		//for i 0 to length, for each occurrence of seed in training text, records the NGram that follows the occurrence of seed in a list
				}
			}

			NGram newseed = NGramlist.get(rand.nextInt(NGramlist.size()));
		//randomly chooses a new seed from the list
			seed = newseed; 
			string += newseed.toString();
		//appends seed.toString to output

		}
		return string ; 
	}
}
