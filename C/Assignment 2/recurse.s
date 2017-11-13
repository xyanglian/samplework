
.globl main
.data
		give_input:
			.asciiz "Please Enter a Number:"
.text

main:
		# prompt the user to enter a number
		li 		$v0,4
		la 		$a0,give_input
		syscall

		#obtain the user's input number
		li 		$v0,5
		syscall

		# check for base case: if input is 0, just print 5 and end program
		beq		$v0,0,end

		# load the 2 and 3 into $t6 and $t7 
		li      $t6,2
		li      $t7,3

		# store the number in $a0
		move 	$a0,$v0

		# jump to recur 
		jal recur 
		
		# print a the number 
		move    $a0,$v0
		li		$v0,1
		syscall 

		# end the program for all other cases except for the base case
		li 		$v0,10
		syscall


recur:

		# add stack 
		addi 	$sp,$sp,-12
		sw 		$t0,0($sp)
		sw		$t1,4($sp)
		sw		$ra, 8($sp)

		#base case check if $a0= 0
		beq 	$a0,0,basecase

		# get N-1 
		addi	$t1,$a0,-1
		# store N-1 in $a0
		move    $a0, $t1

		# call recur 
		jal recur 
		# $t1 = (N-1)*3
		mul 	$t1,$t1,$t7
		# $t1 = (N-1)*3-1
		addi	$t1,$t1,-1
		# $t1 = 2*f(N-1)
		mul 	$t0,$v0,$t6
		# #t1 = (N-1)*3-1+2*f(N-1)
		add 	$t1,$t1,$t0
		# write to $v0
		move 	$v0,$t1

		j clean

# store 5 in $v0 
basecase:

		li		$v0,5

clean: 	
		#pop stack

		lw		$t1 4($sp)
		lw      $t0,0($sp)
		lw		$ra, 8($sp)
		addi 	$sp,$sp,12

		#return 
		jr		$ra

# end program for base case 	
end:	
		li 		$a0,5
		li 		$v0,1
    	syscall
    	#end program 
    	li 		$v0,10
    	syscall  

 