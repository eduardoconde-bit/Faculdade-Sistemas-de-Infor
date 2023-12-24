package Questao4;

public class Livro extends Media {
    String autor;

    Livro(String autor, String nome, Double price, String codBarras) {
        super(nome, price, codBarras);
        this.autor = autor;
    }

    public void showInformation() {
        System.out.println("Informações do Livro");
        super.showInformation();
        System.out.println("Autor: " + this.autor);
    }
}
