
/*************************************************************************
 * @author Kevin Wayne
 *
 * Description: A term and its weight.
 * 
 *************************************************************************/

import java.util.Comparator;

public class Term implements Comparable<Term> {

	private final String myWord;
	private final double myWeight;

	public Term(String word, double weight) {
		
		// stores a String value and the corresponding positive weight of the word
		// implements Comparable to give a default comparison
		
		if (word == null)
			throw new NullPointerException();
		if (weight < 0)
			throw new IllegalArgumentException();
		   
		myWord = word;
		myWeight = weight;
	}

	public static class PrefixOrder implements Comparator<Term> {
		private final int r;
		
		// sorts terms lexicographically, but only uses the first r letters

		public PrefixOrder(int r) {
			this.r = r;
			
			new Term.ReverseWeightOrder();  
		}

		public int compare(Term v, Term w) {
			
			// compares v and w lexicographically using only their first r letters
		
			if(v.getWord().length()<r || w.getWord().length() < r){
				return v.compareTo(w);
			}
			for (int i=0; i<r;i++)
				if (v.getWord().charAt(i)!=(w.getWord().charAt(i))){
					return v.getWord().charAt(i)-w.getWord().charAt(i);
				}
			return 0;
		}
	}

	public static class ReverseWeightOrder implements Comparator<Term> {
		public int compare(Term v, Term w) {
			
//compares Terms using only their weights, in descending order

			if (v.getWeight() == w.getWeight()){
				return 0;
			}
			if(v.getWeight() > w.getWeight()){
				return -1;
			}
			if(v.getWeight() < w.getWeight()){
				return 1;
			}
			return 0;
		}
	}

	public static class WeightOrder implements Comparator<Term> {
		public int compare(Term v, Term w) {
			
			// compares Terms using only their weights, in ascending order 

			if (v.getWeight() == w.getWeight()){
				return 0;
			}
			if(v.getWeight() > w.getWeight()){
				return 1;
			}
			if(v.getWeight() < w.getWeight()){
				return -1;
			}
			return 0;
		}
	}

	public int compareTo(Term that) {
		return myWord.compareTo(that.myWord);
	}


	public String getWord() {
		
	//getter methods, which are used in other classes that use Term 
		
		return myWord;
	}

	public double getWeight() {
		
		//getter methods, which are used in other classes that use Term 

		return myWeight;
	}

	public String toString() {
		return String.format("%14.1f\t%s", myWeight, myWord);
	}
}


