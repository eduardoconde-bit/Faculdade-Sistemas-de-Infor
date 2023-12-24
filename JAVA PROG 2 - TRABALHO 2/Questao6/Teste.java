package Questao6;

//Testando as Classes presentes no pacote
public class Teste {
    public static void main(String[] args) {
        Forma[] forma = new Forma[5];
        Retangulo retangulo = new Retangulo(40, 50);
        Quadrado quadrado = new Quadrado(10);
        Circulo circulo = new Circulo(10);
        Quadrado quadrado2 = new Quadrado(10);
        Retangulo retangulo2 = new Retangulo(15, 20);

        forma[0] = retangulo2;
        forma[1] = retangulo;
        forma[2] = quadrado;
        forma[3] = circulo;
        forma[4] = quadrado2;

        for(int i = 0; i < forma.length; i++) {
            System.out.println("---------------------------------");
            System.out.println("Área: " + forma[i].calcularArea());
            System.out.println("Perímetro: " + forma[i].calcularPerimetro());
            System.out.println("---------------------------------");
        }
    }
}
