package Questao6;

public class Circulo extends Forma{
    public float raio;

    public Circulo (float raio) {
        this.raio = raio;
    }

    public float calcularArea() {
        return ((float)Math.PI) * raio * raio;
    }

    public float calcularPerimetro() {
        return 2 * ((float)Math.PI) * raio;
    }

    public void imprimeDados() {
        System.out.println("Área: " + calcularArea());
        System.out.println("Comprimento: " + calcularPerimetro());
    }
}