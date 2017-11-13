
.globl main

.data 

	give_name_input:
			.asciiz "Please Enter a Name:"
	give_jersey_input:
			.asciiz "Please Enter a Jersey Number:"
	give_gradyear_input:
			.asciiz "Please Enter a Graduation Year:"

	done:
			.asciiz "DONE\n"

	nln:    .asciiz "\n"

	space:  .asciiz " "

.text

main:

	# keep a count only for the purpose of sorting
	# while still dynamically allocating memory
	li			$t8,0

	# create a struct 
	li 			$v0,9 	#allocate dynamic memory
	li 			$a0,116 	#116 bytes 
	syscall

	# let $t5 be the iter 
	move 		$t5,$v0

	# save address of this node in this node
	sw          $v0,112($t5)

	# let $s6 be the head
	move        $s6,$t5


loop: 

    
	# prompt the user to enter a string (name)
	li 			$v0,4
	la 			$a0,give_name_input
	syscall
	
	#obtain the user's input name
	li 			$v0,8
	# load the address of the name into 0($t5)
	la 			$a0,0($t5)
	li          $a1,100
	syscall

   # keep a count of how many letters of "DONE" the string has 
   # hit so far 
    li			$t2    0

    # load address of done ("DONE\n") to $a1
    la      	$a1,done

 #stop if the string read hits D,O,N,E
stringcompare:

    # if count = 5, I have hit DONE, go to sort the inputs 
	beq			$t2,5,sort

    # load a byte from "DONE"
    lb			$t0($a1)
    # load a byte from the name in interest
    lb 			$t1($a0) # $a0 is the address of the input string 

    # if the two letteres are the same, go to increment
    beq			$t0,$t1,increment
    # if the two letters are different, then I haven't hit done yet, just go to
    # continuemain to continue collect the other two pieces of info
    bne     	$t0,$t1,continuemain


continuemain:   
 
 	# display message to get jersey number 
	li 		$v0,4
	la 		$a0,give_jersey_input
	syscall
	
	#obtain the user's input jersey number 
	li 		$v0,5
	syscall

	# save the address of the jersey number in the struct 
	sw		$v0,100($t5)

	# prompt the user to enter the graduation year 
	li 		$v0,4
	la 		$a0,give_gradyear_input
	syscall
	
	#obtain the user's input of graduation year
	li 		$v0,5
	syscall

	#save the address of graduation year in the struct
	sw		$v0,104($t5)

	# create a new struct #malloc()
	li 			$v0,9 	#allocate dynamic memory
	li 			$a0,116 #116 bytes 
	syscall

	# save the address of the next node in this 
	# current node so I can do iter->next
	sw			$v0,108($t5)

	# move to the next node, iter = iter->next
	move 		$t5,$v0

	# save address of this node in this node so I can come back to iter after 
	# I move to iter->next when swapping information later for sorting 
	sw          $v0,112($t5)

	# increment the count by 1
	addi		$t8,$t8,1
    
    # go back to loop
	j loop 


increment: 

	#increment the count for how many letters of "DONE" I have hit by 1
	addi 	$t2,$t2,1

	# point $a0 to the next letter
    addi	$a0,$a0,1
    # point $a1 to the next letter 
    addi	$a1,$a1,1

    # go back to stringcompare 
	j stringcompare


# This is the sorting function using bubblesort 
sort:

	# if I only have 1 input, then just go for printing directly since there's no 
	# need to sort with 1 input 
	beq         $t8,1,printresults

	# outer loop for bubblesort: set $t7 to be 0: 
	# for (c=0; c< sizeofarray-1; c++){
	li 			$t7,0

	# subtract 1 from $t8 because the loop needs to
	# stop when $t7 = $t8-1
	addi		$t8,$t8,-1

#enter the first loop
gradsortloop:

		# set iter ($t5) to be head ($t6) every time I enter the outer loop because
		# the last few elements have been already sorted by the way bubbelsort 
		# works and how unsorted items "bubble" to the top 
		move	$t5,$s6

		# if I have reached the end of my outer loop, go to preprintresults which
		# just adds 1 to $t8 (since it was subtracted before for the purpose of
		# this loop) to print 
		beq  	$t7,$t8,preprintresults

		# $t0: $t8 - $t7 - 1
		sub    $t0,$t8,$t7

		# increment $t7 by 1 
		addi    $t7,$t7,1

		# second (nested) loop: set $t9 to be 0: for (d=0; d<sizeofarray-c-1; d++){
		li 			$t9,0

gradsortlooptwo:

		# if $t9 = $t8 - $t7 -1, go to the first loop because I am done with the 
		# inner loop for this $t7 value 
		beq     $t9,$t0,gradsortloop

		# $s7 is iter->jerseynum
		lw      $s7,100($t5)

		# $t3 is iter->gradyear 
		lw  	$t3,104($t5)

		# $t6 is iter->next
		lw		$t6,108($t5)

		# get iter's address too so I can come back to iter from iter->next later 
		lw      $s2,112($t5)

		# move iter to iter->next
		move	$t5,$t6

		# $s0 is iter->next->jerseynum 
		lw      $s0,100($t5)

		# $t2 is iter-next->gradyear
		lw  	$t2,104($t5)

		# move iter->next back to iter
		move    $t5,$s2
	
		# set $t1 to 1 if iter->gradyear
		# is greater than iter->next->gradyear
		slt     $t1,$t2,$t3

		# If so, start swapping information because I want the graduation years 
		# to be sorted in ascending order
		beq     $t1,1,swap

		# if iter->gradyear is smaller than or 
		# equal to iter->next->gradyear, go to updatepinter, which then
		# differentiates between whether they are equal or one smaller than the 
		# other 
		bne     $t1,1,updatepinter

# this is where I swap information for sorting purposes
swap: 

		# update iter to be iter->next
		move	$t5,$t6   

		# iter->next->gradyear = iter->gradyear
		# storing iter->gradyear's value in iter->next->gradyear's address
		sw    	$t3,104($t5)

		# iter->next->jerseynum = iter->jerseynum
		# storing iter->jerseynum's value in iter->next->jerserynum's address
		sw      $s7,100($t5)

		# move iter->next back to iter
		move 	$t5,$s2

		# iter->gradyear  = iter->next->gradyear
		sw			$t2,104($t5)

		# iter->jerseynum  = iter->next->jerseynum
		sw          $s0,100($t5)

        # set nln count ($s4) as 0; this is to count the number of times I have
        # reached the end of a name so that I can swap names properly since 
        # I do not know their lengths in advance 
		li          $s4,0

		# load address of iter->name to $a0
		la      $a0,0($t5)

		# move iter to iter->next
		move    $t5,$t6

		# load address of iter->next->name to $s1
		la 		$s1,0($t5)

		# move iter->next back to iter
		move    $t5,$s2

		# set $t4 to 10 so I know when I have reached "\n" at the end of a string
		li      $t4,10
		# set $s5 to 0 so I know when I have reached "0" at the end of a string 
		li      $s5,0

		# keep count of how many times a NULL or 0 has been reached at the end
		# of each of the two names in interest
		li      $k0,0	
		li      $k1,0

# loop where I swap names byte by byte 
swapnameloop:

		# load a byte from iter->name
		lb      $a1,0($a0)

		# if the byte is "0", go to loadzero
		beq     $a1,$s5,loadzero

		# if the byte is "\n", go to incrementnlncount
		beq     $a1,$t4,incrementnlncount


	continueswapnameloop:

		# load a byte from iter->next->name
		lb      $t2,0($s1)

		# if the byte is "0", go to loadzerotwo
		beq     $t2,$s5,loadzerotwo

		# if the byte is "\n", go to incrementnlncount
		beq     $t2,$t4,incrementnlncounttwo


	continueswapnamelooptwo:

		# save the byte from iter->name to iter->next->name
		sb      $a1,0($s1)

		#save the byte from iter->next->name to iter->name
		sb      $t2,0($a0)

		#load the next bytes 
		addi  $a0,$a0,1
		addi  $s1,$s1,1

		# go back to swapnameloop
		j swapnameloop


# increment the count of the number of times a "0" or NULL has been reached at the 
# end of a name
incrementnlncount: 

		# increment the number of time NULL or "0" has been returned by the first 
		# name by 1
		addi  $k0,$k0,1

		# just to be sure, I only want a name to reach NULL or "0" once and I do 
		# not want it to be double counted if it reaches them more than once,
		# so I only go ahead and increment $s4 the first time one of the two 
		# has been reached by a name
		beq   $k0,1,goaddidoublecount

		# if it's not the first time, go back to continueswapnameloop
		j continueswapnameloop

goaddidoublecount:

		# increment $s4 by 1, which is the count of the number of names whose counts
		# I have reached 
        addi  $s4,$s4,1

        # if I have reached the end of both names, continue to sort by going to 
        # continuegradsortlooptwo
        beq   $s4,2,continuegradsortlooptwo

        # if not, go back to continueswapnameloop
        j continueswapnameloop

incrementnlncounttwo:

		# increment the number of time NULL or "0" has been returned by the first 
		# name by 1
		addi  $k1,$k1,1

		# just to be sure, I only want a name to reach NULL or "0" once and I do 
		# not want it to be double counted if it reaches them more than once,
		# so I only go ahead and increment $s4 the first time one of the two 
		# has been reached by a name
		beq   $k1,1,goaddidoublecounttwo

		# if it's not the first time, go back to continueswapnamelooptwo
		j continueswapnamelooptwo

goaddidoublecounttwo:

		# increment $s4 by 1, which is the count of the number of names whose counts
		# I have reached 
		addi  $s4,$s4,1

		# if I have reached the end of both names, continue to sort by going to 
        # continuegradsortlooptwo
		beq   $s4,2,continuegradsortlooptwo

		# if not, go back to continueswapnamelooptwo
        j continueswapnamelooptwo

loadzero:
		
		addi  $k0,$k0,1
		beq   $k0,1,goaddidoublecount
		j continueswapnameloop


loadzerotwo:		

		# increment the number of time NULL or "0" has been returned by the first 
		# name by 1
		addi  $k1,$k1,1

		# just to be sure, I only want a name to reach NULL or "0" once and I do 
		# not want it to be double counted if it reaches them more than once,
		# so I only go ahead and increment $s4 the first time one of the two 
		# has been reached by a name
		beq   $k1,1,goaddidoublecounttwo

		# if not, go back to continueswapnamelooptwo
		j continueswapnamelooptwo


continuegradsortlooptwo:

		# increment the count for the inner loop ($t9) 
		# by 1 after swapping information 
		addi 	$t9,$t9,1

		# update iter = iter->next
		move 	$t5,$t6

		# go to gradsortlooptwo, the inner loop
		j gradsortlooptwo

# check if the two graduation years in interest are equal or the first one less than
# the second one (in which case, no sorting is needed)
updatepinter:

		# check if the two are equal; if so, break the tie by sorting the names
		beq 	$t2,$t3,namesort

		# if the first graduation year is less than the second one, just update
		# the pointer and the loop
		bne     $t2,$t3,justupdate

justupdate: 

		# increment the count for the inner loop ($t9) 
		# by 1
		addi 	$t9,$t9,1

		# update iter = iter->next
		move 	$t5,$t6

		# go to gradsortlooptwo
		j gradsortlooptwo


# break ties for players whose graduation years are equal 
namesort:

		#compare byte by byte the names of the 
		# players whose graduation years are equal

		# load address of iter->name into $a0
		la      $a0,0($t5)

		# move iter to iter->next 
		move    $t5,$t6

		# load address of iter->next->name into $a1
		la      $a1,0($t5)

		# move iter->next back to iter
		move    $t5,$s2

		loopnamesort:

		# load a byte from iter->playername
		lb   	$s7($a0)

		# load a byte from iter->next->playername
		lb 		$s3($a1)

		# if they are the same letter, load the next one 
		beq     $s7,$s3,loadthenext

		# if $s7<$s8, set $t1 to 1; if not,
		# $t1 is 0
		slt     $t1,$s7,$s3

		# if for example, (c>b), then I need to swap the two 
		beq 	$t1,0,swap 

		# increment the count for the inner loop ($t9) 
		# by 1
		addi 	$t9,$t9,1

		# iter = iter->next
		lw		$s1,108($t5)
		move 	$t5,$s1

		# go to gradsortlooptwo
		j gradsortlooptwo

# load the next byte so I can continue to compare the two names 
loadthenext:

		# load the next byte for both strings
		addi $a0,$a0,1
		addi $a1,$a1,1

		# go back to loopnamesort
		j loopnamesort

# just add 1 to $t8 for the purpose of printing since 1 is subtracted for the 
# purpose of looping for bubblesort 
preprintresults:

		addi    $t8,$t8,1
		# go to printresults to print everything 
		j printresults

# print the final sorted results 
printresults:

		# set iter = head
		move    $t5,$s6

	    # set $t6 to be 0, so I know when $t6 = $t8, I end my printing 
		li      $t6,0

print:

		# load address of the name
		la     	$a0,0($t5)

	# loop through the linked list to print 
	loopprint: 


		# load byte of name until I reach "\n" or "0"
		# then I go update the byte as "0"
		# and then I manually add a space for printing formatting purposes  
		li      $t1,10
		li      $t2,0


		# load a byte of the name 
		lb     	$t0,0($a0)


		# change the byte to "0" to indicate the end of the string if I have 
		# reached the end of the string by either "0" ot "\n"
		beq    	$t0,$t1,changebyte
		beq     $t0,$t2,changebyte

		# if not, go to the next byte 
		addi	$a0,$a0,1

		# go to loopprint 
		j loopprint

# change the byte to "0" to indicate the end of the string if I have 
# reached the end of the string by either "0" ot "\n"
changebyte:

		# change the byte to "0" to indicate the end of the string
		sb       $0,0($a0)

		# load address of the name into $s4, print it
		la		$a0,0($t5)
		li 		$v0,4
		syscall

		# print a space 
		la     $a0,space
		li     $v0,4
		syscall

		# print the jerseynumber
		lw		$s1,100($t5)
		move	$a0,$s1
    	li 		$v0,1
    	syscall 

    	# increment $t6 by 1
    	addi    $t6,$t6,1

    	# when $t6 = $t8, end the program as printing is done 
    	beq 	$t6,$t8,endprog

    	# print an empty line as every set of inputs needs to be on different
    	# lines 
        li      $v0, 4         
    	la		$a0,nln
    	syscall

    	# move pointer to the next
    	lw		$s1,108($t5)
    	move	$t5,$s1

    	# go back to print 
    	j print

# end the program 
endprog: 

    	li          $v0,10
    	syscall

