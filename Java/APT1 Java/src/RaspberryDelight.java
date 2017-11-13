
public class RaspberryDelight {
	public int toasts(int upper_limit, int layer_count) {
		int answer = 100;
		if ((layer_count % upper_limit) > 0) {
			answer = (layer_count / upper_limit) + 1;
		}
		if ((layer_count % upper_limit) == 0) {
			answer = layer_count / upper_limit;
		}
		return answer;
	}
}