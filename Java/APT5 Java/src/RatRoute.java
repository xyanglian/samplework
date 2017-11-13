import java.util.*;
public class RatRoute {
	int rows;
	int cols;
	int cheeserow;
	int cheesecol;
	int myrow;
	int mycol;
	char[][] map;
	public static void main(String[] args){
		
	}
public int numRoutes(String[] enc){
	rows=enc.length;
	cols=enc[0].length();
	map=new char[rows][cols];
	for(int i=0;i<enc.length;i++){
		for(int j=0;j<enc[i].length();j++){
		map[i][j]=enc[i].charAt(j);
		if(map[i][j]=='C'){
			cheeserow=i;
			cheesecol=j;
		}
		if(map[i][j]=='R'){
			myrow=i;
			mycol=j;
		}
		}
	}
	return method(myrow,mycol, Math.abs(mycol-cheesecol)+Math.abs(myrow-cheeserow));
}
private int method(int row, int col, int dist){
	if(row>=rows || row<0 || col>=cols || col<0){
		return 0;
	}
	if(row==cheeserow && col==cheesecol){
		return 1;
	}
	if(map[row][col]=='X'){
		return 0;
	}
	if(dist<Math.abs(col-cheesecol)+Math.abs(row-cheeserow)){
		return 0;
	}
	dist=Math.abs(col-cheesecol)+Math.abs(row-cheeserow);
	return method(row+1,col,dist)+method(row-1,col,dist)+method(row,col+1,dist)+method(row,col-1,dist);
}
}