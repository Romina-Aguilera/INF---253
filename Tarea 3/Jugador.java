import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class Jugador extends Personaje {
    private String nombre;
    private Integer xp;
    private List<Item> inventario;
    private Map<String, Equipamiento> equipamientos;
    private Arma arma;

    /*
    * Constructor de la clase Jugador
    * 
    * @param nombre: nombre del Jugador
    * 
    * return : No retorna nada
    */
    public Jugador (String nombre){
        super(100,1);
        this.xp = 0;
        this.nombre = nombre;
        List<Item> items = new ArrayList<>();
        this.inventario = items;
        this.arma = new Arma(0.25f,0.5f,"espada basica");
        this.equipamientos = new HashMap <String, Equipamiento>();
        this.equipamientos.put("Armadura", null);
        this.equipamientos.put("Botas", null);
        this.equipamientos.put("Amuleto", null);
    }

    public char getRepresentacion(){
        return 'J';
    }

    public void ganarXp(Integer xp){
        this.xp = this.xp+xp;
        if (xp >= 100 ){
            this.aumentarNivel();
        }
    }

    public void equiparA(Arma arma){
        this.arma = arma;
    }

    /*public void equiparE(Equipamiento equipamiento){

        /*if(equipamientos.get("Armadura") == null){
            equipamientos.put("Armadura", equipamientos);

        } else if (equipamientos.get("Botas")== null){
            equipamientos.put("Botas", equipamientos);

        } else if (equipamientos.get("Amuleto")== null){
            equipamientos.put("Amuleto", equipamientos);
        }
    }*/

    /*
    * Muestra por pantalla las estadisticas del Jugador
    * 
    * @param nivel: nivel del personaje
    * 
    * return : No retorna nada
    */
    public void Estadisticas(int nivel){
        System.out.println("Estadisticas del Jugador:");
        System.out.println(nombre);
        System.out.println(nivel);
        System.out.println(xp);
        System.out.println(super.getHp());
        float ataque = super.calcularAtaque() + arma.calcularAtaque(0, 0); // TODO: agregar parametros de calcular ataque.
        System.out.println(ataque);

        Equipamiento Botas = equipamientos.get("Botas");
        Equipamiento Amuleto = equipamientos.get("Amuleto");
        Equipamiento Armadura = equipamientos.get("Armadura");

        if (Botas != null){
            System.out.println(Botas.getNombre());
        } else {
            System.out.println("No tiene botas equipadas");
        }

        if(Amuleto != null){
            System.out.println(Amuleto.getNombre());
        } else {
            System.out.println("No tiene amuleto equipado");
        }

        if(Armadura != null){
            System.out.println(Armadura.getNombre());
        } else {
            System.out.println("No tiene armadura equipada");
        }

        System.out.println(arma.getNombre());
    }

    /*
    * Muestra por pantalla el inventario del Jugador
    * 
    * No tiene parametros
    * 
    * return : No retorna nada
    */
    public void Inventario(){
        System.out.println("Inventario del Jugador:");

        if (inventario.isEmpty()){
            System.out.println("El inventario esta vacio");
        } else {
            for (Item it :inventario ){
                System.out.println(it);
            }
        }

    }
}