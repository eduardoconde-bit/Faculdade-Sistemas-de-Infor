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
    
    //M�todo inicializa
    public void inicializa() {
        this.contador = 0;
    }   
    
    //M�todo incrementa 1 ao contador
    public void incrementa() {
        this.contador++;
    }
   
    //M�todo decrementa 1 ao contador
    public void decrementa() {
        this.contador--;
    }
    
    //M�todo que retorna o contador
    public int getContador() {
        return this.contador;
    }
}
