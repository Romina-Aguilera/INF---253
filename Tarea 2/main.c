#include "arbol.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

Nodo* nodo_raiz(Nodo*);
void liberar_nodo(Nodo*);

int main(){
    Nodo* actual = crear_nodo(NULL, "directorio", "principal");
    char instruccion [300];

    for(;;){
        printf("instruccion: ");
        fgets(instruccion, 300, stdin);
        instruccion[strlen(instruccion)-1] = '\0';
        if (strncmp(instruccion,"mkdir ",6) == 0){
            char* nombre_dir = instruccion + 6;
            mkdir(actual,nombre_dir);

        } else if (strncmp(instruccion, "cd ",3) == 0){
            char* nombre_dir = instruccion + 3;
            if (strcmp(nombre_dir, "..")==0){
                if (actual->padre != NULL)
                    actual = actual->padre;
                else
                    printf("no hay padre\n");
            } else {
                Nodo* actual2;
                actual2 = buscar_directorio((Directorio*)actual->contenido, nombre_dir);
                if (actual2 == NULL)
                    printf("error\n");
                else
                    actual = actual2;
            }

        } else if (strncmp(instruccion, "touch ", 6) == 0){
            char* nombre_arch = instruccion + 6;
            touch(actual, nombre_arch);

        } else if (strncmp(instruccion, "write ", 6) == 0){
            char* nombre_arch = instruccion +6 ;
            char* contenido= nombre_arch + strcspn(nombre_arch," ") + 1;
            *(contenido-1) = '\0';
            write(actual, nombre_arch, contenido);

        } else if (strncmp(instruccion, "cat ", 4) == 0){
            char* nombre_arch = instruccion + 4;
            cat(actual, nombre_arch);

        } else if (strncmp(instruccion, "ls ", 3) == 0){
            char* nombre_dir = instruccion + 3;
            ls_dir(actual, nombre_dir);

        } else if (strcmp(instruccion, "ls") == 0){
            ls(actual);
        
        } else if (strncmp(instruccion, "mapdir touch ",13) == 0){
            char* nombre_arch = instruccion + 13;
            mapdir(actual,touch,nombre_arch);

        } else if (strncmp(instruccion, "mapdir ls ",10) ==0){
            char* nombre_dir = instruccion + 10;
            mapdir(actual, ls_dir, nombre_dir);

        } else if (strncmp(instruccion, "mapdir mkdir ", 13) == 0){
            char* nombre_dir = instruccion + 13;
            mapdir(actual, mkdir, nombre_dir);
        } else if (strncmp(instruccion, "exit", 4) == 0) {
            break;
        }
    }

    Nodo* nodo2 = nodo_raiz(actual);
    liberar_nodo(nodo2);
    free(nodo2);

}

/*
Descripcion: 
recupera el nodo padre del arbol

Parametros:
nodo (Nodo*): nodo actual

Retorno: 
nodo (Nodo*): padre del arbol
*/
Nodo* nodo_raiz(Nodo* nodo){
    Nodo* nodo_actual = nodo;
    while(nodo_actual->padre != NULL){
        nodo_actual = nodo_actual->padre;
    }
    return nodo_actual;
}

/*
Descripcion: 
liberar la memoria del arbol

Parametros:
nodo (Nodo*): nodo a liberar

Retorno: 
No retorna nada
*/
void liberar_nodo(Nodo* nodo){
    if (nodo==NULL){
        return;
    }

    if (strcmp(nodo->tipo, "archivo")==0){
        free(nodo->contenido);
    } else {
        for(int i =0; i<((Directorio*)nodo->contenido)->hijos->largo_actual; i++){
            Nodo* nodo_actual = & ((Directorio*)nodo->contenido)->hijos->arreglo[i];
            liberar_nodo(nodo_actual);
        }
        free(((Directorio*)nodo->contenido)->hijos->arreglo);
        free(((Directorio*)nodo->contenido)->hijos);
        free(nodo->contenido);
    }
}