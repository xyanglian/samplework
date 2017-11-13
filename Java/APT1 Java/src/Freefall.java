
public class Freefall {
	public double fallingDistance(double time, double velo){
		
       double answer = velo * time + (1.0/2.0)*(9.8*Math.pow(time, 2));
       return answer;
      }
  }