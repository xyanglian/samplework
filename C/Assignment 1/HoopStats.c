
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// construct a struct to store information in
struct players {

	char playername[100];
	int jerseynum;
	int gradyear;
	// carete a pointer to point to the struct itself
	struct players* next;

};

// a pointer variable that points at the head of the 
//linked list 
struct players *head ; 
// a pointer that iterates through the linked list
struct players *iter;
// a pointer that later acts to free the 
//dynamically allcoated memory
struct players *dlete;

// build a sort function that the main function calls
void sort(struct players *lst, int sizeofarray){

	int c;
	int d;

	// bubblesort
	for (c=0; c< sizeofarray-1; c++){
		// update lst to be the head of the linked list
		lst = head;

		for (d=0; d<sizeofarray-c-1; d++){

			// compare the graduation years and sort 
			// accordingly 
			if (lst->gradyear > lst->next->gradyear){

				// swap the values for the graduation 
				//years
				int a = lst->gradyear;
				lst->gradyear = lst->next->gradyear;
				lst->next->gradyear = a;

				// swap the values for the jersey 
				//numbers
				int b = lst->jerseynum;
				lst->jerseynum = lst->next->jerseynum;
				lst->next->jerseynum = b; 

				// swap the players' names 
				char tepo[100];

				memcpy(tepo,lst->playername,sizeof(tepo));

				memcpy(lst->playername,lst->next->playername,sizeof(lst->playername));

				memcpy(lst->next->playername,tepo,sizeof(lst->next->playername));

				// update lst to be the next lst
				lst = lst->next;

			}

			else if (lst->gradyear < lst->next->gradyear){

				// update lst to be the next lst anyway
				lst = lst->next;

			}


			// in the event of equal graduation years.
			// break the tie by comparing players' names
			else if (lst->gradyear == lst->next->gradyear){

				// compare players' names 
				if (strcmp(lst->playername,lst->next->playername)>0){

					int a = lst->gradyear;
					lst->gradyear = lst->next->gradyear;
					lst->next->gradyear = a;

					int b = lst->jerseynum;
					lst->jerseynum = lst->next->jerseynum;
					lst->next->jerseynum = b; 

					char tempo[100];

					memcpy(tempo,lst->playername,sizeof(tempo));

					memcpy(lst->playername,lst->next->playername,sizeof(lst->playername));

					memcpy(lst->next->playername,tempo,sizeof(lst->next->playername));

					// update lst 
					lst = lst->next;

				}

				else if (strcmp(lst->playername,lst->next->playername)<0){

					// update lst anyway
					lst = lst->next;
				}

			}
		}
	}
}

int main(int argc, char *argv[] ) {

	// malloc the head to dynamically allocate memory 
	head = (struct players*) malloc(sizeof(struct players));

	// set head->next to NULL so that the program
	// later knows when it has reached the end of
	// the linked list
	head->next = NULL;
	// set iter to be head so I can iterate through 
	// the list later 
	iter = head;

	// read the file line by line
	FILE *playersinfo = fopen(argv[1],"r");

	// set a count so I know the number of players 
	// in order to perform bubblesort 
    int count = 0;

    // fscanf the first line of the file so 
    // I can start checking whether it is
    // DONE in the while loop 
    fscanf (playersinfo, "%s", &iter->playername);

// check if the current line of the file is DONE

	while (strcmp(iter->playername, "DONE") != 0){

		// fscanf to store jersey numbers and 
		// graduation years too 
		fscanf (playersinfo, "%d", &iter->jerseynum);

		fscanf (playersinfo, "%d", &iter->gradyear);

		// malloc iter and update it every iteration 
		iter->next = (struct players*) malloc(sizeof(struct players));

		iter = iter->next;

		// now fscanf the next playername in order to 
		// check if I have reached DONE
		fscanf (playersinfo, "%s", &iter->playername);

		// set iter->next to be NULL so later I know 
		//when I have reached the end of the list 
		iter->next = NULL;
		// increment count so I know the number of 
		// players for bubble sort later 
		count += 1; 

		}

	// set iter to be head so I can iterate over the
	// linked list
	iter = head;

	// call the sort function
	sort (iter,count);

	int i;

	// iterate over linked list

	while (iter->next != NULL){

		// print the information as required 
		printf("%s %d\n", iter->playername,iter->jerseynum);
		// set dlete to be iter
		dlete = iter;
		// update iter to be iter->next
		iter = iter->next;
		// free dynamically allocated memory
		free(dlete);
	}

	// free the last dynmically allocated memory where
	// "DONE" is stored from the earlier while loop
	free (iter);

	// close the file 
	fclose(playersinfo);
	return 0;
}


