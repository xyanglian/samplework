import java.util.Iterator;
import java.util.Stack;

import com.sun.xml.internal.bind.v2.runtime.unmarshaller.XsiNilLoader.Array;

public class LinkStrand implements IDnaStrand, Iterator<String> {


	 // creates a strand representing an empty DNA strand, length of zero


	public class Node {
		// linked list is stored using nodes
		String value; // The string value contained by this node
		Node next; // A pointer to the next node in the linked list

		public Node() {
			value = null;
			next = null;
		}

		public Node(String s) {
			value = s;
			next = null;
		}

		public Node(String s, Node n) {
			value = s;
			next = n;
		}
	}

	// links the nodes to form the linked list
	private Node myHead; 
	private Node myTail; 
	private int myAppends;
	private long mySize;
	private Node current2;

	public LinkStrand() {
		 
		// creates empty dna strand ("")

		initialize("");

	}

	public LinkStrand(String s) {
		
		// creates a Node holding dna


		initialize(s);
	}

	@Override
	public void initialize(String source) {
		
		// creates one node upon initialization, and sets/resets all of the instance variables
	
		myHead = new Node(source);
		myTail = myHead;
		myAppends = 0;
		mySize = source.length();
		current2 = myHead;
	}

	@Override
	public IDnaStrand cutAndSplice(String enzyme, String splicee) {
		
		// replaces every instance of first argument with second argument
		// LinkStrand has only a single node, so the original LinkStrand is identical before and after calling cutAndSplice and the return value is a new LinkStrand
		
		StringBuilder stringinie = new StringBuilder(myHead.value);
		StringBuilder search = stringinie;
		int pos = 0;
		int start = 0;
		boolean first = true;
		LinkStrand ret = null;	

		while ((pos = search.indexOf(enzyme, pos)) >= 0) {
			if (first) {
				ret = new LinkStrand(search.substring(start, pos));
				first = false;
			} else {
				ret.append(search.substring(start, pos));

			}
			start = pos + enzyme.length();
			ret.append(splicee);
			pos++;
		}

		if (start < search.length()) {
			
			// special case: If the enzyme is never found, returns an empty String.
			
			if (ret == null) {
				ret = new LinkStrand("");
			} else {
				ret.append(search.substring(start));
			}
		}
		return ret;
	}

	@Override
	public long size() {
		
		// returns the number of nucleotides/base-pairs in this strand
		
		return mySize;
	}

	@Override
	public String strandInfo() {
		
		// returns some string identifying this class, representing this strand and its characteristics

		return this.getClass().getName();

	}

	@Override
	public String getStats() {
		
		// returns a string that can be printed to reveal information about what this object has encountered as it is manipulated by append and cutAndSplice

		return String.format("# append calls = %d", myAppends);
	}

	@Override
	public String toString() {
		
		// returns the sequence of DNA this object represents as a String
		
		StringBuilder stringinie = new StringBuilder();
		Node current = myHead;
		while (current != null) {
			stringinie.append(current.value);
			current = current.next;
		}
		return stringinie.toString();

	}

	@Override
	public void append(IDnaStrand dna) {
		
		// appends a strand of DNA to this strand
		
		if (dna instanceof LinkStrand) {
			
			// 	if dna instance of LinkStrand, tails points to new LinkStrand's head
			
			LinkStrand var = (LinkStrand) dna;
			myTail.next = (Node) dna;

		} else {
			
			// else, creates a Node from IDnaStrand.toString
			
			Node newNode = new Node(dna.toString());
		}
	}

	@Override
	public void append(String dna) {
		// appends a strand of dna data to this strand
		Node dgh = new Node(dna);
		myTail.next = dgh;
		myTail = dgh;
		mySize += dna.length();
		myAppends++;

	}

	@Override
	public IDnaStrand reverse() {
		
		// returns an IDnaStrand that is the reverse of this strand
		
		Stack <Node> stack = new Stack<Node>() ;
		Node current = myHead;
		while ( current != null) {
			stack.push(current);
			current = current.next;
		}
		LinkStrand strand = new LinkStrand();
		while (!stack.empty()) {
			Node node = stack.pop();
			StringBuilder stringinie = new StringBuilder(node.value);
			strand.append(stringinie.reverse().toString());
		}
		return strand; 
	}

	
			@Override
			public String next() {
				
				// returns the next element in the underlying LinkedList data structure
				
			    Node current3 = current2;
				current2 = current2.next;
				return current3.value;
	}

	@Override
	public boolean hasNext() {
		
		// returns true if next evaluates correctly False if next returns with an error
		
		if (current2 == null){
		return false;
		}
		return true;
	}
}
