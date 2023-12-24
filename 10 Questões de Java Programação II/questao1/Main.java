/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package questao1;

/**
 *
 * @author Eduardo
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Circulo circulo = new Circulo(20);
        System.out.printf("Raio do c�rculo: %.2f\n", circulo.getRaio());
        System.out.printf("Coordenadas X e Y: (%d, %d)\n", circulo.getX(), circulo.getY());
        // Desloca 'x' 17 unidades +
        circulo.setX(17);
        System.out.println("---------------------------------------------------");
        System.out.printf("Raio do círculo: %2f\n", circulo.getRaio());
        System.out.printf("Coordenadas X e Y: (%d, %d)\n", circulo.getX(), circulo.getY());
    }

}
