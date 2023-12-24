package Questao1;

public class Circulo extends ObjetoGeometrico {

    double x, y, raio;

    //Construtor
    public Circulo(double width, double height, double x, double y, double raio) {
        super(width, height);
        this.x = x;
        this.y = y;
        this.raio = raio;
    }

    //Método da Área        
    public double area() {
        return Math.PI * raio * raio;
    }
    
    //Método do Perímetro
    public double perimetro() {
        return 2 * Math.PI * raio;
    }
}
