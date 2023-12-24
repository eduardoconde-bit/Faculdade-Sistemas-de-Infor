package Questao5;

public class Circulo implements Impressao, FormaGeometrica{
    private double raio;

    public Circulo (double raio) {
        this.raio = raio;
    }

    public double area() {
        return Math.PI * raio * raio;
    }

    public double comprimento() {
        return 2 * Math.PI * raio;
    }

    public void imprimeDados() {
        System.out.println("Área: " + area());
        System.out.println("Comprimento: " + comprimento());
    }
}
