Course: COMPSCI 260
Name: Liane Yanglian
NetID: xy48
Problem: 4
Problem Set: 2
Due: Fri 30 Sep 2016, 5pm
Using free extension (yes/no):no

Statement of collaboration and resources used (put None if you worked 
entirely without collaboration or resources; otherwise cite carefully):
I consulted these and borrowed ideas from these resources: TA Kyle Moran
My solutions and comments for this problem are below.
-----------------------------------------------------
In order to minimize the number of restriction sites used to generate manageable reads which span the length of the genome, I have the 
following algorithm, with the following pseudo code. I assume that the input is an array (referred to as "array" in the pseduo code) of 
the distances between the consecutive restriction enzymes. n is the number of bases to which I'm able to reliably sequence reads. The
algorithm returns the list of the restriction sites that are used by referring to their indices in the original input, array, and also
prints that list and the number of restriction sites used:

def find_min_restriction_sites(array):
    count = 0 
    restrictionsitesused = []
    
    for i in range (0,len(array))
        if count + array[i] <= n
           count += array[i]
        if count + array[i] > n
           restrictionssitesused.append(i-1)
           count = array[i]
           
    print 'Minimum number of restriction sites used is,'len(restrictionssitesused)
    print 'The restriction sites used by their indices are:',restrictionsitesused
    return restrictionsitesused
 
 This algorithm is correct because the for loop loops through every restriction site, and then add the length of the retriction site to 
 the count to check if the count is less than or equal to n. When the count is greater than n, the index of the previous restriction site
 is appended to the list restrictionsitesused, which store all the indices of the restriction sites used. Also, count will be updated to
 the distance between the current restriction site and the previous one, so as to start the search again and repeat the aforementioned
 procedure. In the end, the minimum number of restriction sites used is the length of the list restrictionsitesused, and we can know 
 which restriction sites have been used by referring to the list itself, which records the restriction sites used by their indices in the
 original input, array. 
 
 The running time of the algorithm is O(a), given that the length of the input array, i.e.the number of restriction sites, is a. This is
 because there is one for loop looping through every element in the restriction sites, making the running time O(a).
 
 I can prove my strategy yields an optimal solution by proof by contradiction. First, let's assume that my algorithm does not yield an 
 optimal solution. Then there must exist other algorithms which give a shorter running time. Since the running time for my algorithm is
 O(a), then the running times of those more efficient algorithms can be O(loga) or O(1). However, when the running times are O(loga) or 
 O(1), it isn't possible to have looped through every restriction site; in that case, it isn't possible to come up with the minimum 
 number of restriction sites because it's necessary to loop through every restriction site in order to know using which restriction sites
 can enable the minimum number of restriction sites. Therefore, there's a contradiction, which means the assumption that my 
 algorithm does not yield an optimal solution is wrong. Thus, my strategy does yield an optimal solution. 
