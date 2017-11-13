
public class DNAMutate {
	public String mutate(String dna) {
        return new StringBuilder(dna).reverse().toString();
    }
 }