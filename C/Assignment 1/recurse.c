#include <stdio.h>

int recur(int number){

	// base case 
	if (number==0){

		return 5;
	}

    // use the formula provided here, and call t
    // the function itself recursively 
	else{

		return 3*(number-1)+2*recur(number-1)-1;
	}

}

int main(int argc, char *argv[] ) {


 	int N;

    sscanf (argv[1], "%d",&N);

   // base case 
	if ( N == 0) {
		printf ("%d",5);
		return 0 ;
	} 

	// call the recur function in the main function 
	// so recursive calls are made 
	else {

		printf ("%d",recur(N));
		return 0;

    }

	}



