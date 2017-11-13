

	//import java.util.HashMap;
	//
	//public class TrieExample {
	//	
//		public TrieNode myRoot;
	//	
//		class TrieNode{
//			boolean isWord; //true if the path to this node represents a valid word
//			HashMap<Character, TrieNode> children; //map containing all children
//			
//			public TrieNode(){
//				isWord = false;
//				children = new HashMap<Character, TrieNode>();
//			}
//		}
	//	
//		public TrieExample(){
//			myRoot = new TrieNode();
//		}
	//
//		/**
//		 * Traverse the trie, then adds the nodes to represent toAdd in the trie, 
//		 * and then sets the node representing toAdd to a word node.
//		 * @param toAdd - The word to be added
//		 */
//		public void add(String toAdd){
//			TrieNode current = myRoot;
//			for(int i = 0; i < toAdd.length(); i++){
//				char nextCh = toAdd.charAt(i);
//				//TODO: add the child if it's missing, then move to it
//			}
//			current.isWord = true;
//		}
	//	
//		/**
//		 * Determines if the input is contained in the trie
//		 * @param word - the word we're checking forimport java.util.HashMap;
	//
	//public class TrieExample {
	//	
//		public TrieNode myRoot;
	//	
//		class TrieNode{
//			boolean isWord; //true if the path to this node represents a valid word
//			HashMap<Character, TrieNode> children; //map containing all children
//			
//			public TrieNode(){
//				isWord = false;
//				ch
//		 * @return true if word is in the trie
//		 */
//		public boolean isWord(String word){
//			//TODO: Implement isWord
//			return false;
//		}
	//	
//		/**
//		 * Returns the number of words starting with prefix in this trie. If prefix
//		 * itself is a word, include it in the count. 
//		 * For example, if the trie contained "a", "at", "ate", and "b",
//		 * countWordsStartingWith("a") should return 3
//		 * countWordsStartingWith("at") should return 2
//		 * countWordsStartingWith("c") should return 0
//		 * 
//		 * We do this by first navigating to the node representing the prefix. 
//		 * We know by the prefix property all words starting with the prefix must be 
//		 * in the trie rooted at that node, so we can simply use recursion to count 
//		 * how many nodes in that trie have isWord set to true.
//		 * @param prefix - the prefix we're looking for
//		 * @return the number of words starting with prefix
//		 */
//		public int countWordsStartingWith(String prefix){
//			TrieNode current = myRoot;
//			//TODO: Move current to point to the node representing prefix, or return
//			//0 if no words starting with the prefix exist
//			return countWords(current);
//		}
	//	
//		/**
//		 * Recursive helper method for countWordsStartingWith. Counts the number
//		 * of nodes in the trie rooted at current which represent words.
//		 * @param current - the root of the subtrie
//		 * @return The number of words in the subtrie
//		 */
//		public int countWords(TrieNode current){
//			//TODO: Complete countWords using recursion
//			return 0;
//		}
	//	
//		/**
//		 * Returns the word in this trie which would come first in lexicographic 
//		 * ordering.
//		 * @return the first word as determined by lexicographic ordering
//		 */
//		public String firstWord(){
//			//TODO: Implement firstWord
//			return "";
//		}
	//}

