/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package questao6;

/**
 *
 * @author eduardo
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int opcao;
        NumeroComplexo numComplex1 = new NumeroComplexo();
        numComplex1.inicializaNumero(2, 3);
        NumeroComplexo numComplex2 = new NumeroComplexo();
        numComplex2.inicializaNumero(1, -4);
        
        System.out.println("----------------------------------------------");
        numComplex1.imprimeNumero();
        numComplex2.imprimeNumero();
        System.out.println("-------------------------------------------");
        // Compara se o numeroComplex1 é igual ao segundo
        System.out.println("O número complexo 1 é igual ao segundo?: " + numComplex1.eIgual(numComplex2));
        System.out.println("-------------------------------------------");

        opcao = menu();
        switch (opcao) {
            case 1:
                numComplex1.somar(numComplex2);
                numComplex1.imprimeNumero();
                break;
            case 2:
                numComplex1.subtrair(numComplex2);
                numComplex1.imprimeNumero();
                break;
            case 3:
                numComplex1.multiplicar(numComplex2);
                numComplex1.imprimeNumero();
                break;
            case 4:
                numComplex1.dividir(numComplex2);
                break;
            default:
                System.out.println("opção inválida!");
        }
    }

    // Cria um menu interativo!
    public static int menu() {
        System.out.println("------------------------------------------------");
        System.out.println("1 - somar | 2 - Subtrair | 3 Multiplicar | 4 - Dividir");
        System.out.print("Escolha sua opção: ");
        int opcao = Keyboard.readInt();
        return opcao;
    }
}
