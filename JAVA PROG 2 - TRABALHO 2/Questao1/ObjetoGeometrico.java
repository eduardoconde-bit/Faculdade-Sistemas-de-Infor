package Questao1;

public class ObjetoGeometrico {
    public double width, height;

    public ObjetoGeometrico(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public void showDim() {
        System.out.printf("Width: %f\nHeight: %f\n", width, height);
    }

    public double area() {
        return width * height;
    }

    public double perimetro() {
        return (width + height) * 2;
    }
}
