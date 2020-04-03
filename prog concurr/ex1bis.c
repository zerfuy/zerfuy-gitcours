#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>


int main(int argc, char argv[]){
    int nbProc = atoi(argv[1]);
    int i, pid, numPipe;
    int arrayPids[nbProc];
    int     [nbProc][2];

    // init pipes
    for(i=0 ; i < nbProc ; i++){   
        pipe(arrayPipes[i]);
    }

    for(i=0 ; i < nbProc ; i++){   
        pid = fork();
        arrayPids[i] = pid;

        if(!pid){

            printf("processus pid %d, numéro %d \n", getpid(), i);
        
        } else {
            break;
        }
    }

    for(int i=0 ; i < nbProc ; i++){
                if(i != numPipe && i != numPipe + 1){
                    close(arrayPipes[i][0]);
                    close(arrayPipes[i][1]);
                }else {
                    if(i == numPipe){
                        close(arrayPipes[i][1]);
                    } else {
                        close(arrayPipes[i+1][0]);
                    }
                }
            }
            
            dup2(arrayPipes[numPipe][1], 1);
            dup2(arrayPipes[numPipe+1][0], 0);

    return 0;
}
