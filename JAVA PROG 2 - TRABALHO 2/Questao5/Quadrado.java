package Questao5;

public class Quadrado implements FormaGeometrica, Impressao{
    private double lado;

    public Quadrado(double lado) {
        this.lado = lado;
    }

    public double area() {
        return Math.pow(lado, 2);
    }

    public double comprimento() {
        return lado * 4;
    }

    public void imprimeDados() {
        System.out.println("Área: " + area());
        System.out.println("Comprimento: " + comprimento());
    }
}
