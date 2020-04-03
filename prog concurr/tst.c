#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include<sys/wait.h> 
#include <fcntl.h>
#include <unistd.h>
#include <string.h>


int main(int argc, char argv[]){
    // exemple de redirection avec pip pour un ls
    int tube[2];
    int fichier;
    fichier = open("tmp", O_WRONLY|O_CREAT);

    pipe(tube);

    if (!fork()){ // !0 donc fork = 0 donc fils
        dup2(tube[1], 1);
        dup2(tube[0], fichier);
        close(tube[1]);
        close(tube[0]);
        execlp("ls", "ls", NULL);
    } else {
        close(tube[1]);
        close(tube[0]);
        wait(NULL);
    }
       
    return 0;
}
