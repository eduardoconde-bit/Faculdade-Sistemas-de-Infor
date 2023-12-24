package Questao1;

public class Retangulo extends ObjetoGeometrico {
    //Herda e é aplicável o método "area" da superclasse ObjetoGeometrico para a subclasse Retangulo

    public Retangulo(double width, double height) {
        super(width, height);
    }
    
    //Poderia simplesmente acessar o método da superclasse.
    public double perimetro() {
        return 2 * width + 2 * height;
    }
}
