package Questao3;

public class Dvd extends Media {
    public String duration;

    public Dvd(String duration, String nome, Double price) {
        super(nome, price);
        this.duration = duration;
    }

    public void showInformation() {
        System.out.println("Informações do DVD");
        super.showInformation();
        System.out.println("Duração: " + duration);
    }
}
