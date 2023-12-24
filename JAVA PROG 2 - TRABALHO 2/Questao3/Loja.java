package Questao3;

import java.util.ArrayList;

public class Loja {
    public static void main(String[] args) {
        ArrayList<Media> produtos = new ArrayList<>();

        Livro livro1 = new Livro("Tom Riddle", "Casa de Cera", 50.00);
        Livro livro2 = new Livro("Tom Riddle", "Morte no Lago", 50.00);
        Livro livro3 = new Livro("Benjamin Franklin", "A Maior Nação do Mundo", 75.50);
        Cd cd = new Cd(10, "Led Zeppelin", 50.00);
        Dvd dvd = new Dvd("120 (Minutos)", "A casa de Cera", 200.00);

        produtos.add(livro1);
        produtos.add(livro2);
        produtos.add(livro3);
        produtos.add(cd);
        produtos.add(dvd);

        for(Media produto : produtos) {
            System.out.println("-------------------------");
            produto.showInformation();
            System.out.println("-------------------------");
        }
    }    
}
