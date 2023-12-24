package Questao3;

public class Media {
    public String nome;
    public Double price;

    public Media() {
    }

    public Media(String nome, double price) {
        this.nome = nome;
        this.price = price;
    }

    public void showInformation() {
        System.out.println("Nome: " + this.nome);
        System.out.println("Preço: R$ " + this.price);
    }
}
