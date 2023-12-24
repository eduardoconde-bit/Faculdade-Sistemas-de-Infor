/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package questao7;

/**
 *
 * @author eduardo
 */
public class Ponto {
    private float x, y;
    
    //Construtor
    public Ponto(float x, float y) {
        this.x = x;
        this.y = y;
    }
    
    //Move a coordenada
    public void move(float dx, float dy) {
        this.x = dx;
        this.y = dy;
    }
    
    //Exibe a coordenada
    public void exibe() {
        System.out.printf("Ponto (%.2f , %.2f)\n", this.x, this.y);
    }
}
