#include <stdio.h>


int main(int argc, char *argv[] ) {

 	int N;

    sscanf (argv[1], "%d",&N);

    // base cases
    if (N==0){

    	printf(" ");
    	return 0;
    }

	if ( N == 1 ) {
		printf ("2");
		return 0;
	} 

	if ( N == 2 ) {
		printf ("2\n2");
		return 0;
	}

	else {

		int newlist [N];
		
		// base cases
		newlist[0] = 1;
		newlist[1] = 1;

		int a;
		int b;

		// calculate the fibonacci numbers
		for (a = 2; a<N; a ++) {

			newlist [a] = newlist [a-1] + newlist [a-2];

		}

		// double the value of all numbers
    	for (b=0; b<N; b ++) {

    		newlist[b] = newlist [b] + newlist[b];
    		printf("%d\n", newlist[b]);

    	}
    	return 0;
}

}



