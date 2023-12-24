package Questao4;

import java.util.ArrayList;

//Utilização das classes Cd, Dvd, Cd que herdam da classe Media 
public class Loja {
    public static void main(String[] args) {
        ArrayList<Media> produtos = new ArrayList<>();

        //Criando os Objetos
        Livro livro1 = new Livro("Tom Riddle", "Casa de Cera", 50.00, "100000");
        Livro livro2 = new Livro("Tom Riddle", "Morte no Lago", 50.00, "B3000");
        Livro livro3 = new Livro("Benjamin Franklin", "A Maior Nação do Mundo", 75.50, "R500A");
        Cd cd = new Cd(10, "Led Zeppelin", 50.00, "B5551");
        Dvd dvd = new Dvd("120 (Minutos)", "A casa de Cera", 200.00, "50022200BCA");
        //Adicionando Elementos ao ArrayList "produtos"
        produtos.add(livro1);
        produtos.add(livro2);
        produtos.add(livro3);
        produtos.add(cd);
        produtos.add(dvd);

        //Impressão do Vetor
        for(Media produto : produtos) {
            System.out.println("-------------------------");
            produto.showInformation();
            System.out.println("-------------------------");
        }

        Cd cd2 = new Cd(10, "Led Zeppelin", 50.00, "B5551");
        Cd cd3 = new Cd(10, "Led Zeppelin", 50.00, "B9991");

        produtos.add(cd2);
        produtos.add(cd3);

        //Busca por código de barras
        System.out.println();
        System.out.println("------- Busca por Código de Barras --------");
        buscaProdutoCodBarra("B5551", produtos);

        //Busca por objeto
        System.out.println();
        System.out.println("------- Busca por objeto --------");
        buscaProduto(dvd, produtos);

        //Busca por nome de Produto
        System.out.println();
        System.out.println("------- Busca por Nome --------");
        buscaProdutoNome("Casa de Cera", produtos);
    }

    public static void buscaProdutoCodBarra(String codBarra, ArrayList<Media> produtos) {
        for(Media produto : produtos) {
            if(produto.codBarras.equals(codBarra)) {
                System.out.println("Índice no Array: " + produtos.indexOf(produto));
                break;
            }
            else {
                System.out.println("O produto não foi encontrado"); 
            }
        }
    }
    
    //Método de busca por objeto!
    public static void buscaProduto(Media produto, ArrayList<Media> produtos) {
        if(produtos.contains(produto)) {
            System.out.println("Índice no Array: " + produtos.indexOf(produto));
        } else {
            System.out.println("O produto não foi encontrado");
        }
    }

    /*Método simples para nomes não iguais, poderia ser implementado com un Id do produto como 001, 1, etc...*/

    public static void buscaProdutoNome(String nome, ArrayList<Media> produtos) {
        for(Media produto : produtos) {
            if(produto.nome.toLowerCase().equals(nome.toLowerCase())) {
                System.out.println("Índice no Array: " + produtos.indexOf(produto));
                break;
            } else {
                System.out.println("Produto não encontrado");
            }
        }
    }
}