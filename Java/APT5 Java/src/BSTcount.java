public class BSTcount {
	public long howMany(int[] values) {


		long value[] = new long[values.length+1]; 

		for (int k=0;k<=values.length;k++){
			value[k] = 1;
			
		}

		for (int i=1; i<=values.length;i++){
			long count = 0;

			for (int j=0;j<i;j++){
				count += value[j]*value[i-j-1];
		        }
			value[i] = count;
				}
		return value[values.length];
	

			}

		}
