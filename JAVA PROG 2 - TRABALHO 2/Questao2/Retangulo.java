package Questao2;

public class Retangulo extends ObjetoGeometrico {
    //Herda e é aplicável o método "area" da superclasse ObjetoGeometrico para a subclasse Retangulo

    public Retangulo() {
        super();
    }

    public Retangulo(double width, double height) {
        super(width, height);
    }
    
    double perimetro() {
        return 2 * width + 2 * height;
    }
}
