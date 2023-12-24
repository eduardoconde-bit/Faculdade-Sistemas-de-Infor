package Questao2;

public class Circulo extends ObjetoGeometrico {

    double x, y, raio;

    //Construtor
    public Circulo(double x, double y, double raio) {
        this.x = x;
        this.y = y;
        this.raio = raio;
    }

    //Método da Área        
    double area() {
        return Math.PI * raio * raio;
    }
    
    //Método do Perímetro
    double perimetro() {
        return 2 * Math.PI * raio;
    }
}
