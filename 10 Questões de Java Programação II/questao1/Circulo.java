/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package questao1;

/**
 *
 * @author Eduardo
 */
public class Circulo {
    private double raio;
    private int x, y;
    
    //construtor
    public Circulo(double raio) {
        this.x = 0;
        this.y = 0;
        this.raio = raio;
    }
    
    public void setX(int valorX) {
        this.x = valorX;
    }
    
    public void setY(int valorY) {
        this.y = valorY;
    }
    
    /*public void setAlteraXY(int valorX, int valorY) {
        this.x = valorX;
        this.y = valorY;
    }*/
    
    public int getX() {
        return this.x;
    }
    
    public int getY() {
        return this.y;
    }
    
    public double getRaio() {
        return this.raio;
    }
}
