package Questao7;

public class Teste {
    public static void main(String[] args) {
        RobotAlfa robotAlfa = new RobotAlfa(0, 0);
        RobotBeta robotBeta = new RobotBeta(1, 1);
        
        System.out.println("Antes das movimentações");
        robotAlfa.imprimePosicao();
        robotBeta.imprimePosicao();

        //Movimentos
        robotAlfa.moveBaixo(-20, 2);
        robotBeta.moveDireita(10, 1);
        robotAlfa.moveEsquerda(30, 1);
        robotBeta.moveCima(5, 1);

        System.out.println("Depois das movimentações");
        robotAlfa.imprimePosicao();
        robotBeta.imprimePosicao();
    }
}
