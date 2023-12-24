package Questao6;

public class Retangulo extends Forma{
    float b, h; // Base e Altura

    Retangulo() {
        b = h = 0;
    }

    Retangulo(float b, float h) {
        this.b = b;
        this.h = h;
    }
    
    public float calcularArea() {
        return b * h;
    }

    public float calcularPerimetro() {
        return (b + h) * 2;
    }

    public void mostraDados() {
        System.out.println("Área: " + calcularArea());
        System.out.println("Perimetro: " + calcularPerimetro());
    }
}
