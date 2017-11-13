import java.util.PriorityQueue;

//General trie/priority queue algorithm for implementing Autocompletor
/// * 
// * @author Austin Lu

public class TrieAutocomplete implements Autocompletor {

	// Root of entire trie

	protected Node myRoot;

	public TrieAutocomplete(String[] terms, double[] weights) {

		// initializes the trie rooted at myRoot, and adds all nodes necessary to represent the
		if (terms == null || weights == null)
			throw new NullPointerException("One or more arguments null");
		// represents the root as a dummy/placeholder node
		myRoot = new Node('-', null, 0);

		for (int i = 0; i < terms.length; i++) {
			add(terms[i], weights[i]);
		}
	}

	private void add(String word, double weight) {

		// adds the word with given weight to the trie. If word already exists in the trie, no new nodes should be created, but the weight of word should be updated.

		if(word == null)
			throw new NullPointerException();
		if (weight < 0)
			throw new IllegalArgumentException();
		Node current = myRoot;
		for (int i = 0; i < word.length(); i++) {
			char nextCh = word.charAt(i);
			if (current.mySubtreeMaxWeight < weight) {
				current.mySubtreeMaxWeight = weight;
			}
			if (current.children.get(nextCh) == null) {
				current.children.put(nextCh, new Node( nextCh, current, weight));
			}
			current = current.children.get(nextCh);
		}
		current.isWord = true;
		current.myWeight = weight;
		current.myWord = word;

		if (current.mySubtreeMaxWeight <= weight) {
			current.mySubtreeMaxWeight = weight;
		}
		else {
			while (current != null) {
				double max = current.myWeight;
				for (Node child : current.children.values()) {
					max = Math.max(max, child.mySubtreeMaxWeight);
				}
				current.mySubtreeMaxWeight = max;
				current = current.parent;
			}
		}
	}

	@Override

	public String[] topKMatches(String prefix, int k) {
		
		// returns an array containing the k words in the trie with the largest weight which match the given prefix, in descending order.
		
		if (prefix == null)
			throw new NullPointerException();
		Node current = myRoot;
		for (int i=0;i<prefix.length();i++){
			char nextCh=prefix.charAt(i);
			if (!current.children.containsKey(nextCh)) {
				return new String[0];
			}
			current = current.children.get(nextCh);
		}

		PriorityQueue<Node> queue = new PriorityQueue<>(new Node.ReverseSubtreeMaxWeightComparator());
		PriorityQueue<Node> matches = new PriorityQueue<>();
		queue.add(current);
		while (!queue.isEmpty()) {
			if (matches.size() == k) {
				if (matches.peek().myWeight >= queue.peek().mySubtreeMaxWeight) {
					break;
				}
				else {
					matches.poll();
				}
			}
			current = queue.poll();
			if (current.isWord) {
				matches.add(current);
			}
			for (Node child : current.children.values()) {
				queue.add(child);
			}
		}

		String[] ret = new String[matches.size()];
		for (int i = 0; i < ret.length; i++) {
			ret[ret.length - i - 1] = matches.poll().myWord;
		}
		return ret;

	}

	@Override

	public String topMatch(String prefix) {
		
		// Given a prefix, returns the largest-weight word in the trie starting with that prefix.
		 
		
		if (prefix == null)
			throw new NullPointerException();
		Node current = myRoot;
		for (int i=0;i<prefix.length();i++){
			char nextCh=prefix.charAt(i);
			if (!current.children.containsKey(nextCh)) {
				return "";
			}
			current = current.children.get(nextCh);
		}
		while (current.mySubtreeMaxWeight != current.myWeight){
			for (Node child : current.children.values()) {
				if (child.mySubtreeMaxWeight == current.mySubtreeMaxWeight) {
					current = child;
					break;
				}

			}

		}
		return current.getWord();

	}
}

