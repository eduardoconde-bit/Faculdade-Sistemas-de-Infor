/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package questao2;

/**
 *
 * @author Eduardo
 */
public class Circulo2 {
    //Atributos da classe
    private double raio;
    private int x, y;
    
    //construtor da classe
    /*public Circulo2() {
        this.x = 0;
        this.y = 0;
        this.raio = 0;
    }*/
    
    //Método Inicializa
    public void inicializa(int valorX, int valorY, double valorRaio) {
        this.raio = valorRaio;
        this.x = valorX;
        this.y = valorY;
    }
    
    public void setX(int valorX) {
        this.x = valorX;
    }
    
    public void setY(int valorY) {
        this.y = valorY;
    }
    
    public void setXY(int valorX, int valorY) {
        this.x = valorX;
        this.y = valorY;
    }
    
    public int getX() {
        return this.x;
    }
    
    public int getY() {
        return this.y;
    }
    
    public void alteraRaio(double valorRaio) {
        this.raio = valorRaio;
    }
    
    public double getRaio() {
        return this.raio;
    }
}