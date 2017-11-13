public class TypingJob 
{
	public int bestTime(int[] pages) {
		return findBest(pages, 0, 0, 0, 0);
	}
	public int findBest(int[] pages, int a, int b, int c, int index){
		if(index == pages.length)
			return Math.max(Math.max(a, b), c);		
		return Math.min(Math.min(findBest(pages, a + pages[index], b, c, index+1),findBest(pages, a, b + pages[index],c,index + 1)), findBest(pages, a,b, c + pages[index], index + 1));	
	}
}