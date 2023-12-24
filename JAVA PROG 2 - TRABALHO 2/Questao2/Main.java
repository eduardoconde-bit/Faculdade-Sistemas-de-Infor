package Questao2;

public class Main {
    public static void main(String[] args) {
        TrianguloEquilatero trianguloEquilatero = new TrianguloEquilatero(20);
        TrianguloIsosceles trianguloIsosceles = new TrianguloIsosceles(10, 7);
        TrianguloEscaleno trianguloEscaleno = new TrianguloEscaleno(10, 12, 15);
        Quadrado quadrado = new Quadrado(10);

        System.out.println();

        //Equilatero
        System.out.println("Triângulo Equilátero");
        System.out.println("Área: " + trianguloEquilatero.area());
        System.out.println("Perímetro: " + trianguloEquilatero.perimetro());

        System.out.println();
        
        //Isosceles
        System.out.println("Triângulo Isosceles");
        System.out.println("Área: " + trianguloIsosceles.area());
        System.out.println("Perímetro: " + trianguloIsosceles.perimetro());

        System.out.println();

        //Escaleno
        System.out.println("Triângulo Escaleno");
        System.out.println("Área: " + trianguloEscaleno.area());
        System.out.println("Perímetro: " + trianguloEscaleno.perimetro());

        System.out.println();

        //Quadrado
        System.out.println("Quadrado");
        System.out.println("Área: " + quadrado.area());
        System.out.println("Perímetro: " + quadrado.perimetro());
    }
}
