import java.util.*;

public class MemberCheck {
	public String[] whosDishonest(String[] club1, 
			String[] club2, 
			String[] club3) {

	    ArrayList<String> clubb1 = new ArrayList<String> (Arrays.asList(club1));	
		ArrayList<String> clubb2 = new ArrayList<String>(Arrays.asList(club2));
		ArrayList<String> clubb3 = new ArrayList<String>(Arrays.asList(club3));	
		HashSet <String> clubbb1 = new HashSet<String>();
		clubbb1.addAll(clubb1);
		HashSet <String> clubbbb1 = new HashSet<String>();
		clubbbb1.addAll(clubb1);
		HashSet <String> clubbb2 = new HashSet<String>();
		clubbb2.addAll(clubb2);
		HashSet <String> clubbb3 = new HashSet<String>();
		clubbb3.addAll(clubb3);
		HashSet <String> completelist = new HashSet<String>();

		clubbb1.retainAll(clubbb2);
		clubbb2.retainAll(clubbb3);
		clubbbb1.retainAll(clubbb3);

		completelist.addAll(clubbb1);
		completelist.addAll(clubbb2);
		completelist.addAll(clubbbb1);

		ArrayList<String> list = new ArrayList<String>();
		list.addAll(completelist);
		Collections.sort(list);
		String [] list2 =  list.toArray(new String [list.size()]);
		return list2;}
}

