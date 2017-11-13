


import java.util.*;
import java.io.FileReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.lang.*;

public class cachesim {
	
	// create main memory as a string array 
	public static String [] mainmemory = new String[(int)Math.pow(2,24)];
	
	// create the method intializememory to intialize memory to all "00" since
	// each bytes corresponds to two hex numbers 
	public static String[] initializememory (String[] inputmemory){
		
		// initialize main memory to "00"
		for (int a =0; a< inputmemory.length; a++){
			
			inputmemory[a]="00";
		}
		return inputmemory;
	}
	
// this function concatenates strings in the form of a string array 
//given a start, end index and a string array
		
		public static String[] concatenatemain (String [] memory, int startindex,int endindex){
			
			String[] memoryarray = new String[endindex-startindex];
			
			int count = 0; 

			for (int i=startindex;i<endindex;i++){
				
				memoryarray[count] = memory[i];
				count = count +1; 
			}
			return memoryarray;	
		}
		
    // declare public variables to ba accessed throughout the file 
	public static String filename; 
	public static Integer cachesize;
	public static Integer assocs;
	public static String writewhat;
	public static Integer blocksize;
	public static Integer frame;
	public static Integer numsets;
	public static String loadorstore;
	public static String address;
	public static Integer numberofbytes;
	public static String valuetowrite;
	// size of offset
	public static Integer offsetsize;
	// size of index
	public static Integer indexsize;
	// actual index bits
	public static String indexb;
	public static Integer tagbitssize;
	// actual tag bits
	public static String tagb;
	// actual offset bits 
	public static String offsetb;
	
	// main function 
	public static void main (String[] args) {
		
		
		// parse the file
		filename = args[0];
		// convert string to integer 
		cachesize = Integer.valueOf(args[1]);
		assocs = Integer.valueOf(args[2]);
		writewhat = args[3];
		blocksize = Integer.valueOf(args[4]);
		// convert cachesize (KB) to B by multiplying it by 1024
		frame = cachesize*1024/blocksize;
		numsets = frame/assocs;
		// calculate offsetsize 
		offsetsize = (int) (Math.log(blocksize)/Math.log(2));
 		// calculate indexsize 
		indexsize = (int) (Math.log(numsets)/Math.log(2));
		// calculate tagbitssize 
		tagbitssize = 24-offsetsize-indexsize;
		// declare a new cache
		cache mycache = new cache();
		// initialize main memory
		mainmemory = initializememory(mainmemory);
		// call readfile and pass the file in as one of the arguments 
		readfile(filename,mycache);
		
	}
	
	// create a class for frames/blocks 
	public static class frame {
		
		Integer validbit;
		Integer dirtybit;
		String tagbits;
		
		// blockdata is an array of bytes 
		String[] blockdata = new String[blocksize];
		// a constructor to construct new frames 
		public frame(String tagbit,String[] datablock, Integer dirtybit){
			
			//set tagbits, blockdata, and dirtybit
			// dirtybit is always 1 because if it is in a frame, it will
			// be added to a cache and thus become dirty 
			tagbits=tagbit;
			blockdata=datablock ;
			dirtybit = 1;
			}
		}

	// create cacheset, which is a set of frames/blocks as linked lists 
	public static class cacheset{
		LinkedList<frame> framelinkedlist = new LinkedList<frame>();
	}
	
	// set of sets which make a cache 
	public static class cache{
		// an array that is the size of the number of sets 
		cacheset [] cachearray = new cacheset[numsets];
	}

	// convert hex to binary 
	public static String converthextobinary (String hexa){
		// need to chop off first two bits before converting from hex 
		// because the hex numbers in address start with 0x, which 
		// the program cannot read 
		hexa = hexa.substring(2);
		int i = Integer.parseInt(hexa, 16);
		String bina = Integer.toBinaryString(i);
		// left fill the binary number with "0"'s
		// until the length of the binary is 
		// four times that of the hex 
		while (bina.length()!= hexa.length()*4){
			bina = "0"+bina;
		}
		return bina;
	}

	// convert hex to binary; this is for hex numbers to do not start with 0x 
	// so I do not need to chop off the first two bits 
	public static String converthextobinarywithno0 (String hexa){
		
		int i = Integer.parseInt(hexa, 16);
		String bina = Integer.toBinaryString(i);
		while (bina.length()!= hexa.length()*4){
			bina = "0"+bina;
		}
		return bina;
	}
	// write a function to read tracefile 
	public static void readfile (String nameoffile, cache mycache ) {
		
		
		try{
			FileReader file = new FileReader(nameoffile);
			Scanner source = new Scanner (file);
		
			while (source.hasNextLine()){
			
				String fileline = source.nextLine();
				// split the line by spaces 
				String[] parsed = fileline.split("\\s+");
				loadorstore = parsed[0];
				// converting address to 24 bits 
				address = converthextobinary(parsed[1]);				
				// slice the 24 bits address to get the index bits 
				indexb = address.substring(tagbitssize, 24-offsetsize);
				// slice the 24 bits address to get the tag bits 
				tagb = address.substring(0,tagbitssize);
				// slice the 24 bits address to get the offset bits
				offsetb = address.substring(tagbitssize+indexsize, 24);
				// get the access size in terms of number of bytes 
				numberofbytes = Integer.valueOf(parsed[2]);
			// if the instruction is store not load 
				if (loadorstore.equals("store")){
						// initialize hit to be 0, if hit ends up being greater than
					// 0 then, there is a store hit; otherwise, it's a store miss
						int hit = 0;					    
						// do not need to convert valuetowrite, LEAVE as HEX
						valuetowrite = parsed[3];
						// turn valuetorwite into string array
						String[] valuewritearray = valuetowrite.split("");
						// because I want to store two hex numbers for each byte,
						// I create a new string array so as to store two of what's 
						// in valuwritearray in to one position in valuetowritearray
						// the length of valuetowritearray corresponds to blocksize
						String[] valuetowritearray = new String[blocksize];
						// intialize everything in valuetowritearray to 00 firts
						for (int e=0;e<blocksize;e++){
							valuetowritearray[e] = "00";
						}
								// keep a count value 
								int value = 0;
								Integer blockoffsetdec;
								// convert blockoffset to decimal for indexing purposes
								blockoffsetdec = Integer.parseInt(offsetb,2);

// store what's in valuewritearray to valuetowritearray and index it according to blockoffset (decimal)
								// so I store the values in the correct places since everything else 
								// has been intialized to "00"
									for (int g =blockoffsetdec;g<blockoffsetdec+valuetowrite.length()/2;g++){

										valuetowritearray[g] = valuewritearray[value+1]+valuewritearray[value+2];

										// increment by 2 because I'm updating two elements at a time for 
										// valuewritearray
										value = value +2 ; 
		
								}

						// if store + writeback 
						if (writewhat.equals("wb")){
														
							// convert indexb, from binary to decimal 
							int decindexb = Integer.parseInt(indexb,2);
	
							// if this is null, i.e., the first time it is readl; it's naturally
							// a store miss 
							if (mycache.cachearray[decindexb] == null){
								// it's a miss
								hit = 0;	
							}
							// else if the size of the linked list is 0; then it is naturally a 
							// miss here too
							else if (mycache.cachearray[decindexb].framelinkedlist.size()==0){
								// it's a miss
								hit = 0;
							}
							
								// otherwise, check if the frames' tagbits equal the tagbits given
								else if (mycache.cachearray[decindexb].framelinkedlist.size()!=0){
								
									int linkedlistsize = mycache.cachearray[decindexb].framelinkedlist.size();
								
									// use  a for loop to check if there exists a frame in the set whose 
									// tagbits equal the target tagbits 
									for (int l = 0; l<linkedlistsize; l++){

										if (mycache.cachearray[decindexb].framelinkedlist.get(l).tagbits.equals(tagb)){
					
											// if STORE HIT, increment hit by 1 
											hit = hit + 1; 
		
										// change dirtybit to 1
										mycache.cachearray[decindexb].framelinkedlist.get(l).dirtybit = 1;
									
									int count = 0;
									
									// WRITE TO CACHE
									
									// convert offsetb from binary to decimal for indexing purposes
									Integer decoffsetb = Integer.parseInt(offsetb,2);
								
									// write to cache's block data, starting from offset bits for length
									// offset size + access byte size

									for (int c = decoffsetb; c< decoffsetb+numberofbytes; c++){

										mycache.cachearray[decindexb].framelinkedlist.get(l).blockdata[c] = valuetowritearray[count+1]+valuetowritearray[count+2];
	
										count = count+2;
									}
									
									// update linked list so MRU is at front and LRU is at end 
									// store MRU in frame recent 
									frame recent = mycache.cachearray[Integer.valueOf(indexb)].framelinkedlist.get(l);
									// first remove the recent frame from where it was
									mycache.cachearray[Integer.valueOf(indexb)].framelinkedlist.remove(l);
									// then add the MRU to the front of the list 
									mycache.cachearray[decindexb].framelinkedlist.addFirst(recent);
									// do not need to check if set is full since I am not adding a new frame to the set
								}
								
							  }
							
							}
							
							// if hit, print outside of for loop 
							if (hit>0){
								System.out.print("store ");
								System.out.print(parsed[1]);
								System.out.print(" hit ");
							}
							
							// if STORE AND MISS 
							if (hit==0){
						
								// create a new frame for the missed read using the frame constructor 
								// within the frame class 
								frame newframe = new frame(tagb,valuetowritearray,1);

								// only declare a new linkedlist if I need to;
								// otherwise, I just use the same linkedlist and
								// evict the old one
								if (mycache.cachearray[decindexb] == null){

								mycache.cachearray[decindexb] =  new cacheset();
							}

// if the size of the linked list is equal to associativity, I need to evict 
								if (mycache.cachearray[decindexb].framelinkedlist.size() == assocs){
									
									// store LRU in variable LRU of type frame 
									frame LRU = mycache.cachearray[decindexb].framelinkedlist.getLast();
									// if LRU is dirty, update main memory before evicitng LRU 
									if (LRU.dirtybit==1){     
										// concatenate LUR's tagbits and index bits to form the new address
										String newaddress = LRU.tagbits+indexb;

										// convert the new address to decimal for indexing purposes 
										// note: DO NOT chop off first two bits; this is in binary, not hex
										Integer newaddre = Integer.parseInt(newaddress,2);
										
										// update MAIN MEMORY of LRU's block data (the entire block)										
										for (int d = 0; d<blocksize; d++){

											mainmemory[newaddre] = LRU.blockdata[d];	
										// increment the index of mainmemory during each iteration 
											newaddre++;
											
										}
										
										// evict LRU 
										mycache.cachearray[decindexb].framelinkedlist.removeLast();

									}
									// if not dirty, then just evict LRU from linked list  
									// without updating main memory
									else{
										// otherwise, just evict LRU 
										mycache.cachearray[decindexb].framelinkedlist.removeLast();
									}
								}

								// add the new frame (MRU) to the front of the linked list
								mycache.cachearray[decindexb].framelinkedlist.addFirst(newframe);
								// set the frame's dirty bit to 1
								mycache.cachearray[decindexb].framelinkedlist.getFirst().dirtybit = 1;
								// print results 
								System.out.print("store ");
								System.out.print(parsed[1]);
								System.out.println(" miss");
							}	
						}
				}

				// if store + write through; please see comments for store+write back
						// if hit: write value to cache 
						// then write value to memory 
						// update MRU
						// then print
				if (loadorstore.equals("store")){

					if (writewhat.equals("wt")){

						int hit = 0;
						
						valuetowrite = parsed[3];
												
						String[] valuewritearray = valuetowrite.split("");
						
						String[] valuetowritearray = new String[blocksize];
						
						// intialize everything to 00 firts
						for (int e=0;e<blocksize;e++){

							valuetowritearray[e] = "00";
						}

						int value = 0;

						Integer blockoffsetdec;

						blockoffsetdec = Integer.parseInt(offsetb,2);

					for (int g =blockoffsetdec;g<blockoffsetdec+valuetowrite.length()/2;g++){

						valuetowritearray[g] = valuewritearray[value+1]+valuewritearray[value+2];

						value = value +2 ; 
		
					}

						// check if hits/in cache
							// convert indexb, from binary to decimal 
							int decindexb = Integer.parseInt(indexb,2);
							
							// if this is null, i.e., the first time it is read, it's a
							// store miss 
							if (mycache.cachearray[decindexb] == null){
								// it's a miss
								hit = 0;	
							}

							// else if the size of the linked list is 0, it's also a store miss
							else if (mycache.cachearray[decindexb].framelinkedlist.size()==0){
								// it's a miss
								hit = 0;
							}
							    // otherwise, check if there is a frame whose tag bits match the tag bits given
								else if (mycache.cachearray[decindexb].framelinkedlist.size()!=0){
								
									int linkedlistsize = mycache.cachearray[decindexb].framelinkedlist.size();
									
									for (int l = 0; l<linkedlistsize; l++){
					
								// if hit/found the address 
										if (mycache.cachearray[decindexb].framelinkedlist.get(l).tagbits.equals(tagb)){
											// if STORE HIT 
											hit = hit + 1; 
										// change dirtybit to 1
										mycache.cachearray[decindexb].framelinkedlist.get(l).dirtybit = 1;
									
									int count = 0;
									
									// WRITE TO CACHE
									// convert offsetb from binary to decimal
									Integer decoffsetb = Integer.parseInt(offsetb,2);
						
									for (int c = decoffsetb; c< decoffsetb+numberofbytes; c++){
										// two hex numbers per byte 
										mycache.cachearray[decindexb].framelinkedlist.get(l).blockdata[c] = valuetowritearray[count+1]+valuetowritearray[count+2];

										count = count+2;
										
									}

									// ALSO WRITE TO MAIN MEMORY 

								String newaddress = tagb+indexb;
								
								Integer newaddre = Integer.parseInt(newaddress,2);
								// update main memory of LRU's block data (the entire block)		
								for (int d = 0; d<blocksize; d++){
									
									mainmemory[newaddre] = valuetowritearray[d];
									newaddre++;	
								}
									// update linked list so MRU is at front and LRU is at end 
									// store MRU in frame recent 
									frame recent = mycache.cachearray[Integer.valueOf(indexb)].framelinkedlist.get(l);
									// first remove the recent frame from where it was
									mycache.cachearray[Integer.valueOf(indexb)].framelinkedlist.remove(l);
									// then add the MRU to the front of the list 
									mycache.cachearray[decindexb].framelinkedlist.addFirst(recent);
									// do not need to check if set is full since I am not adding a new frame to the set
					
								}
							}
							
						}
							
							// if hit, print outside of for loop 
							if (hit>0){
								
								System.out.print("store ");
								System.out.print(parsed[1]);
								System.out.print(" hit ");
								
							}
						// if store miss, write to main memory 
						// if miss/not in cache 
						// DO NOT bring block to cache
						// just write to main memory
						// then print 
							if (hit == 0){

								String newaddress = tagb+indexb;
								
								Integer newaddre = Integer.parseInt(newaddress,2);
								// update main memory of LRU's block data (the entire block)					
								for (int d = 0; d<blocksize; d++){
									
									mainmemory[newaddre] = valuetowritearray[d];
									newaddre++;

								}
						// print results						
						System.out.print("store ");
						System.out.print(parsed[1]);
						System.out.println(" miss");

					}

				}

			}
				//if load 
				if (loadorstore.equals("load")){
					
					int decindexb = Integer.parseInt(indexb,2); 

					int hit = 0;
					
					if (mycache.cachearray[decindexb]==null){
						
						hit = 0;
					}

					// int framelinkedlistsize = mycache.cachearray[decindexb].framelinkedlist.size();

					else if (mycache.cachearray[decindexb].framelinkedlist.size() == 0){

						hit = 0;
					}
										
					else{
						
					
					// if hit in cache 
					for (int l = 0; l< mycache.cachearray[decindexb].framelinkedlist.size(); l++){
//						System.out.print(l);

						
						// if hit/found the address 
						// need to convert indexb to decimal 

						// if cache is null, then it has not been updated yet 

						
							if (mycache.cachearray[decindexb].framelinkedlist.get(l).tagbits.equals(tagb)){
							
							
							hit = hit + 1; 
							
							// change dirtybit to 1
							
							mycache.cachearray[decindexb].framelinkedlist.get(l).dirtybit = 1;
							
							// update linked list so MRU is at front and LRU is at end 
							// store MRU in frame recent and remove it from the list 
							frame recent = mycache.cachearray[decindexb].framelinkedlist.get(l);
							
							mycache.cachearray[decindexb].framelinkedlist.remove(l);
							// add the MRU to the front of the list 
							mycache.cachearray[decindexb].framelinkedlist.addFirst(recent);
							// do not need to check if set is full since I am not adding a new frame to the set
						
					}
						
					}
					
					}					
					
					// if load hit, read from cache to print 
					if (hit>0){				
						
						// print out these values 
						System.out.print("load ");
						System.out.print(parsed[1]);
						System.out.print(" hit ");
						String loadhitvalue = "";
						// print from cache 
						int blockoffsetdec = Integer.parseInt(offsetb,2);
// start from the offset bits and the total length of the read should b the number of access bytes 
						for (int g=blockoffsetdec;g<numberofbytes+blockoffsetdec;g++){

							loadhitvalue =  loadhitvalue+ mycache.cachearray[decindexb].framelinkedlist.getFirst().blockdata[g];

						}
						
						System.out.println(loadhitvalue);
						
					}
					
					// if load miss 
					if (hit==0){
						
						// get the indexes to read from memory 
						int startindex = Integer.parseInt(address,2) - Integer.parseInt(offsetb,2);
						int endindex = startindex + blocksize;
						// intialitze a string array to be the size of endindex-startindex
						String[] concantenated = new String[endindex-startindex];
						// READ FROM MEMORY
						// concantenated is the string array that contains elements in mainmemory only 
						// corresponding to indices startindex to endindex 
						concantenated = concatenatemain(mainmemory,startindex,endindex);

						// create a new frame for the missed read 
						frame newframe = new frame(tagb,concantenated,1);
							// only declare a new linkedlist if need to 
								if (mycache.cachearray[decindexb] == null){

								mycache.cachearray[decindexb] =  new cacheset();
							}

						// WRITE TO CACHE 

						// if linked list's size is equal to associativity, need to evict
						if (mycache.cachearray[decindexb].framelinkedlist.size() == assocs){

							frame LRU = mycache.cachearray[decindexb].framelinkedlist.getLast();
							
							// if LRU is dirty, update main memory before evicitng LRU 
							if (LRU.dirtybit==1){     
								// update main memory 
								// concantenate strings 				
								String newaddress = LRU.tagbits+indexb;
								// convert newaddress to decimal for indexing purposes 
								Integer newaddre = Integer.parseInt(newaddress,2);
								// update main memory of LRU's block data (the entire block)
			
								// WRITE LRU TO MEMORY 
								for (int d = 0; d<blocksize; d++){
									mainmemory[newaddre] = LRU.blockdata[d];
									newaddre++;
								}
								// evict LRU 
								mycache.cachearray[decindexb].framelinkedlist.removeLast();
							}
							
							// if not dirty, then just evict LRU from linked list  
							// without updating main memory
							else{
								// just evict LRU 
								mycache.cachearray[decindexb].framelinkedlist.removeLast();

							}
							
						}

						// add the new frame to front of the linked list as MRU 
						mycache.cachearray[decindexb].framelinkedlist.addFirst(newframe);
						// set its dirty bit to 1
						mycache.cachearray[decindexb].framelinkedlist.getFirst().dirtybit = 1;

						// print result 
						String loadmissvalue = "";
						System.out.print("load ");
						System.out.print(parsed[1]);
						System.out.print(" miss ");
						
						int blockoffsetdec = Integer.parseInt(offsetb,2);

						// load from MEMORY
						String memoryindex = "";
						memoryindex = tagb+indexb;
						// print out from memory 
						Integer memorydec = Integer.parseInt(memoryindex,2);

						    for (int g=memorydec+blockoffsetdec;g<numberofbytes+blockoffsetdec+memorydec;g++){
							
							loadmissvalue =  loadmissvalue+ mainmemory[g];
						}
				
						System.out.println(loadmissvalue);
				
					}
					
				}
			}
			// close source 
			source.close();
			}
			// catch if there's an exception
		    catch (FileNotFoundException exception){
		    	exception.printStackTrace();
		    }
		}
			
	}

	

	
	



