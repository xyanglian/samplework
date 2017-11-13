
public class AccessList {
	public String mayAccess(int[] rights, int minPermission) {
		String empty = "";
		for (int element : rights) {
			if (element < minPermission) {
				empty += "D";
			}
			if (element >= minPermission) {
				empty += "A";
			}
		}

		return empty;

	}
}