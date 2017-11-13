#include <stdio.h>  // needed for size_t
#include <unistd.h> // needed for sbrk
#include <assert.h> // needed for asserts
#include "dmm.h"

/* You can improve the below metadata structure using the concepts from Bryant
 * and OHallaron book (chapter 9).
 */

typedef struct metadata {
  /* size_t is the return type of the sizeof operator. Since the size of an
   * object depends on the architecture and its implementation, size_t is used
   * to represent the maximum size of any object in the particular
   * implementation. size contains the size of the data object or the number of
   * free bytes
   */
<<<<<<< HEAD
  bool free;
=======
>>>>>>> 3b743adc95c7924faf12c74a0f593998afd2b9b7
  size_t size;
  struct metadata* next;
  struct metadata* prev; 
} metadata_t;

/* freelist maintains all the blocks which are not in use; freelist is kept
 * sorted to improve coalescing efficiency 
 */

static metadata_t* freelist = NULL;

void* dmalloc(size_t numbytes) {
  /* initialize through sbrk call first time */
<<<<<<< HEAD
  if(freelist == NULL) {      
=======
  if(freelist == NULL) { 			
>>>>>>> 3b743adc95c7924faf12c74a0f593998afd2b9b7
    if(!dmalloc_init())
      return NULL;
  }

  assert(numbytes > 0);
<<<<<<< HEAD
  metadata_t* currentblock = freelist;

  //find a free block that is big enough
  while (!currentblock->free || currentblock->size < numbytes) {
    if (currentblock->next) {
      currentblock = currentblock->next;
    } else {
      return NULL;
    }
  }

  //allocated to current
  currentblock->free = false;

  //implement spliting
  if (currentblock->size > (numbytes + METADATA_T_ALIGNED)) {

    //pointer to a new block
    metadata_t* newblock = (metadata_t *)(((void*) currentblock) + numbytes + METADATA_T_ALIGNED);
    newblock->free = true;
    newblock->size = currentblock->size - numbytes - METADATA_T_ALIGNED;
    newblock->prev = currentblock;
    newblock->next = currentblock->next;

    //need a pointer to newblock from the next block of newblock
    if (newblock->next) {
      newblock->next->prev = newblock;
    }
    //pointer to newblock from the previous block of new block
    if (newblock->prev) {
      newblock->prev->next = newblock;
    }

    //updated since last submission
    currentblock->size = numbytes;
    currentblock->next = newblock;
  }
 
  //pointer to the current block
  metadata_t* ptr = (metadata_t *)(((void*) currentblock) + METADATA_T_ALIGNED);

  return ptr;
}

void dfree(void* ptr) {
  //updated since last submission
  metadata_t* currentblock = ((metadata_t*) ptr) - 1;

  //free the current block
  currentblock->free = true;

  //pointer to previous and next blocks
  metadata_t* prevblock = currentblock->prev;
  metadata_t* nextblock = currentblock->next;

  //coalesce
  //both previous and next blocks are free, coalesce both
  if (prevblock && prevblock->free && nextblock && nextblock->free) {
    prevblock->size += currentblock->size + METADATA_T_ALIGNED + nextblock->size + METADATA_T_ALIGNED;
    prevblock->next = nextblock->next;
  }
  //only previous block is free
  else if (prevblock && prevblock->free && (!nextblock || !nextblock->free)) {
    prevblock->size += currentblock->size + METADATA_T_ALIGNED;
    prevblock->next = nextblock;
  }
  //only next block is free
  else if ((!prevblock || !prevblock->free) && nextblock && nextblock->free) {
    currentblock->size += nextblock->size + METADATA_T_ALIGNED;
    currentblock->next = nextblock->next;
  }
  //last case if both previous and next are not free do nothing
  else if ((!prevblock || !prevblock->free) && (!nextblock || !nextblock->free)) {
    return;
  }
=======

  /* your code here */
	
  return NULL;
}

void dfree(void* ptr) {
  /* your code here */
>>>>>>> 3b743adc95c7924faf12c74a0f593998afd2b9b7
}

bool dmalloc_init() {

  /* Two choices: 
   * 1. Append prologue and epilogue blocks to the start and the
   * end of the freelist 
   *
   * 2. Initialize freelist pointers to NULL
   *
   * Note: We provide the code for 2. Using 1 will help you to tackle the 
   * corner cases succinctly.
   */

  size_t max_bytes = ALIGN(MAX_HEAP_SIZE);
  /* returns heap_region, which is initialized to freelist */
  freelist = (metadata_t*) sbrk(max_bytes); 
  /* Q: Why casting is used? i.e., why (void*)-1? */
  if (freelist == (void *)-1)
    return false;
<<<<<<< HEAD
  freelist->free = true; // initially all free
=======
>>>>>>> 3b743adc95c7924faf12c74a0f593998afd2b9b7
  freelist->next = NULL;
  freelist->prev = NULL;
  freelist->size = max_bytes-METADATA_T_ALIGNED;
  return true;
}

/* for debugging; can be turned off through -NDEBUG flag*/
void print_freelist() {
  metadata_t *freelist_head = freelist;
  while(freelist_head != NULL) {
    DEBUG("\tFreelist Size:%zd, Head:%p, Prev:%p, Next:%p\t",
<<<<<<< HEAD
    freelist_head->size,
    freelist_head,
    freelist_head->prev,
    freelist_head->next);
=======
	  freelist_head->size,
	  freelist_head,
	  freelist_head->prev,
	  freelist_head->next);
>>>>>>> 3b743adc95c7924faf12c74a0f593998afd2b9b7
    freelist_head = freelist_head->next;
  }
  DEBUG("\n");
}
