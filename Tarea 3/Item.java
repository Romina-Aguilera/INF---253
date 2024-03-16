public abstract class Item implements Visible {
    private char representacion;
    private String nombre;

    /*
    * Constructor de la clase Item
    * 
    * @param representacion: representacion del Item
    * @param nombre : nombre del Item
    * 
    * return : No retorna nada
    */
    public Item (char representacion, String nombre){
        
        this.nombre = nombre;
        this.representacion = representacion;
    }
    public char getRepresentacion(){
        return representacion;
    }

    public String getNombre(){
        return nombre;
    }

    public void setRepresentacion(char representacion){
        this.representacion = representacion;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }
}
