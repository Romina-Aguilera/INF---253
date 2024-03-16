#include "arbol.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/*
Descripcion: 
Crea una lista para almacenar los nodos del arbol

Parametros:
largo_maximo_inicial (int): longitud maxima de la lista

Retorno: 
lista (Lista*) : puntero al struct Lista
*/
Lista* crear_lista(int largo_maximo_inicial){
    Lista* lista = malloc(sizeof(Lista));

    lista->largo_actual = 0;
    lista->largo_maximo = largo_maximo_inicial;
    lista->arreglo = malloc(sizeof(Nodo) * largo_maximo_inicial);
    return lista;
}


/*
Descripcion: 
insertar los nodos en la lista, si el largo actual es igual
al largo maximo entonces se duplica el tamaño y se actualiza el valor del largo maximo

Parametros:
lista (Lista*): lista donde se insertaran los nodos
nodo (Nodo*): nodo a insertar en la lista

Retorno: 
no retorna nada
*/
void insertar_lista (Lista* lista, Nodo* nodo){
    if (lista->largo_actual == lista->largo_maximo){
        lista->arreglo = realloc(lista->arreglo , sizeof(Nodo) * lista->largo_actual * 2);
        lista->largo_maximo = lista->largo_actual * 2;
    }
    lista->arreglo[lista->largo_actual] = *nodo;
    lista->largo_actual++;
}


/*
Descripcion:
Busca un directorio especificado en el directorio actual 

Parametros:
actual (Directorio*): directorio en donde uno se encuentra
nombre (char*): nombre del directorio a buscar

Retorno: 
nodo (Nodo*): puntero al directorio encontrado
*/
Nodo* buscar_directorio (Directorio* actual, char* nombre){
    for (int i =0; i < actual-> hijos ->largo_actual;i++){
        Nodo* nodo = &actual-> hijos ->arreglo[i];
        if (strcmp (nodo->tipo, "directorio") == 0){
            if (strcmp(((Directorio*)nodo->contenido)->nombre,nombre)==0){
                return nodo;
            } 
        }
    }
    return NULL;
}


/*
Descripcion: 
Busca un archivo especificado en el directorio actual

Parametros:
actual (Directorio*): directorio en donde uno se encuentra
nombre (char*): nombre del archivo a buscar

Retorno: 
nodo (Nodo*): puntero al archivo encontrado
*/
Nodo* buscar_archivo (Directorio* actual, char* nombre){
    for (int i =0; i < actual-> hijos ->largo_actual;i++){
        Nodo* nodo = &actual-> hijos ->arreglo[i];
        if (strcmp (nodo->tipo, "archivo") == 0){
            if (strcmp(((Archivo*)nodo->contenido)->nombre,nombre)==0){
                return nodo;
            } 
        }
    }
    return NULL;
}


/*
Descripcion: 
Crea un nodo del arbol

Parametros:
padre (Nodo*): padre del nodo a crear
tipo (char*): tipo del nodo a crear, en este caso archivo o directorio
nombre (char*): nombre del nodo a crear

Retorno: 
nodo (Nodo*): puntero al nodo creado
*/
Nodo* crear_nodo (Nodo* padre, char* tipo, char* nombre){
    Nodo* nodo = malloc(sizeof(Nodo));
    nodo ->padre = padre;
    strcpy(nodo->tipo, tipo);

    if (strcmp(tipo, "directorio") == 0){
        Directorio* aux = malloc(sizeof(Directorio));

        aux ->hijos = crear_lista(1);
        strcpy (aux->nombre, nombre);

        nodo->contenido = (void*) aux;
        
    } else if (strcmp(tipo,"archivo") == 0){
        Archivo* aux2 = malloc(sizeof(Archivo));

        aux2 ->contenido[0] = '\0';
        strcpy (aux2 ->nombre, nombre);

        nodo ->contenido = aux2;
    }
    return nodo;
}


/*
Descripcion: 
Crea un directorio en el directorio actual

Parametros:
actual (Nodo*): directorio actual
nombre_directorio (char*): nombre del directorio a crear

Retorno: 
no retorna nada
*/
void mkdir (Nodo* actual, char* nombre_directorio){
    Nodo* nuevo_dir = crear_nodo(actual,"directorio", nombre_directorio);
    insertar_lista(((Directorio*)actual->contenido)->hijos,nuevo_dir);
    free(nuevo_dir);
}


/*
Descripcion: 
Crea un archivo en el directorio actual

Parametros:
actual (Nodo*): directorio actual
nombre_directorio (char*): nombre del archivo a crear

Retorno: 
no retorna nada
*/
void touch (Nodo* actual, char* nombre_archivo){
    Nodo* nuevo_arch = crear_nodo(actual, "archivo", nombre_archivo);
    insertar_lista(((Directorio*)actual->contenido)->hijos,nuevo_arch);
    free(nuevo_arch);
}


/*
Descripcion: 
escribe dentro de un archivo especificado que este dentro del directorio actual

Parametros:
actual (Nodo*): directorio actual
nombre_archivo (char*): nombre del archivo donde se quiere escribir
contenido (char*): lo que se escribe dentro del archivo

Retorno: 
no retorna nada
*/
void write (Nodo* actual, char* nombre_archivo, char* contenido){
    Nodo* nodo = buscar_archivo((Directorio*)actual->contenido , nombre_archivo);
    if (nodo != NULL){
        strcpy(((Archivo*)nodo->contenido)->contenido, contenido);
    }
}


/*
Descripcion: 
imprime lo que hay escrito dentro de un archivo

Parametros:
actual (Nodo*): directorio actual
nombre_archivo (char*): nombre del archivo

Retorno: 
no retorna nada
*/
void cat (Nodo* actual, char* nombre_archivo){
    Nodo* nodo = buscar_archivo((Directorio*)actual->contenido , nombre_archivo);
    if (nodo != NULL){
        printf("%s\n", ((Archivo*)nodo->contenido)->contenido);
    }
}


/*
Descripcion: 
imprime los archivos y directorios del directorio actual

Parametros:
actual (Nodo*): directorio actual

Retorno: 
no retorna nada
*/
void ls (Nodo* actual){
    Lista* lista = ((Directorio*)actual->contenido)->hijos;
    for (int i =0; i < lista->largo_actual; i++){
        if (strcmp(lista->arreglo[i].tipo, "directorio") == 0){
            printf("./%s\n", ((Directorio*)lista->arreglo[i].contenido)->nombre);
        } else if (strcmp(lista->arreglo[i].tipo, "archivo") == 0){
            printf("%s\n",((Directorio*)lista->arreglo[i].contenido)->nombre);
        }
    }    
}


/*
Descripcion: 
imprime los archivos y directorios del directorio seleccionado

Parametros:
actual (Nodo*): directorio actual
nombre_directorio (char*): nombre del directorio donde se quiere imprimir

Retorno: 
no retorna nada
*/
void ls_dir(Nodo* actual, char* nombre_directorio){
    if (strcmp(nombre_directorio, ".") == 0){
        ls(actual);
        return;
    }
    Nodo* nodo = buscar_directorio((Directorio*)actual->contenido, nombre_directorio);
    if (nodo == NULL)
        printf("El directorio %s no existe\n", nombre_directorio);
    else 
        ls(nodo);
}


/*
Descripcion: 
aplica una instruccion especificada a todos los subdirectorios

Parametros:
actual (Nodo*): directorio actual
void (*instruccion)(Nodo*,char*) : funcion a ejecutar
parametro_instruccion (char*) : nombre de la instruccion a ejecutar

Retorno: 
no retorna nada
*/
void mapdir(
    Nodo* actual,
    void (*instruccion)(Nodo*, char*),
    char* parametro_instruccion
){
    for (int i =0; i < ((Directorio*)actual->contenido)->hijos->largo_actual; i++){
        Nodo* nodo = &((Directorio*)actual->contenido)->hijos->arreglo[i];
        if (strcmp(nodo -> tipo,"directorio")==0){
            instruccion(nodo, parametro_instruccion);
        }
    }
}