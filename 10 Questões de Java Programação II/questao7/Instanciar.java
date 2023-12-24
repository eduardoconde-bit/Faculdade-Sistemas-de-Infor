/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package questao7;

/**
 *
 * @author eduardo
 */
public class Instanciar {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Ponto coordenada = new Ponto(-53, 40);
        coordenada.exibe();
        coordenada.move(20, 50);
        coordenada.exibe();
    }
    
}
