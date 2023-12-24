/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package questao3;

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
        Scanner input = new Scanner(System.in);
        Trava trava = new Trava();
        
        System.out.print("Quem quer travar?: ");
        //Objeto "travado"
        trava.travar(input.nextLine(), true);
        //Retorno do estado do objeto
        System.out.println("O objeto encontra-se travado?: " + trava.isTravado());
    }
    
}
