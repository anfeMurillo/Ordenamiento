import java.util.Scanner;

public class Metodo_Burbuja {
    public static void main (String [] args ){

        Scanner entrada = new Scanner(System.in);

        int code [], nElementos = 10, aux = 0;
        String name[], auxNombre;


        //Declaracion de del tamaño del arreglo
        code = new int[nElementos];
        name = new String[nElementos];

        //Asignacion de los valores del arreglo en cada posicion
        code [0] = 10; name[0] = "Camila";
        code [1] = 4; name[1] = "Daniel";
        code[2] = 3; name[2] = "Sofía";
        code[3] = 2; name[3] = "Juan";
        code[4] = 7; name[4] = "Valentina";
        code[5] = 6; name[5] = "Carlos";
        code[6] = 5; name[6] = "Isabella";
        code[7] = 9; name[7] = "Andrés";
        code[8] = 8; name[8] = "Mariana";
        code[9] = 1; name[9] = "Felipe";



        //Metodo burbuja
        for( int i=0 ; i <nElementos-1 ; i++){ //Bucle for para recorrer el arreglo por fuera y saber cuantas vueltas tiene que dar
            for (int j=0 ; j< nElementos-1; j++){ // Bucle para recorer, comparar los elementos y ordenarlos
                if (code[j] > code[j+1]) { //Condicion para saber si el elemento de la izquierda es mayor que el de la derecha
                    aux = code[j]; //si la variable aux es igual al numero actual
                    code[j] = code[j+1]; //si numero actual es igual al numero siguiente
                    code[j+1] = aux; // y en esta el numero siguiente va quedar guardado con el numero actual que estaba en aux

                    //Intercambio de nombre
                    auxNombre = name[j];
                    name[j] = name[j+1];
                    name[j+1] = auxNombre;


                }
            }
        }

        //mostrar los datos
        System.out.println("\nArreglo de forma ordenada creciente: ");
        for ( int i = 0 ; i < nElementos ; i++){
            System.out.println(code[i]+" - " + name[i]);

        }

    }
}