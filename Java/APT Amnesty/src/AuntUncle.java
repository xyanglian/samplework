import java.util.*;

public class AuntUncle {
	public String[] list(String[] parents, String target) {

		Map<String, String[]> familyTree = new TreeMap<String, String[]>();
		ArrayList<String> childrenlist = new ArrayList<String>();
		for(String s : parents){
			String[] data = s.split(" ");
			String kid = data[2];
			String[] parentsofchild = new String[2];
			parentsofchild[0] = data[0];
			parentsofchild[1] = data[1];
			familyTree.put(kid,parentsofchild);
		}
		
//		  find grandparents
      HashSet<String> grands = new HashSet <String>();
     
      // find grandparents, and then find grandparents' children
     
      String[] parentsofchild = familyTree.get(target);
      if (!familyTree.containsKey(target)){
    	  return new String[0];
      }

	String[] grands0 = familyTree.get(parentsofchild[0]);
	String[] grands1 = familyTree.get(parentsofchild[1]);
	if (grands0 != null){
		
    grands.add(grands0[0]);
    grands.add(grands0[1]);

	}
	if (grands1 != null){
		
	    grands.add(grands1[0]);
	    grands.add(grands1[1]);

		}
	//find grandparents' children
     HashSet<String> childrenofgrands  = new HashSet <String>();


     for(String s : grands){
         for(String o : familyTree.keySet()){
        		 // see which people have the grandparents as a parent
        		 if (familyTree.get(o)[0] .equals(s) || familyTree.get(o)[1] .equals(s) ){
        			 childrenofgrands.add(o);
        		 }
        	 }
       
     }
     childrenofgrands.remove(familyTree.get(target)[0]);
     childrenofgrands.remove(familyTree.get(target)[1]);
     childrenofgrands.remove(target);
     String[] answerarray = childrenofgrands.toArray(new String[childrenofgrands.size()]);
     childrenofgrands.toArray();
     Arrays.sort(answerarray);
	return answerarray;
	}
}