#lang scheme

;; Retorna una lista en la cual cada elemento corresponde al tamaño de los bloques con igual cantidad de bits 
;; de una lista compuesta por 0 y 1
;;
;; lista: lista de 0 y 1 a encontrar
;; elemento: 1 o 0 dependiendo del elemento que se quiera buscar
;; contador: cantidad de veces que se encuentra el elemento 
;; res: lista con el tamaño de los bloques con igual cantidad de bits
(define (encode_aux lista elemento contador res)
  (cond (( null? lista) (append res (list contador)))
        ((= (car lista) elemento) (encode_aux (cdr lista) (car lista) (+ contador 1) res))
        (else ( encode_aux (cdr lista) (car lista) 1 (append res (list contador))))))

(define(encode bits)
  (encode_aux bits 0 0 '()))






;; Retorna lista en la cual cada elemento está la cantidad de veces que se indica en una lista codificada
;; por la funcion "encode", por medio de recursion tipo cola
;;
;; lista: lista a transformar
;; elemento: 1 o 0 dependiendo del elemento que se quiera agregar a la lista
;; res: lista decodificada
(define (decode_cola_aux lista elemento res)
  (cond ((null? lista)res)
        ((=(car lista) 0)(decode_cola_aux (cdr lista) (- 1 elemento) (append res '())))
        (else (decode_cola_aux(append (list (-(car lista)1))(cdr lista)) elemento (append res (list elemento))))))

(define (decode_cola lista)
  (decode_cola_aux lista 0 '()))






;; Retorna lista en la cual cada elemento está la cantidad de veces que se indica en una lista codificada
;; por la funcion "encode", por medio de recursion simple
;;
;; lista: lista a transformar
;; elemento: 1 o 0 dependiendo del elemento que se quiera agregar a la lista
(define (decode_simple_aux lista elemento)
  (cond
    ((null? lista) '())
    ((=(car lista) 0) (decode_simple_aux (cdr lista) (- 1 elemento)))
    ( else (cons elemento (decode_simple_aux (cons (-(car lista)1) (cdr lista)) elemento)))))

(define (decode_simple lista)
  (decode_simple_aux lista 0))






;; Retorna el resultado de la operacion f(a+k((b-a)/n))
;;
;; a: limite inferior
;; b: limite superior
;; n: cantidad de veces
;; f: funcion a aplicar
;; contador: veces que se realiza la sumatoria
;; valor: resultado final
(define (suma_simple a b n f contador valor)
  (if (= n contador)
      valor
      (+ valor (suma_simple a b n f (+ contador 1)(f(+ a(* contador (/(- b a)n))))))))

(define (integrar_simple a b n f)
  (*(/(- b a)n)
    (+(/(f a)2)
      (/(f b)2)
      (suma_simple a b n f 1 0))))






(define (map_arbol arbol camino f)
  (cond ((null? arbol) '())
        ((null? camino) (list (f (car arbol)) (cdr arbol)))
        ((=(car camino)0) (list(f (first arbol)) (map_arbol (second arbol) (cdr camino) f)(third arbol)))
        (else (list(f (first arbol)) (second arbol) (map_arbol (third arbol) (cdr camino) f)))))

      