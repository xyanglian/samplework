import java.util.*;

public class ClassScores {
      public int[] findMode(int[] scores) {
    	  
    	  Arrays.sort(scores);
    	  int max = 0;
    	  for (int i = 0; i < scores.length; i++) {
    	         int count = 0;
    	         for (int j = 0; j < scores.length; j++) {
    	           if (scores[i]==scores[j])
    	               count++;
    	     }
    	    if (count >= max)
    	        max = count;
    	  }
    	  ArrayList<Integer> list = new ArrayList<>();	  
    	  for (int ele : scores){
    		  int count = 0;
 	         for (int j = 0; j < scores.length; j++) {
 	           if (ele==scores[j]){
 	               count++;
 	           }
 	         }
    		  
    		  if (count == max && !list.contains(ele)) {
    			 
    			  list.add(ele);
    		  }
    			  
    		  }
    	  int[] array = new int[list.size()];
    	  for (int i = 0;i<list.size();i++){
    		  array[i]=list.get(i);
    	  }
    	  Arrays.sort(array);
      return array;
    	  

    		  
    	  }
    	  
}
