/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package questao9;

/**
 *
 * @author eduardo
 */
public class Questao9 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        for(int i = 0; i < 2; i++) {
            for(int j = 0; j < 3; j++) {
                if(i == j) {
                    continue;
                }
                System.out.println("i=" + i + " j=" + j);
            }
        }
    }
    
}
