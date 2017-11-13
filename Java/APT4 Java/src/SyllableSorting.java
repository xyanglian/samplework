import java.util.*;

public class SyllableSorting {
	public String[] sortWords(String[] words) {
		Comparator<ArrayList<String>> comparator = new Comparator<ArrayList<String>>(){
			@Override
			public int compare(ArrayList<String> one, ArrayList<String> two){
				
			
				ArrayList<String> dupone = new ArrayList<String> ();
				for (int i=0; i<one.size(); i++){
					dupone.add(one.get(i));}
				
				ArrayList<String> duptwo = new ArrayList<String> ();
				for (int i=0; i<two.size(); i++){
					duptwo.add(two.get(i));}

				Collections.sort(dupone);
				Collections.sort(duptwo);
				if (dupone.equals(duptwo)){
					for (int j=0;j<one.size();j++){
						if (one.get(j).equals(two.get(j))){
						    continue;}
						else{
						    
							return one.get(j).compareTo(two.get(j));
						}
					}
				}
					
				else{
					for (int i=0; i<Math.min(dupone.size(),duptwo.size());i++){
						if (dupone.get(i).equals(duptwo.get(i))){
						    continue;}
						else{
							return dupone.get(i).compareTo(duptwo.get(i));
						}

					}
					return dupone.size()-duptwo.size();
				
			}
				return 0;

			}
		};
			ArrayList<Character> vowel = new ArrayList<Character> ();
			vowel.add('a');
			vowel.add('e');
			vowel.add('i');
			vowel.add('o');
			vowel.add('u');
			
			

			ArrayList <ArrayList<String>> list = new ArrayList <ArrayList<String>> ();
			

			for (int i=0; i<words.length; i++){
				int index = 0 ;
				ArrayList <String> sublist = new ArrayList <String> ();
                int k = 0;
				for ( k =0; k<words[i].length()-1;k++){

					if (vowel.contains(words[i].charAt(k))){
						if (!vowel.contains(words[i].charAt(k+1))){

							sublist.add(words[i].substring(index, k+1));
							
							index = k+1;


						}
					}
					

					
				}
				sublist.add(words[i].substring(index, k+1));
				list.add(sublist);
			}

			Collections.sort(list,comparator);
			String[] answer = new String[list.size()];
			for (int i=0; i<list.size();i++){
				answer[i] = "";
				for (int j=0;j<list.get(i).size();j++){

				answer[i] += list.get(i).get(j);
				          
			//			helper method? 
			//
			//					new arraylist 
			//					store all the pieces into arraylist
			//
			//					all inside the comparator 
			//					two arraylists, one for each word,
			//					create two more copies (two sorted, two unsorted)
			//					collections.sort for each arraylist 
			//					compare two sorted arraylists, if they are the same, loop through and compare the two unsorted ones
			//					compareto until result is non0
		}
				
	}
			return answer;
	}
	 
}

