import java.util.Scanner;

public class JavaHack {
    static Scanner scanner = new Scanner (System.in);
    public static void main(String[] args) {   
        System.out.println("Ingrese Nombre del Jugador: ");
        String name = scanner.nextLine();

        Jugador jugador = new Jugador(name);

        System.out.println("Ingrese altura");
        Integer altura = scanner.nextInt();

        System.out.println("Ingrese ancho");
        Integer ancho = scanner.nextInt();

        Mundo mundo = new Mundo(altura,ancho,1,jugador);
        mundo.mostrar();

        System.out.println("Ingrese su jugada");
        String instruccion;
        instruccion = scanner.nextLine();
        instruccion = scanner.nextLine();

        while(instruccion.equals("Salir") == false){
            if (instruccion.equals("Estadisticas")){
                jugador.Estadisticas(1);
            } else if (instruccion.equals("Inventario")){
                jugador.Inventario();
            } else {
                System.out.println("Instruccion no valida");
            }
            System.out.println("Ingrese su jugada");
            instruccion = scanner.nextLine();
        }

    }

}
