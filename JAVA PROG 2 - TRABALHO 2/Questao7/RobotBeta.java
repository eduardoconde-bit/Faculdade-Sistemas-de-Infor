package Questao7;

public class RobotBeta extends RobotAbstrato{

    RobotBeta() {
    }

    RobotBeta(int x, int y) {
        super.setX(x);
        super.setY(y);
    }

    public void moveDireita(double dx, double par) {
        super.setX((int)dx);
    }

    public void moveEsquerda(double dx, double par) {
        super.setX((int)dx);
    }

    public void moveCima(double dy, double par) {
        super.setY((int)dy);
    }

    public void moveBaixo(double dy, double par) {
        super.setY((int)dy);
    }

    public void imprimePosicao() { 
        System.out.println("Robo Beta: " + super.retornaPosicao());
    }
}
