public class Arma extends Item{
    private float mul_str;
    private float mul_int;
    
    /*
    * Constructor del arma
    * 
    * @param mul_int : inteligencia del item
    * @param mul_str : fuerza del item
    * @param nombre: nombre del item
    * 
    * return : No retorna nada
    */

    public Arma(float mul_int, float mul_str, String nombre){
        
        super('A',nombre);
        this.mul_int = mul_int;
        this.mul_str = mul_str;
    }
    
    public float calcularAtaque(Integer str, Integer Int){
        float ataque = str*mul_str + Int*mul_int;
        return ataque;
    }
}