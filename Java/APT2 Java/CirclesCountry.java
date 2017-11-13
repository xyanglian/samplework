
public class CirclesCountry {
	public int leastBorders(int[] x, int[] y, int[] r, 
			int x1, int y1, int x2, int y2) {
		int count = 0;
		for (int i = 0;i<x.length; i++){
			boolean b1 = inCircle (x1,y1,x[i],y[i],r[i]);
			boolean b2 = inCircle (x2,y2,x[i],y[i],r[i]);
			if (b1 != b2) {
				count += 1 ;
				
			}
				
		}
		return count;
	}
	private boolean inCircle(int x1, int y1, int x2, int y2, int r){
		double distance = Math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)); //
		return distance<r; //return value you calculated
	}

}

