'''
@author: Liane Yanglian
@date: September 22, 2016

@note:

'''

from compsci260lib import *
from random import shuffle
import random
import timeit

def inversions_brute_force(array):
    # taking the first number and comparing it with the remaining n-1 numbers, then taking the second number and comparing it
    # with the remaining n-2 numbers, and so on
    i = 0
    count=0
    # checking against the case in which the first number is the smallest number in the array
    if array[i] == min(array) and i == 0:
        i += 1
    # looping through every number in the array
    while i < len(array)-1 :
        # if the next number is less than this one, then incrementing the count by 1 
        for number in array[i+1:]:
            if number < array[i]: 
                count += 1
        # incrementing i to go to the next number in the array
        i += 1
    print 'From the brute force approach, the number of in-order pairs is',count
    
def sort(subarrayA, subarrayB):
    # using merge sort to solve the problem in O(nlogn) time; this will be called by inversions_divide_conquer 
    global count
    a = 0 
    b = 0 
    list = []
    # for all numbers in subarray A and subarray B 
    while a<len(subarrayA) and b<len(subarrayB):
        # if the number of the first array is less than that of the second (since we have reversed the input array)
        if subarrayA[a] <= subarrayB[b]:
            # if the number is not what we're looking for, then append it to the list and increment a by 1 
            list.append(subarrayA[a])
            a+=1
        # appending the number that we're looking for to list and incrementing the count of b by 1
        else:
            list.append(subarrayB[b])
            # incrementing the count by len(subarrayA) - a because both subarrayA and subarrayB are sorted, so the numbers
            # in subarray A after subarrayA[a] must also be greater than subarrayB[b] if subarrayA[a] is greater than 
            #subarrayB[b]
            count = count + len(subarrayA) - a
            b+=1
    
    # checking if a has been incremented to equal the length of subarrayA;if not, the list is extended to include what's in A
    if a != len(subarrayA):
        list.extend(subarrayA[a:])
    # if a has been incremented to equal the length of subarrayA, then the list is extended to include what's in subarrayB
    if a == len(subarrayA):
        list.extend(subarrayB[b:])
    
    #returning the lists that have been checked for their numbers 
    return list 

def inversions_divide_conquer(array):
    # diving problems into subproblems the mergesort way
    
    length = len(array)
    # as long as the length of the subarrays are greater than 1
    if length > 1 :
        # halfing the index so as to divide the list into sublists of half of the length of the original list
        subarrayindex = length/2
        # creating subarrays of half of the length of the original list and running inversions_divide_conquer on elements 
        # of subarrays until the subarrays are of length 1, with subarray 1 slicing for the first half and subarray 2 slicing
        # for the second half of the array
        subarray1 = inversions_divide_conquer(array[:subarrayindex])
        subarray2 = inversions_divide_conquer(array[subarrayindex:])
        return sort(subarray1,subarray2)
    # when the array is of length 1, we reached our goal of dividing and return the array
    if length <= 1:
        return array


if __name__ == '__main__':


    array = [15, 8, 20, 4, 9,3,24]
    #reversing the array and making it into a list
    inversions_brute_force(list(reversed(array)))
    # initializing count to 0 
    count = 0 
    #reversing the array and making it into a list
    inversions_divide_conquer(list(reversed(array)))
    print 'From the divide and conquer approach, the number of in-order pairs is',count
    randomlist = random.sample(range(0,10**8),10**8)
    print 'divideandconquer',timeit.timeit('inversions_divide_conquer(randomlist)', setup='from __main__ import inversions_divide_conquer, randomlist', number=1)
    print 'bruteforce',timeit.timeit('inversions_brute_force(randomlist)', setup='from __main__ import inversions_brute_force, randomlist', number=1)


