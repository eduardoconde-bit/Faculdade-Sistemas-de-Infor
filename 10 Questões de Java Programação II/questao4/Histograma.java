/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package questao4;

import java.util.ArrayList;

/**
 *
 * @author eduardo
 */
public class Histograma {
    private static ArrayList<Character> a;
    private static ArrayList<Character> b;
    private static ArrayList<Character> c;
    private static ArrayList<Character> d;
    private static ArrayList<Character> e;
    private static ArrayList<Character> f;
    private static int contador;

    public Histograma() {
        Histograma.a = new ArrayList<>();
        Histograma.b = new ArrayList<>();
        Histograma.c = new ArrayList<>();
        Histograma.d = new ArrayList<>();
        Histograma.e = new ArrayList<>();
        Histograma.f = new ArrayList<>();
        Histograma.contador = 0;
    }
    
    public void lerCaracteres() {
        char opcao = 's';
        while(opcao == 's') {
            System.out.print("Digite um caractere (A, B, C, D, F, E): ");
            char caracter = Character.toUpperCase( Keyboard.readChar());
            switch(caracter){
                case 'A' -> {
                    a.add('A');
                    Histograma.contador++;
                }
                case 'B' -> { 
                    b.add('B');
                    Histograma.contador++;
                }
                case 'C' -> { 
                    c.add('C');
                    Histograma.contador++;
                }
                case 'D' -> { 
                    d.add('D');
                    Histograma.contador++;
                }
                case 'E' -> { 
                    e.add('E');
                    Histograma.contador++;
                }
                case 'F' -> { 
                    f.add('F');
                    Histograma.contador++;
                }
                default -> System.out.println("Caracter Inválido!");
            }
            System.out.print("(n) - Sair | (s) Continuar?: ");
            opcao = Character.toLowerCase(Keyboard.readChar());
        }
    }
    
    public void imprimeHistograma() {
        System.out.println("--- Histograma das Letras ---");
        System.out.println("A   B   C   D   E   F");
        System.out.printf("%d   %d   %d   %d   %d   %d\n", a.size(), b.size(), c.size(), d.size(), e.size(), f.size());
    }
}
