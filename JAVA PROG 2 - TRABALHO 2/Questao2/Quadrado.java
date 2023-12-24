package Questao2;

public class Quadrado extends Retangulo{
    double l;

    Quadrado(double l) {
        this.l = l;
    }

    double area() {
        return Math.pow(l, 2);
    }

    double perimetro() {
        return l * 4;
    }
}
