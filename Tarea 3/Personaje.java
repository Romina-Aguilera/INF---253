public class Personaje implements Visible{
    private float hp;
    private Integer nivel;

    /*
    * Constructor de la clase Personaje, inicializa el personaje
    * 
    * @param hp: salud del personaje
    * @param nivel: nivel del personaje
    * 
    * @return : No retorna nada
    */
    public Personaje (float hp, Integer nivel){
        
        this.hp = hp;
        this.nivel = nivel;
    }

    public char getRepresentacion(){
        return 'O';
    }

    public void recibirDanio(Integer dmg){
        this.hp = this.hp-dmg;
    }

    public float calcularAtaque(){
        float danio = 3*this.nivel;
        return danio; 
    }

    /*
    * Aumenta el nivel del personaje
    * 
    * no tiene parametros
    *
    * return : No retorna nada
    */
    public void aumentarNivel(){
        this.nivel = this.nivel+1;
    }

    public float getHp(){
        return this.hp;
    }

}
