package Questao4;

public class Media {
    public String nome, codBarras;
    public Double price;

    public Media() {
    }

    public Media(String nome, double price, String codBarras) {
        this.nome = nome;
        this.price = price;
        this.codBarras = codBarras;
    }

    //toString sobrescrito (Método direto para exibir formatado os valores)
    public void showInformation() {
        System.out.println("Nome: " + this.nome);
        System.out.println("Preço: R$ " + this.price);
        System.out.println("Código de Barras: " + codBarras);
    }

    //Equals sobrescrito
    public boolean equalsCodBarras(Media produto) {
        return this.codBarras.equals(produto.codBarras);
    }
}
