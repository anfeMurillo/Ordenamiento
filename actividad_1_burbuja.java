import java.util.Scanner;

public class actividad_1_burbuja {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        int[] code = new int[10];  // Declaración del arreglo de códigos
        String[] name = new String[10];  // Declaración del arreglo de nombres

        // Asignación de valores
        code[0] = 10; name[0] = "Camila";
        code[1] = 4; name[1] = "Daniel";
        code[2] = 3; name[2] = "Sofía";
        code[3] = 2; name[3] = "Juan";
        code[4] = 7; name[4] = "Valentina";
        code[5] = 6; name[5] = "Carlos";
        code[6] = 5; name[6] = "Isabella";
        code[7] = 9; name[7] = "Andrés";
        code[8] = 8; name[8] = "Mariana";
        code[9] = 1; name[9] = "Felipe";

        entrada.close(); // Cerramos Scanner, ya que no se usa entrada de datos

        // Método de burbuja optimizado
        boolean swapped;
        for (int i = 0; i < code.length - 1; i++) {
            swapped = false;  // Bandera para verificar si hubo intercambios
            for (int j = 0; j < code.length - 1 - i; j++) { // Evitamos comparaciones innecesarias
                if (code[j] > code[j + 1]) {  
                    // Intercambio de códigos
                    int aux = code[j];
                    code[j] = code[j + 1];
                    code[j + 1] = aux;

                    // Intercambio de nombres
                    String auxNombre = name[j];
                    name[j] = name[j + 1];
                    name[j + 1] = auxNombre;

                    swapped = true; // Se realizó un intercambio
                }
            }
            if (!swapped) break; // Si no hubo intercambios, el arreglo ya está ordenado
        }

        // Mostrar los datos ordenados
        System.out.println("\nArreglo ordenado en orden creciente:");
        for (int i = 0; i < code.length; i++) {
            System.out.println(code[i] + " - " + name[i]);
        }
    }
}
