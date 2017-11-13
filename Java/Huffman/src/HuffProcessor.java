import java.util.*;

public class HuffProcessor implements Processor {

	String[] stringarray = new String[ALPH_SIZE + 1];

	@Override

	public void compress(BitInputStream in, BitOutputStream out) {

		int[] array = new int[ALPH_SIZE];

		// counts characters in file

		int var = in.readBits(BITS_PER_WORD);
		while (var != -1) {
			array[var]++;
			var = in.readBits(BITS_PER_WORD);
		}
		in.reset();

		// creates Huffman tree

		PriorityQueue<HuffNode> pq = new PriorityQueue<HuffNode>();

		// add new Huffnode to a priority queue

		for (int i = 0; i < 256; i++) {
			if (array[i] != 0) {
				HuffNode node = new HuffNode(i, array[i]);
				pq.add(node);
			}
		}

		// adds pseudo-EOF node

		HuffNode eof = new HuffNode(PSEUDO_EOF,0);
		pq.add(eof);
		System.out.println(pq.size());

		while (pq.size() > 1) {

			// polls two smallest nodes, combines them into a new HuffNode and adds the new HuffNode into Priority queue

			HuffNode smallestnode = pq.poll();
			HuffNode secondsmallestnode = pq.poll();
			HuffNode node2 = new HuffNode(-1, smallestnode.weight() + secondsmallestnode.weight(), smallestnode,
					secondsmallestnode);
			pq.add(node2);
		}
		HuffNode root = pq.poll();
		out.writeBits(BITS_PER_INT, HUFF_NUMBER);
		extractCodes(root, "");
		writerHeader(root,out);

		// compresses/writes the body

		int temp = in.readBits(BITS_PER_WORD);
		while (temp != -1)
		{
			String code = stringarray[temp];
			out.writeBits(code.length(), Integer.parseInt(code, 2));
			temp = in.readBits(BITS_PER_WORD);
		}

		// writes the pseudo-EOF

		String newstring = stringarray[PSEUDO_EOF];
		out.writeBits(newstring.length(), Integer.parseInt(newstring, 2));

	}

	// traverses tree and extract codes

	private void extractCodes(HuffNode current, String path) {
		// if current is leaf
		if (current.left() == null && current.right() == null) {
			stringarray[current.value()] = path;
			return;
		}
		extractCodes(current.left(), path + "0");
		extractCodes(current.right(), path + "1");

	}

	// writes the header

	private void writerHeader(HuffNode current, BitOutputStream out) {
		// if current is leaf
		if (current == null){
			return;
		}
		if (current.left() == null && current.right() == null) {
			out.writeBits(1, 1);
			out.writeBits(9, current.value());
		}
		else{
			out.writeBits(1, 0);
			writerHeader(current.left(), out);
			writerHeader(current.right(), out);
		}
	}

	public void decompress(BitInputStream in, BitOutputStream out) {

		//checks for Huff Number

		if (in.readBits(BITS_PER_INT) != HUFF_NUMBER){
			throw new HuffException("HuffException()");

		}
		HuffNode root = readHeader (in);
		HuffNode current = root;

		// parses body of compressed file

		int var2 = in.readBits(1);
		while (var2 != -1){
			if (var2 == 1){
				current = current.right();
			}
			else{
				current = current.left();
			}
			if (current.left() == null || current.right() == null ) {
				if (current.value() == PSEUDO_EOF){
					return;
				}
				else{
					out.writeBits(BITS_PER_WORD, current.value());
					current = root;
				}
			}
			var2 = in.readBits(1);
		}
		throw new HuffException("HuffException()");
	}

	//recreates tree from header
	private HuffNode readHeader (BitInputStream in){
		if (in.readBits(1) == 0){
			HuffNode leftchild = readHeader(in);
			HuffNode rightchild = readHeader(in);
			HuffNode combinedchild = new HuffNode(-1, leftchild.weight() + rightchild.weight(), leftchild,
					rightchild);
			return combinedchild; 
		}
		else{
			return new HuffNode(in.readBits(9),1);

		}
	}
}

