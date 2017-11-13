import static org.junit.Assert.*;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Random;
import java.util.Scanner;

import org.junit.BeforeClass;
import org.junit.Test;


public class TestTrie {

	public static TrieExample smallTestCase;
	public static TrieExample bigTestCase;
	
	@BeforeClass
	public static void setup() throws FileNotFoundException {
		smallTestCase = new TrieExample();
		smallTestCase.add("ape");
		smallTestCase.add("app");
		smallTestCase.add("at");
		smallTestCase.add("bat");
		smallTestCase.add("car");
		
		bigTestCase = new TrieExample();
		Scanner mostcommonwords = new Scanner(new File("src/mostcommonwords"));
		while(mostcommonwords.hasNext()){
			String nextWord = mostcommonwords.next();
			bigTestCase.add(nextWord);
		}
		mostcommonwords.close();
	}
	
	@Test
	public void testAdd(){
		assertTrue(smallTestCase.myRoot.
				children.get('a').children.get('t').isWord);
		assertTrue(smallTestCase.myRoot.
				children.get('a').children.get('p').children.get('p').isWord);
		assertTrue(smallTestCase.myRoot.
				children.get('a').children.get('p').children.get('e').isWord);
		assertFalse(smallTestCase.myRoot.
				children.get('a').isWord);
	}
	
	@Test
	public void testIsWord(){
		assertTrue(smallTestCase.isWord("ape"));
		assertTrue(smallTestCase.isWord("app"));
		assertTrue(smallTestCase.isWord("at"));
		assertTrue(smallTestCase.isWord("bat"));
		assertTrue(smallTestCase.isWord("car"));
		assertFalse(smallTestCase.isWord("a"));
		assertFalse(smallTestCase.isWord("d"));
		assertFalse(smallTestCase.isWord(""));
		
		assertTrue(bigTestCase.isWord("the"));
		assertTrue(bigTestCase.isWord("and"));
		assertTrue(bigTestCase.isWord("of"));
		assertTrue(bigTestCase.isWord("to"));
		assertTrue(bigTestCase.isWord("a"));
		assertTrue(bigTestCase.isWord("in"));
		assertTrue(bigTestCase.isWord("for"));
		assertFalse(bigTestCase.isWord("floccinaucinihilipilification"));
		assertFalse(bigTestCase.isWord("compsci201"));
		assertFalse(bigTestCase.isWord("@%&^$!"));
	}
	
	@Test
	public void testCountWordsStartingWith(){
		assertEquals(5, smallTestCase.countWordsStartingWith(""));
		assertEquals(3, smallTestCase.countWordsStartingWith("a"));
		assertEquals(2, smallTestCase.countWordsStartingWith("ap"));
		assertEquals(1, smallTestCase.countWordsStartingWith("bat"));
		assertEquals(0, smallTestCase.countWordsStartingWith("d"));
	}
	
	@Test(timeout = 100)
	public void testFirstWord(){
		assertEquals("ape", smallTestCase.firstWord());
		
		assertEquals("a", bigTestCase.firstWord());
		
		Random rng = new Random();
		String randomWord = "";
		for(int i = 0; i < 10; i++){
			randomWord += "abcdefghijklmnopqrstuvwxyz".charAt(rng.nextInt(26));
		}
		TrieExample randomTestCase = new TrieExample();
		randomTestCase.add(randomWord);
		randomTestCase.add("zzzzzzzzzzz");
		assertEquals(randomWord, randomTestCase.firstWord());
	}
}
