Course: COMPSCI 260
Name: Liane Yanglian
NetID: xy48
Problem: 1
Problem Set: 1
Due: Fri 16 Sep 2016, 5pm
Using free extension (yes/no): yes

Statement of collaboration and resources used (put None if you worked 
entirely without collaboration or resources; otherwise cite carefully):
I got help from the TA Firas, Kyle, and Lydia. Lydia was so nice that I was able to schedule an appointment with her. 
My solutions and comments for this problem are below.
-----------------------------------------------------
a) less than (18677 - 11717) / 3 = 2320. Since there are untranslated introns, the length of the peptide product is less than 2320.
e) This TAA will act as a stop codon if it's in the same reading frame with the start codon.
For b),c),d),f), please see the p53.py. 

How my solution works:

I start by storing the locations of the beginning and end of the coding region in variables named startofcoding and endofcoding. Then, I extract the part of the sequence between the beginning and the end of the coding region and store it in the variable codingplusintrons. After this I construct a new variable named concatenating to concatenate the coding plus intron sequence with the next three nucleotides. I then use a single regular expression to check that my new sequence indeed starts with ATG and ends with a stop codon. In addition, I print out the nucleotides from 17520 to 17522, which happens to be TAA. To check whether the coding plus intron sequence contains a restiction site for PmII, SgrAI and OliI, for each I use a single regular expression to do so and report the actual sequence that is recognized by this enzyme and the position at which it's located.  

Short transcript of program in operation:

With the ssRNA as input, the program's output is:

Yes, the sequence starts with an ATG and ends with a stop codon!
for PMII, CACGTG at 844
for SgrAI, CACCGGCG at 449
for OliI, CACCACTGTG at 1122
The nucleotides from 17520 to 17522 are TAA .

