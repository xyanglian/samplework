import java.util.*;
public class ErdosNumber {
	private HashMap<String, ArrayList<String>> myGraph = new HashMap<String, ArrayList<String>>();
	private TreeMap<String, String> myDistMap = new TreeMap<String, String>();
	private Integer distance =0;
	
	public void getAdjList(String[] pubs) { 
		
		for (String entry : pubs){
			for (int k=0;k<entry.split(" ").length;k++){
				for (int j=0;j<entry.split(" ").length;j++){
						String firstName = entry.split(" ")[k];
						String secondName = entry.split(" ")[j];
						if (!myGraph.containsKey(firstName)){
							myGraph.put(firstName, new ArrayList<String>());
							
						}
						if (myGraph.containsKey(firstName)){
							ArrayList<String> tempArray = myGraph.get(firstName);
							if (!firstName.equals(secondName)){
								tempArray.add(secondName);
							}
						}
					}
				
				}
		
			}
			
		}

	public void bfs(String start) {
		Set<String> visited = new HashSet<String>();
		Queue<String> qu = new LinkedList<String>();
		visited.add(start); 
		qu.add(start);
		myDistMap.put(start,String.valueOf(distance));
		while (qu.size() > 0){
			String v = qu.remove();

			for(String adj : myGraph.get(v)){
				if (! visited.contains(adj)) {
					visited.add(adj);
					qu.add(adj);
					myDistMap.put(adj,String.valueOf(Integer.parseInt(myDistMap.get(v))+1));
				}
			}
		
		}
		for (String adj2:myGraph.keySet()){
			if (!myDistMap.containsKey(adj2)){
				myDistMap.put(adj2," ");
			}
		}
	}

    public String[] calculateNumbers(String[] pubs) {
        // you write code here
    	
    	getAdjList(pubs);
    	bfs("ERDOS");
    
    	int count=0;
		String[] desired = new String[myDistMap.size()];
		
    	for (String eachKey:myDistMap.keySet()){
    		if (myDistMap.get(eachKey)==" "){
    			desired[count]=eachKey;
    			count++;
    		}
    		else{
    		desired[count]=eachKey+ " "+ myDistMap.get(eachKey);
    		count++;
    		}
    	}
    	return desired;
      }
	public static void main(String[] args){
		  String[] pubs = {"ERDOS ERYX", "ERDOS FISH", "ERYX BALL", "BALL WRITER", "WRITER THEFAXMAN", "FISH WRITER"};
		  ErdosNumber test = new ErdosNumber();
		  System.out.println(Arrays.toString(test.calculateNumbers(pubs)));
	 }
}
