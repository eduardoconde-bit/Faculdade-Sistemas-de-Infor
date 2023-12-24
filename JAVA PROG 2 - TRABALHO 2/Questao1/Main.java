package Questao1;

public class Main {
    public static void main(String[] args) {
        Circulo circulo = new Circulo(0, 0, 2, 1, 20);
        Retangulo retangulo = new Retangulo(20, 30);
        Triangulo triangulo = new Triangulo(0, 0, 15, 15, 15);

        System.out.printf("Área e Perímetro do Círculo: %.2f, %.2f\n", circulo.area(), circulo.perimetro());
        System.out.printf("Área e Perímetro do Retângulo %.2f, %.2f\n:", retangulo.area(), retangulo.perimetro());
        System.out.printf("Área e Perímetro do Triângulo %.2f, %.2f\n:", triangulo.area(), triangulo.perimetro());
    }
}
