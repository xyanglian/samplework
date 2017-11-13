#include <stdlib.h>
#include <iostream>
#include "thread.h"
#include <assert.h>
#include <stdint.h>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <iterator>

using namespace std;

int g=0;
int max_order = 0;

char **g_argv;
vector<int> arr_sandwiches;
vector<int> arr_cashiers;

int cashier_lock = 1;
int can_post = 2;
int board_full = 3;

int prev_sandwich = -1;
int cashier_made;
int num_active;

void loop_maker(void *a) {
  
  
  thread_lock(cashier_lock);
  while (num_active>=1) {

    while (arr_sandwiches.size() < max_order) {
      thread_broadcast(cashier_lock,can_post);
      thread_wait(cashier_lock,board_full);
    }
    if (num_active != 0) {
      int *arr = arr_sandwiches.data();
      int *arr_indexes = arr_cashiers.data();
      if (prev_sandwich == -1) { //finds the very first sandwich to make
        int min = 2000;
        for (int i=0; i<arr_sandwiches.size();i++) {
          if (arr[i] < min) {
            min = arr[i];
          }
        }
        for (int j=0;j<arr_sandwiches.size();j++) {
          if (arr[j] == min) {
            prev_sandwich = arr[j];
            cashier_made = arr_indexes[j];
            arr_sandwiches.erase(arr_sandwiches.begin()+j);
            arr_cashiers.erase(arr_cashiers.begin()+j);
	    	break;
 	  }
	}      
      } else {
        int min_diff = 2000;
        for (int i=0; i < arr_sandwiches.size(); i++) {
          if (abs(arr[i] - prev_sandwich) < min_diff) {
            min_diff = abs(arr[i] - prev_sandwich);
          }
        }
     
        for (int j=0; j < arr_sandwiches.size(); j++) {
          if (abs(arr[j] - prev_sandwich) == min_diff) {
            prev_sandwich = arr[j];
            cashier_made = arr_indexes[j];
            arr_sandwiches.erase(arr_sandwiches.begin()+j);
            arr_cashiers.erase(arr_cashiers.begin()+j); 
	        break;
          } 
        }
      } 
      
      cout << "READY: cashier " << cashier_made << " sandwich " << prev_sandwich << endl;
    
      thread_broadcast(cashier_lock,can_post);
    } 
  }  
  thread_unlock(cashier_lock);
}

void loop_cashiers(void *a) {
  thread_lock(cashier_lock);
  int* cashier_index;
  string sandwich;
  cashier_index = (int *) a;
  
  ifstream myfile(g_argv[(uintptr_t)cashier_index + 2]);
  
  while (getline(myfile,sandwich)) { 
    
    while (arr_sandwiches.size() == max_order || find(arr_cashiers.begin(),arr_cashiers.end(),(uintptr_t)cashier_index)!=arr_cashiers.end()) {
    	thread_broadcast(cashier_lock,board_full);
    	thread_wait(cashier_lock,can_post);
    }

    arr_sandwiches.push_back(atoi(sandwich.c_str())); 
    arr_cashiers.push_back((uintptr_t)cashier_index);
    cout << "POSTED: cashier " << (uintptr_t)cashier_index << " sandwich " << sandwich << endl;

    if (arr_sandwiches.size() < max_order) { 
      thread_broadcast(cashier_lock, can_post);
    }
    else { 
      thread_broadcast(cashier_lock, board_full);
    }
    
  }

  while (find(arr_cashiers.begin(),arr_cashiers.end(),(uintptr_t)cashier_index)!=arr_cashiers.end()){
    
    thread_broadcast(cashier_lock,board_full);
    thread_wait(cashier_lock,can_post);
  }
  num_active--;
  
  if (num_active<max_order) {
    max_order = num_active;
    thread_broadcast(cashier_lock,board_full);
  }
  
  thread_unlock(cashier_lock);
}


void cashier(void *a) {
  int num_cashiers;
  int i;
 
  //start_preemptions(true, false,101);
  num_cashiers = (uintptr_t) a;
  num_active = num_cashiers;
  if (num_active<max_order){
    max_order = num_active;
  }
  
  for (i=0; i<num_cashiers; i++){
    if (thread_create((thread_startfunc_t) loop_cashiers, (void *) (intptr_t)i)) {
      cout << "thread_create failed\n";
      exit(1);
    }
  }
  //cout << "created" << endl;
  if (thread_create((thread_startfunc_t) loop_maker, (void *) "maker")) {
    cout << "thread_create failed\n";
    exit(1);
  }
}

int main(int argc, char *argv[]) {
  max_order = atoi(argv[1]);
  
  
  g_argv = argv;
  
  
  if (thread_libinit((thread_startfunc_t) cashier, (void *) (intptr_t)(argc - 2))){
    cout << "thread_libinit failed\n";
    exit(1);
  }
  
}
