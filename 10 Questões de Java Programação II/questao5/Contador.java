/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package questao5;

/**
 *
 * @author eduardo
 */

public class Contador {
    //atributo privado contador
    private int contador;
    
    //Método inicializa
    public void inicializa() {
        this.contador = 0;
    }   
    
    //Método incrementa 1 ao contador
    public void incrementa() {
        this.contador++;
    }
   
    //Método decrementa 1 ao contador
    public void decrementa() {
        this.contador--;
    }
    
    //Método que retorna o contador
    public int getContador() {
        return this.contador;
    }
}
