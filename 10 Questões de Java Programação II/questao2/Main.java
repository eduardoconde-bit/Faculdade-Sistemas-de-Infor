/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package questao2;

/**
 *
 * @author Eduardo
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Circulo2 circulo = new Circulo2();
        circulo.inicializa(0, 0, 10);
        System.out.printf("Raio do c�rculo: %.2f\n", circulo.getRaio());
        System.out.printf("Coordenadas X e Y: (%d, %d)\n", circulo.getX(), circulo.getY());
        //move o c�rculo para a coodernada (1, 1) e em seguida define coordenada x como 100;
        circulo.setXY(1, 1);
        circulo.setX(100);
        System.out.println("---------------------------------------------------");
        System.out.printf("Novas Coordenadas (x, y): (%d, %d)\n", circulo.getX(), circulo.getY());
        //Altera o raio para 12 e imprime em seguida
        circulo.alteraRaio(12);
        System.out.println("Raio alterado: " + circulo.getRaio());
    }
}
