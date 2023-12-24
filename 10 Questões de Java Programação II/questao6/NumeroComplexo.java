/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package questao6;

/**
 *
 * @author eduardo
 */
public class NumeroComplexo {
    // 'r' == parte real, 'i' == parte imaginária
    private double r, i;

    public void inicializaNumero(double real, double imaginaria) {
        this.setR(real);
        this.setI(imaginaria);
    }

    // Imprime o número complexo
    public void imprimeNumero() {
        System.out.printf("Número Complexo: %.1f + %.1f i\n", this.getR(), this.getI());
    }

    // Retorna a parte real do número complexo
    public double getR() {
        return this.r;
    }

    // Retorna a parte imaginária do numero complexo
    public double getI() {
        return this.i;
    }

    //Seta um valor em r
    public void setR(double r) {
        this.r = r;
    }

    //Seta um valor em i
    public void setI(double i) {
        this.i = i;
    }

    // Compara se o objeto NumeroComplexo é igual a outro NumeroComplexo.
    public boolean eIgual(NumeroComplexo num) {
        return this.i == num.getR() && this.i == num.getI();
    }

    // Executa a soma dos números complexos
    public void somar(NumeroComplexo num) {
        //(a+bi)+(c+di) = (a+c)+(b+d)i;

        this.r += num.getR(); //(a + c)
        this.i += num.getI(); //(b + d) * i
    }

    // Executa a subtração dos números complexos
    public void subtrair(NumeroComplexo num) {
        //(a+bi)-(c+di) = (a-c)+(b-d)i

        this.r -= num.getR(); // (a - c)
        this.i -= num.getI(); // (b - d) * -1
    }

    // Multiplica um número complexo por outro
    public void multiplicar(NumeroComplexo num) {
        double parteR; //Parte real e irracional respectivamente
        double parteI;

        //(a+bi)+(c+di) = (ac-bd)+(ad+bc)i;
        parteR = (this.r * num.getR() - this.i * num.getI());
        parteI = (this.r * num.getI() + this.i * num.getR());
        //Usos dos setters para definir os valores dos atributos da classe
        this.setR(parteR);
        this.setI(parteI);
    }

    // Divide um número complexo por outro
    public void dividir(NumeroComplexo num) {
        double parteR;
        double parteI; 

        // (a+bi)/(c+di) = (ac+bd)/(c²+d²) + ((bc-ad)/(c²+d²))* i
        parteR = (this.r * num.getR() + this.i * num.getI()) / (Math.pow(this.r, 2) + Math.pow(num.getI(), 2) ); //(ac+bd)/(c²+d²)

        parteI = ((this.i * num.getR() - this.r * num.getI()) / (Math.pow(this.r, 2) + Math.pow(num.getI(), 2)) ) * -1; //((bc-ad)/(c²+d²))* i

        this.r = parteR;
        this.i = parteI;
        imprimeNumero();
    }
}
