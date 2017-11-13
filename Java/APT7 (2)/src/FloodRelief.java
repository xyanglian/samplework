public class FloodRelief {
      public int minimumPumps(String[] heights){
         // fill in code here
    	  char [] [] grid = new char [heights.length] [heights[0].length()];
    	  boolean [] [] pump = new boolean [heights.length] [heights[0].length()];
    	  for (int i=0;i<grid.length; i++){
    		  for (int j=0;j<grid[0].length; j++){
    			  grid[i][j] = heights[i].charAt(j);
    			  pump[i][j] = false;
    		  }
    	  }
    	  int count = 0;
    	  for (int level = 'a'; level <= 'z'; level ++){
    		  for (int i=0;i<grid.length; i++){
        		  for (int j=0;j<grid[0].length; j++){
        			  if (grid[i][j] == level && pump[i][j] == false){
        				  count ++;
        				  update(grid,pump,i,j);
        			  }
        		  }
    		  }
    	  }
    	  return count;
      }
      
      private void update (char[][] grid, boolean [][] pump, int row, int column ){
    	  if (pump[row][column]) {
    		  return;
    	  }
    	  pump[row][column] = true;
    	  if (row-1 >= 0 && grid[row-1][column]>= grid[row][column]){
    		  update (grid, pump, row-1, column);
    	  }
    	  if (row+1 < grid.length && grid[row+1][column]>= grid[row][column]){
    		  update (grid, pump, row+1, column);
    	  }
    	  if (column-1 >= 0 && grid[row][column-1]>= grid[row][column]){
    		  update (grid, pump, row, column-1);
    	  }
    	  if (column+1 < grid[0].length && grid[row][column+1]>= grid[row][column]){
    		  update (grid, pump, row, column+1);
    	  }
      }
  }