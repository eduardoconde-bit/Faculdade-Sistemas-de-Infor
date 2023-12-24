/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package questao8;

/**
 *
 * @author eduardo
 */
public class Reta {
    private Ponto a, b;
    
    public Reta(float ax, float ay, float bx, float by) {
        a = new Ponto(ax, ay);
        b = new Ponto(bx, by);
    }
    
    public void exibe() {
        System.out.println("Coordenadas da Reta");
        a.exibe();
        b.exibe();
    }
}
