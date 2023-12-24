package Questao4;

public class Cd extends Media {
    public int NumFaixas;
    
    public Cd(int numFaixas, String nome, double price, String codBarras) {
        super(nome , price, codBarras);
        this.NumFaixas = numFaixas;
    }

    public void showInformation() {
        System.out.println("Informações do CD");
        super.showInformation();
        System.out.println("Número de Faixas: " + NumFaixas);
    }
}
