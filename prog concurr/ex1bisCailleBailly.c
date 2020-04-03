#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <time.h>


int main(int argc, char* argv[]){
    if(argc != 2) {
        perror("NB arg HS");
        exit(-1);
    }
    int nbProc = atoi(argv[1]) - 1;
    int tubes[nbProc + 1][2];
    int process[nbProc];
    int i = 0;
    for(int j = 0; j < nbProc + 1; j++) {
        pipe(tubes[j]);
    }
    while(i < nbProc) {
        process[i] = fork();
        if(process[i] == 0) break;
        i++;
    }
    if(i != nbProc) {
        for(int j = 0; j < nbProc; j++) {
            if(j == i) close(tubes[j][1]);
            else {
                if(j == i + 1) close(tubes[j][0]);
                else {
                    close(tubes[j][0]);
                    close(tubes[j][1]);
                }
            }
        }
        srand(getpid());
        int randVal = rand() % 10000;
        printf("processus pid %d numero %d valeur = %d\n", getpid(), i+1, randVal);
        int randValMax;
        read(tubes[i][0], &randValMax, sizeof(int));
        if(randVal > randValMax) randValMax = randVal;
        write(tubes[i + 1][1], &randValMax, sizeof(randValMax));
        close(tubes[i][0]);
        close(tubes[i + 1][1]);
    } else {
        for(int j = 0; j < nbProc; j++) {
            if(j == 0) close(tubes[j][0]);
            else {
                if(j == nbProc - 1) close(tubes[j][1]);
                else {
                    close(tubes[j][0]);
                    close(tubes[j][1]);
                }
            }
        }
        srand(getpid());
        int randVal = rand() % 10000;
        printf("proc pid %d ; num %d ; val %d ;\n", getpid(), 0, randVal);
        int randValMax;
        write(tubes[0][1], &randVal, sizeof(randVal));
        read(tubes[nbProc][0], &randValMax, sizeof(int));
        printf("Max : %d\n", randValMax);
        close(tubes[0][1]);
        close(tubes[nbProc][0]);
        for(int j = 0; j < nbProc; j++) wait(&process[j]);
    }

    return 0;

}