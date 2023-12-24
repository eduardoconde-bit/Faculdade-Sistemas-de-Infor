package Questao1;

public class Triangulo extends ObjetoGeometrico{

    double l1, l2, l3, s;

    //Construtor
    public Triangulo(double width, double height, double l1, double l2, double l3) {
        super(width, height);
        this.l1 = l1;
        this.l2 = l2;
        this.l3 = l3;
    }
    
    //Método da Área
    public double area() {
        s = (l1 + l2 + l3) / 2;
        return Math.sqrt(s*(s - l1) * (s - l2) * (s - l3));
    }

    //Método do perimetro
    public double perimetro() {
        return l1 + l2 + l3;
    }
}
