package Questao7;

//Classe representando a Posição do "Robot".
public class Posicao {
    private int x, y;
    
    Posicao() {
        x = y = 0;
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public String retornaPosicao() {
        return "["+x+", "+y+"]";
    }
}