/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package questao3;

/**
 *
 * @author eduardo
 */
public class Trava {
    private String quem;
    private boolean travado;
    
    public void travar(String nome, boolean condicao) {
        this.quem = nome;
        this.travado = condicao;
    }
    
    public void destravar(String nome, boolean condicao) {
        this.quem = nome;
        this.travado = condicao;
    }
    
    public boolean isTravado() {
        return this.travado;
    }
}
