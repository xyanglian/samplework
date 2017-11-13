Course: COMPSCI 260
Name: Liane Yanglian
NetID:xy48
Problem: 1
Problem Set: 2
Due: Fri 30 Sep 2016, 5pm
Using free extension (yes/no): no

Statement of collaboration and resources used (put None if you worked 
entirely without collaboration or resources; otherwise cite carefully):
I consulted these and borrowed ideas from these resources:TA Lydia Xu 
My solutions and comments for this problem are below.
-----------------------------------------------------
a) The expected number of occurrences for a read of length m in a genome of size n is (n-m+1)/(4^m) because there are 4^m possible 
sequences of the length m of the bases A,T,G,C, and the total number of times you can get a read of length m in a sequence of length n
is n-m+1. This is because for any read of length m and genome of length n, the number of reads of that length from the genome is n-m+1. 
We can test this with example cases. Suppose n = 100 and m = 2, then that number would be 100-2+1 = 99. (However, if the question is 
asking for a more general solution where n is so large that we can overlook m, then the answer would be n/(4^m).)

b) The brute force algorithm for mapping a read to a reference genome is to create an empty list, loop through the genome one nucleotide 
at a time, and check if the nucleotide matches the first nucleotide of the read given. If so, check if there exist m nucleotides 
in the genome starting from that nucleotide and that those m nucleotides match the entire read. If so, append the index of the first 
matching nucleotide in the genome, and return the list as the output. 

   The pseudo code is as follows:
   
   create an empty list named list
   for every nucleotide in the genome:
   			if the nucleotide in the genome matches the first nucleotide in the read and has at least m-1 nucleotides after it in the 
   			genome:
   				if the m nucleotides starting from that matching nucleotide in the genome match the m nucleotides in the read:
   					append the index of the first matching nucleotide in the genome to list
   	return list 
   	
    For example, if the genome is (A,T,G,T,C,C,T,A,T,G,A,C) and the read is (A,T,G), the program will return (0,7) because those are the 
two indexes of the two matching A's in the genome. For the A in the index 10 in the genome, the program will not return an error and will
still run properly because the algorithm checks against cases where the first nucleotide matches but there aren't m nucleotides left in 
the genome.
   			
   The worst case running time is O(mn) because the the worst case occurs when the algorithm needs to loop through every nucleotide in
the genome of length n to find if any matches with the first nucleotide of the read of length m and if there exist m-1 nucleotide after
that matching nucleotide in the genome. If so,it then has to go through the m nucleotides of the read to determine whether those 
nucleotides match the m nucleotides of the genome starting from the matching nucleotide.

c) It will have been worth it if k is less than (nlogn)/(mn-mlogn). This is because in order for it to be worth it to use the 
pre-processing rather than the brute force algorithm, the running time of the pre-processing algorithm needs to be less than that of 
the brute force one. We already calculated the running time of the brute force algorithm, and are told that for the pre-processing
algorithm it takes O(nlogn) time to build the data structure and O(mlogn) time to query the genome for a specific sequence. Since the 
the number of reads is k, we then compare the runnning  times of the two algorithms: k*mlogn + nlogn < k*(mn) because we multiply the 
number of reads with the running time to run the algorithm itself, but we don't need to do that with nlogn in the pre-processing method
because the algorithm only needs to build the data structure once. Solving the equation then gives us k < (nlogn)/(mn-mlogn). 
  Ultimately, the trades-offs between the brute force approach and the pre-processing approach are that the brute force approach has less
efficiency and needs more time and space as it runs, but is of less complexity whereas the pre-processing approach is of more 
complexity, but has more efficiency and needs less time and space as it runs. 


