package Questao2;

public class Triangulo extends ObjetoGeometrico{

    double l1, l2, l3, s;

    //Construtor
    public Triangulo() {
        super();
    }

    public Triangulo(double l1, double l2, double l3) {
        this.l1 = l1;
        this.l2 = l2;
        this.l3 = l3;
    }
    
    //Método da Área
    double area() {
        s = (l1 + l2 + l3) / 2;
        return Math.sqrt(s*(s - l1) * (s - l2) * (s - l3));
    }

    //Método do perimetro
    double perimetro() {
        return l1 + l2 + l3;
    }
}
