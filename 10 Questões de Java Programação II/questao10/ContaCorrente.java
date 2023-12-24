package questao10;

/* Declaração da Classe ContaCorrente */
class ContaCorrente{
   private String numero;
   private double saldo;

   /* Construtor da Classe Conta */
   public ContaCorrente (String n, double s){
      numero = n; 
      saldo = s;
   }

   /* Método para Creditar na Conta */
   public void creditar (double valor){
      saldo = saldo + valor;
   }

   /* Método para Debitar na Conta */
   public void debitar (double valor){
      saldo = saldo - valor;
   }

   /* Método para retornar o Número da Conta */
   public String getNumero(){
      return numero;
   }

   /* Método para retornar o Saldo da Conta */
   public double getSaldo(){
      return saldo;
   }

   /* Método para atribuir o Número da Conta */
   public void setNumero(String n){
      numero = n;
   }

   /* Método para atribuir o Saldo da Conta */
   public void setSaldo(double s){
      saldo = s;
   }

}