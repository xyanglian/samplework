
public class GalaxyTrip {
	 public int[] possibleValues(String[] dependencies) {
//	V* = empty set
//			Sizes = list of integers
//			For each vertex v:
//			If v not in V*:
//			V = empty set
//			Run DFS/BFS on v, using V as the visited set for DFS/BFS
//			Add V.size to sizes
//			Add all elements in V to V*
//		 S = set of answers (global variable)
//				 count(freq, 0, 0)
//				 count(freq, total, pos):
//				 if total != 0, add total to S //add one possible answer
//				 if pos >= sizes’ length, return //we’ve iterated through whole
//				 //list, we’re done
//				 for i from 0 to freq[pos]:
//				 count(freq, total+i*pos, pos+1) //try adding a different
//				 //number of components of each size
}
