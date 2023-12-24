package Questao2;

public class TrianguloEquilatero extends Triangulo {

    double l;

    public TrianguloEquilatero(double l) {
        this.l = l;
    }

    double area() {
        return (Math.pow(l, 2) * Math.sqrt(3)) / 4; 
    }

    double perimetro() {
        return l * 3;
    }
}
