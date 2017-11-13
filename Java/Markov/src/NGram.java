import java.util.Arrays;
import java.util.List;

public class NGram implements Comparable<NGram> {

	private String[] contents;
	private String separator;

	public NGram(List<String> source, String sep) {
		separator = sep;
		contents = new String[source.size()];
		contents = Arrays.copyOf(source.toArray(new String[source.size()]), source.size());
	}

	public int compareTo(NGram other) {
		
		//compares NGrams by looping over words 

		for (int i = 0; i < Math.min(contents.length, other.contents.length); i++) {
			if (!contents[i].equals(other.contents[i])) {
				return contents[i].compareTo(other.contents[i]);
			}
		}
		return contents.length - other.contents.length;
	}  

	public boolean equals(Object o) {
		
		// makes sure that o is not null, that o is an NGram, that both NGrams have the same length 
		
		if(o == null || o.getClass() != this.getClass()) return false;
		if(contents == o && this.getClass() == o.getClass()) return true;
		NGram other = (NGram) o;
		if (this.contents.length != other.contents.length) return false;
		for(int i=0; i<this.contents.length; i++){
		if(! contents[i] .equals( other.contents[i]) ) return false;
		}
		return true;
	}

	public int hashCode() {
		
		// uses prime numbers to generate a good hashCode 
		
		int hashValue = 1;

			 for (int i=0; i< contents.length; i++) {
			 hashValue += hashValue*(i*i%393)* 2017/ 999 * contents[i].hashCode();
			 }
			 return hashValue;
			 }

	public String toString() {
		
		// returns the only relevant information to Markov, that is, the final element of contents
		
		return contents[contents.length - 1] + separator;
	}
}