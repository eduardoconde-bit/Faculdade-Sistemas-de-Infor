/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package questao5;

/**
 *
 * @author eduardo
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Contador contador = new Contador();
        contador.inicializa();
        System.out.println("Contador depois de inicializar: "+ contador.getContador());
        contador.incrementa();
        contador.incrementa();
        System.out.println("Contador Incrementado 2x: " + contador.getContador());
        contador.decrementa();
        System.out.println("Contador Decrementado 1x: " + contador.getContador());
    }
    
}
