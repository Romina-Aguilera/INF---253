public class Equipamiento extends Item{
    private String tipo;
    private Integer stra;
    private Integer inta;

    /*
    * Constructor de la Equipamiento
    * 
    * @param tipo : tipo del quipamiento(Armadura, botas, amuleto)
    * @param stra : fuerza del item
    * @param inta : inteligencia que otorga el item
    * @param nombre: nombre del item
    * 
    * return : No retorna nada
    */

    public Equipamiento(String tipo, Integer stra, Integer inta, String nombre){
        
        super('E',nombre);
        this.inta = inta;
        this.stra = stra;
        this.tipo = tipo;
    }

    public String getTipo(){
        return tipo;
    }

    public Integer getStra(){
        return stra;
    }

    public Integer getInta(){
        return inta;
    }
}
