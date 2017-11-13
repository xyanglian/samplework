import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class BinarySearchAutocomplete implements Autocompletor {

	// uses a sorted array of Term objects, and this implementation uses binary serach to find the top terms
	
	Term[] myTerms;

	public BinarySearchAutocomplete(String[] terms, double[] weights) {
		
		// given arrays of words and weights, initializes myTerms to a corresponding array of Terms sorted lexicographically
		
		if (terms == null || weights == null)
			throw new NullPointerException("One or more arguments null");
		myTerms = new Term[terms.length];
		for (int i = 0; i < terms.length; i++) {
			myTerms[i] = new Term(terms[i], weights[i]);
		}
		Arrays.sort(myTerms);
	}

	public static int firstIndexOf(Term[] a, Term key, Comparator<Term> comparator) {
		
		// uses binary search to find the index of the first Term in the passed in array which is considered equivalent by a comparator to the given key
		
		int low = -1;
		int high = a.length;
		while (high - low > 2) {
			int mid = (low + high) / 2;
			if (comparator.compare(a[mid], key) == 0) {
				high = mid + 1;
			} else if (comparator.compare(a[mid], key) < 0) {
				low = mid;
			} else {
				high = mid;
			}
		}

		if (comparator.compare(a[low + 1], key) == 0) {
			return low + 1;
		} else {
			return -1;
		}
	}

	public static int lastIndexOf(Term[] a, Term key, Comparator<Term> comparator) {
		
		// finds the index of the last Term
		
		int low = -1;
		int high = a.length;
		while (high - low > 2) {
			int mid = (low + high) / 2 + (low + high) % 2;
			if (comparator.compare(a[mid], key) == 0) {
				low = mid - 1;
			} else if (comparator.compare(a[mid], key) < 0) {
				low = mid;
			} else {
				high = mid;
			}
		}

		if (comparator.compare(a[high - 1], key) == 0) {
			return high - 1;
		} else {
			return -1;
		}
	}

	public String[] topKMatches(String prefix, int k) {
		
		if (prefix == null)
			throw new NullPointerException();
		
		// Returns an array containing the k words in myTerms with the largest weight which match the given prefix, in descending weight order.
		
		Comparator<Term> comp = new Term.PrefixOrder(prefix.length());
		int first = firstIndexOf(myTerms, new Term(prefix, 0), comp);
		int last = lastIndexOf(myTerms, new Term(prefix, 0), comp);
		if (first == -1) {
			return new String[] {};
		}

		PriorityQueue<Term> pq = new PriorityQueue<Term>(k, new Term.WeightOrder());
		for (int i = first; i <= last; i++) {
			Term t = myTerms[i];
			if (pq.size() < k) {
				pq.add(t);
			} else if (pq.peek().getWeight() < t.getWeight()) {
				pq.remove();
				pq.add(t);
			}
		}
		int numResults = Math.min(k, pq.size());
		String[] ret = new String[numResults];
		for (int i = 0; i < numResults; i++) {
			ret[numResults - 1 - i] = pq.remove().getWord();
		}
		return ret;
	}

	@Override
	
	public String topMatch(String prefix) {
		
		// returns the largest-weight word in myTerms starting with that prefix. If no such word exists, return an empty String.
		
		if (prefix == null)
			throw new NullPointerException();
		
		Comparator<Term> comp = new Term.PrefixOrder(prefix.length());
		int first = firstIndexOf(myTerms, new Term(prefix, 0), comp);
		int last = lastIndexOf(myTerms, new Term(prefix, 0), comp);
		if (first == -1) {
			return "";
		}

		String maxTerm = "";
		double maxWeight = -1;
		for (int i = first; i <= last; i++) {
			Term t = myTerms[i];
			if (t.getWeight() > maxWeight) {
				maxTerm = t.getWord();
				maxWeight = t.getWeight();
			}
		}
		return maxTerm;
	}

}
