/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package operadoreslogicos;

/**
 *
 * @author luise
 */
public class OperadoresLogicos {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) { //teste de operadores lógicos
        int idade1 = 10, idade2 = 20;
        char resp = (idade1 < idade2 ^ idade1 == 10)?'s':'n';
        System.out.println("O resultado é ``" + resp + "``");
    }
    
}
