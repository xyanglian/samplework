Course: COMPSCI 260
Name: Liane Yanglian
NetID:xy48
Problem: 2
Problem Set: 2
Due: Fri 30 Sep 2016, 5pm
Using free extension (yes/no):no

Statement of collaboration and resources used (put None if you worked 
entirely without collaboration or resources; otherwise cite carefully):
I consulted these and borrowed ideas from these resources: TA Lydia Xu, 
https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort and 
http://stackoverflow.com/questions/7801861/why-is-merge-sort-worst-case-run-time-o-n-log-n and https://codehiker.wordpress.com/2012/03/18/inversions/ 
My solutions and comments for this problem are below.
-----------------------------------------------------
a) The running time of this method is O(n^2). This is because what we do is equivalent to looping through the array twice, comparing 
each number in the array with every other element in the array. Since the array is of length n, the running time will be O(n^2).

b) I will describe the algorithm here and please see specific comments of the code in the .py file. A divide-and-conquer algorithm 
that solves the problem in O(nlogn) time can consist of two functions. One function is called divide_and_conquer, which takes the given 
input array as its argument. The other function is called sort, which takes two arguments, each being the subarrays derived from the 
given input array. The divide_and_conquer function divides the array into subarrays until the subarrays are of length 1. To achieve this,
the pseudo code will be:
first reverse the given array and make it into a list 
length = len(array)
if length > 1 : 
	subarrayindex = length/2
	subarray1 = inversions_divide_conquer(first half of array)
	subarray2 = inversions_divide_conquer(second half of array)
	return sort(subarray1,subarray2) (sort being the other function which will be described later)
if length <= 1:
	return array 
	
  The sort function is called by inversions_divide_conquer. It checks if the subarrays of length 1 from the inversions_divide_conquer 
function satisfy what we're looking for, namely, i>j and ai>aj (although the original array has been reversed, so it's i<j, ai>aj 
for the reversed array). If so, then it increments the count. If not, it will eventually append the numbers to a list and return the
list. The pseudo code will be: 

a = 0
b = 0
count = 0
list = []

while a is less than the length of subarrayA and b is less than the length of subarrayB:
	if subarrayA[a] is less than subarrayB[b]:
		list.append(subarrayA[a])
		a += 1
	otherwise:
		list.append(subarrayB[b])
		count = count + len(subarrayA[a]) - a
		
		(note that the count is incremented by len(subarrayA) - a because both subarrayA and subarrayB are sorted, so the numbers in 
		subarray A after subarrayA[a] must also be greater than subarrayB[b] if subarrayA[a] is greater than subarrayB[b])
		
		b+=1
	if a is not equal to the length of subarrayA:
		extend the list to include the elements in subarrayA from index a
	otherwise:
		extend the list to include the elements in subarrayB from index b
	
For example, for an input of [15,8,20,4,7,10,1], the algorithm will return 6 because there are 6 in-order pairs: (15,20),(8,20),(4,7),
(4,10),(7,10),(8,10).

The worst case running time will still be O(nlogn). Suppose we have a list of 10 items split into lists of lists of length 1, it will 
take log(10), log(n), doublings to get a list of 10 numbers long. In the worst case, each number in each sublist will need to be checked once, 
so for all doublings, we need to check 10 numbers, n numbers. Therefore, the running time will be O(nlogn).

c) For the divide_and_conquer algorithm, the running time for sets of random inputs of length n of {10^2,10^3,10^4,10^5,10^6,10^7} are 
respectively 0.000308990478516, 0.00414395332336, 0.0551989078522, 0.672538042068, 7.98036193848, and 100.314037085. My estimate for its 
running time for inputs of length n = 10^8 is 100.314037085*12 = 1203.768445. I ran the algorithm for n = 10^8, and the actual output I
got was quite close to this number: 1178.53446722.
	The running time seems to increase for the divide_and_conquer algorithm by a factor of around 12 to 13 every time the length of 
the random inputs increases by a factor of 10. 

   For the brute_force algorithm, the running time for sets of random inputs of length n of {10^2,10^3,10^4,10^5} are respectively
2533, 252747,25089377, and 2486179734. My estimate for its running times for inputs of length n of {10^6,10^7,10^8} are respectively
2486179734*100 = 248617973400, 24861797340000, and 2486179734000000. 
	The running time seems to increase for the brute_force algorithm by a factor of approximately 100 every time the length of the
random input increases by a factor of 10.

    The running time of the divide_and_conquer algorithm increases by a factor of approximately 12 whereas the running time of the 
brute_force algorithm increases by a factor of 100 every time the length of the random input increases by a factor of 10. As a result, 
when the length of the random input increases by a large factor, for example, from 10^2 to 10^5, there's a large difference between 
the increase in running times of the divide_and_conquer algorithm and the brute_force algorithm. In this example, the divide_and_conquer 
algorithm increased by a factor of 0.672538042068/0.000308990478516 = 2176.565586 which is close to 13^3 = 2197. This is consistent with
the complexity analysis, the running time O(nlogn). On the other hand, the brute_force algorithm increased by a factor of 
2486179734/2533 = 981515.8839. This is close to 100^3 = 1000000. This is also consistent with the complexity analysis, the running time
O(n^2).

    There do exist differences between what I observe and what I might expect from the asymptotic analysis. From the analysis, 
the brute_force algorithm's running time is O(n^2). Therefore, when the length of the input increases by a factor of 10, I expect the 
brute_force algorithm's running time to increase by a factor of ((10^(n+1))^2)/((10^n)^2) = 100. Similarly, the divide_and_conquer
algorithm's running time is O(nlogn), and solving the equation (((10^(n+1))^2)*log(((10^(n+1))^2)))/(((10^n)^2)*log((10^n)^2)) gives a 
result close to 12 or 13. However, doing calculations on the data I obtained from both algorithms for n of {10^2,10^3,10^4,10^5}, I 
noticed that the algorithms don't increase by exactly the factor of 100 or of 12 or 13 when n increases by 10. 

    The differences might have arisen because even though the asymptotic analysis yields a result of O(n^2) and O(nlogn) as the running 
times, the accurate running times might be something of the like of, for example, O(n^2 + 6n + 2) and O(nlogn +1). But when the
asymptotic analysis is done, only the term with the highest power was considered, so when the program actually runs, the running time 
might be different from what one would expect from just looking at the running time analysis. Moreover, each computer's memory and 
processing speed is different, so that might have also factored into why the actual running time is not exactly what one would expect
from the asymptotic analysis.

Short transcript of the program in operation: 

input: array = [15, 8, 20, 4, 9,3,24]
output: From the brute force approach, the number of in-order pairs is 10
From the divide and conquer approach, the number of in-order pairs is 10





	
	