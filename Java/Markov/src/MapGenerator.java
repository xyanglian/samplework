import java.util.*;


public class MapGenerator implements TextGenerator {

	private TrainingText text;
	Random rand;
	HashMap <NGram, ArrayList<NGram>> map;

	MapGenerator() {
		
		//constructs a Random object
		
		rand = new Random();
	}

	MapGenerator(int n) {
		
		//initializes a Random Object with seed n
		
		rand = new Random(n);
	}



	public int train(Scanner source, String delimiter, int k){
		
		//creates TrainingText
		
		text = new TrainingText(source, delimiter, k);	
		
		//creates Map
		
		map = new HashMap <NGram,ArrayList<NGram>>();
		for (int i=0;i<text.size()-1; i++){

			if (! map.containsKey(text.get(i))) {

				map.put(text.get(i), new ArrayList<NGram>());

			}

			map.get(text.get(i)).add(text.get(i+1));
		}
		
		//with current state(i) as the key in the map, a list of next states as value, puts next state (i+1) in the value list
		
				return map.keySet().size();

	}

	public String generateText(int length){
		
		//NGram seed: randomly picks a start state
		
		NGram seed = text.get(rand.nextInt(text.size()));
		String string = "";
		for (int i=0;i<length;i++){
			NGram newseed = map.get(seed).get(rand.nextInt(map.get(seed).size()));
			
	         //randomly picks a new seed as next state from the value list: map.get(seed)
				
			seed = newseed; 
			string += newseed.toString();
			
			//appends seed.toString()
	
		}
		return string;
	}
}