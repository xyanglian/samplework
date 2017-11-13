
.globl main

.data
		give_input:
			.asciiz "Please Enter a Number:"

		msg:    .asciiz " "
		mag:    .asciiz "2"
		nln:    .asciiz "\n"

.text

main:
		# prompt the user to enter a number
		li 		$v0,4
		la 		$a0,give_input
		syscall

		#obtain the user's input number
		li 		$v0,5
		syscall

		# store the number in $t0
		move 	$t0,$v0


		la 		$t1,msg    # setting up 
		la 		$t2,mag
		li 		$t3,1
		li		$t4,1

# set up the base cases for when the input is 0,1,or2
again:   				
    	beq 	$v0,0,target
    	beq 	$v0,1,taget
    	beq 	$v0,2,targt
    	bne     $v0,0,check  

# if the input is 0, print nothing 
target: 

		move 	$a0,$t1
		li 		$v0,4
    	syscall

    	#end program 
    	li 		$v0,10
    	syscall   

# if the input is 1, print "2"
taget:  
		move 	$a0,$t2
		li 		$v0,4
    	syscall

    	#end program 
    	li 		$v0,10
    	syscall   

# if the input is 2, print "2\n2"
targt:  

		# print first 2
		move	$a0,$t2
		li 		$v0,4
    	syscall

    	# print the empty line break in between
        li      $v0, 4          
    	la		$a0,nln
    	syscall

    	# print second 2
    	move	$a0,$t2
    	li 		$v0,4
    	syscall 

    	#end program 
    	li 		$v0,10
    	syscall   

# if the number is not 1, go to checktwo
check:
		bne     $v0,1,checktwo

# if the number is not 2, go to checkthree
checktwo:
		bne     $v0,2,checkthree

# for all other cases, use checkthree
checkthree: 

		# print first 2
		move	$a0,$t2
		li 		$v0,4
    	syscall

    	# print the empty line break in between
    	la		$a0,nln
    	syscall

    	# print second 2
    	move	$a0,$t2
    	li 		$v0,4
    	syscall 

    	# print another empty line break in between
        li      $v0, 4         
    	la		$a0,nln
    	syscall

        # set i=2,and increment till it hits $t0, which is the input number 
    	li 		$t5,2

    	# loop to get the fibionacci numbers
    	loop:

    	# move the registers
    	move	$t6,$t3
    	move	$t3,$t4

        # add the previous two numbers together to obtain the next number 
    	addu  	$t4,$t6,$t3

    	#multiply the value in $t6 by 2
    	addu 	$t7,$t4,$t4

    	#print out the current value
    	li 		$v0,1
    	move 	$a0,$t7
    	syscall	
    	
    	# increment $t5 by 1
    	addi 	$t5,$t5,1

    	#check if the loop has ended; if so, end program
		beq  	$t5,$t0,end

		#if not, print an empty line
        li      $v0, 4        
		la		$a0,nln
    	syscall

    	# go through the loop again
    	j loop 

        #end program 
    	end: 		
    	li 		$v0,10
    	syscall            
