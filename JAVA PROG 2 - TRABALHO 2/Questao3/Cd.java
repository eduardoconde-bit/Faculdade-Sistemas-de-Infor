package Questao3;

public class Cd extends Media {
    public int NumFaixas;
    
    public Cd(int numFaixas, String nome, double price) {
        super(nome ,price);
        this.NumFaixas = numFaixas;
    }

    public void showInformation() {
        System.out.println("Informações do CD");
        super.showInformation();
        System.out.println("Número de Faixas: " + NumFaixas);
    }
}
