package Questao2;

public class ObjetoGeometrico {
    double width, height;

    public ObjetoGeometrico() {
        this.width = this.height = 0.0;
    }

    public ObjetoGeometrico(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public ObjetoGeometrico(double x) {
        this.width = this.height = x;
    }

    void showDim() {
        System.out.printf("Width: %f\nHeight: %f\n", width, height);
    }

    double area() {
        return width * height;
    }

    double perimetro() {
        return (width + height) * 2;
    }
}
