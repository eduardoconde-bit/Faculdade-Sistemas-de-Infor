/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package questao4;

import java.util.Scanner;


/**
 *
 * @author eduardo
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Histograma histograma = new Histograma();
        histograma.lerCaracteres();
        System.out.println("-------------------------------");
        System.out.println("Linha 1: Caracteres");
        System.out.println("Linha 2: Número de ocorrências");
        System.out.println("-------------------------------");
        histograma.imprimeHistograma();
        System.out.println("-------------------------------");
    }
    
}
