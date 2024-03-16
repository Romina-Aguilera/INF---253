import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.lang.Math;

public class Mundo{
    private Integer nivel;
    private Integer alto;
    private Integer ancho;
    private Integer enemigos;
    private List<List<Visible>> mapa;
    private Random random = new Random();

    /*
    * Constructor del mundo
    * 
    * @param alto : alto del mapa
    * @param ancho : ancho del mapa
    * @param nivel : nivel del mapa
    * @param jugador : Jugador en el mapa
    * 
    * return : No retorna nada
    */
    public Mundo (Integer alto, Integer ancho, Integer nivel, Jugador jugador){

        this.alto = alto;
        this.ancho = ancho;
        this.nivel = nivel;
        this.enemigos = 0;
        //crear numero random

        //Creacion de la matriz
        List<List<Visible>> matrizVisibles = new ArrayList<>();
        
        //Creacion de las filas y columnas de la matriz
        for (int i=0; i<alto; i++){
            List<Visible> fila = new ArrayList<Visible>(ancho);
            for (int j=0; j<ancho; j++){
                double aleatorio = random.nextDouble();
                double aleatorio2 = random.nextDouble();
                if (aleatorio <= Math.min(0.05+0.01*nivel,20.0)){
                    if (aleatorio2 < 0.5){
                        fila.add(new Arma(1,1,"prueba"));
                    } else {
                        fila.add(new Equipamiento("Armadura",1,1,"prueba"));
                    }
                } else if (aleatorio > Math.min(0.05+0.01*nivel,20.0) && aleatorio < Math.min(0.2+0.01*nivel,55.0)){
                    fila.add(new Personaje(1,1));
                    this.enemigos ++;
                } else{
                    fila.add(new Vacio());
                }
            }
            matrizVisibles.add(fila);
        }
        matrizVisibles.get(0).set(0,jugador);
        this.mapa = matrizVisibles;
    }

    public void mostrar(){
        for(List<Visible> fila :mapa ){
            for(Visible elemento: fila){
                System.out.print(elemento.getRepresentacion());
                System.out.print(" ");
            }
            System.out.println();
        }
    }

    public void nuevoNivel(Mundo mundo, Jugador jugador){
        this.nivel +=1;
        mundo = new Mundo(this.alto,this.ancho,this.nivel,jugador);   
    }
}