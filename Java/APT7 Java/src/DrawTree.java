

	import java.util.*;
	public class DrawTree {
	    
	    public class Node{
	        String info;
	        Node[] kids;
	        Node parent;
	        Node(String s){
	            info = s;
	        }
	    }
	    ArrayList<String> myOutput = new ArrayList<String>();
	    
	    public Node makeTree(int[] parents, String[] names, int rootIndex, Node parent){
	        Node root = new Node(names[rootIndex]);
	        ArrayList<Integer> list = new ArrayList<Integer>();
	        for(int k=0; k < parents.length; k++){
	            if (parents[k] == rootIndex){
	                list.add(k);
	            }
	        }
	        root.kids = new Node[list.size()];
	        for(int k=0; k < list.size(); k++){
	            root.kids[k] = makeTree(parents,names,list.get(k),root);
	        }
	        root.parent = parent;
	        return root;
	    }
	    
	    public void print(Node root, String prefix){
	        myOutput.add(prefix+"+-"+root.info);
	        for(Node kid : root.kids){
	            String newPrefix = prefix+"  ";
	            for(int k=0; k < root.parent.kids.length-1; k++){
	                if (root.parent.kids[k] == root){
	                    newPrefix = prefix + "| ";
	                }
	            }
	            print(kid,newPrefix);
	        }
	    }
	    
	    public String[] draw(int[] parents, String[] names){
	        int index = 0;
	        for(int k=0; k < parents.length; k++){
	            if (parents[k] == -1){
	                index = k;
	                break;
	            }
	        }
	        Node globalRoot = makeTree(parents,names,index,null);
	        myOutput.add("+-"+globalRoot.info);
	        for(Node kid : globalRoot.kids){
	            print(kid,"  ");
	        }
	        return myOutput.toArray(new String[0]);
	    }
	}

