package questao10;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

/* Declara��o da Classe Banco */
public class Banco {
	public static ArrayList<ContaCorrente> acc = new ArrayList<ContaCorrente>();
	public static Scanner entrada = new Scanner(System.in);

	/* Criando um objeto do tipo Conta */
	public static void main(String[] args) {
		int opcao;
		opcao = montaMenu();
		while (opcao != 8) {
			switch (opcao) {
				/* Cadastrar Contas */
				case 1:
					cadastrarContas();
					break;
                                        /* Ordenar Contas */
				case 2:
					encontrarConta();
					break;
                                        /* Ordenar Contas */
				case 3:
					ordenarContas();
					break;
				/* Exibir Contas */
				case 4:
					exibirContas();
					break;
				case 5:
					/* Creditar Valor */
					creditarValor();
					break;
				case 6:
					/* Debitar Valor */
					debitarValor();
					break;
				case 7:
					String conta = leiaConta();
					removerConta(obterConta(conta));
					break;
				default:
					System.out.println("Saiu do Sistema! Volte Sempre.");
			}
			limpaTela();
			opcao = montaMenu();
		}
	}

	private static void limpaTela() {
		for (int i = 0; i < 25; i++)
			System.out.println();
	}

	private static int montaMenu() {
		int opcao;
		System.out.println("1 - Cadastrar Conta");
		System.out.println("2 - Obter Conta");
		System.out.println("3 - Ordenar Contas");
		System.out.println("4 - Exibir Contas");
		System.out.println("5 - Creditar Valor");
		System.out.println("6 - Debitar Valor");
		System.out.println("7 - Remover Conta");
		System.out.println("8 - Sair");
		System.out.print("Escolha Opção: ");
		opcao = Keyboard.readInt();
		return opcao;
	}

	private static void cadastrarContas() {
		String conta = leiaConta();
		System.out.print("Digite o saldo da conta: ");
		double saldoInicial = Keyboard.readDouble();
		ContaCorrente novaConta = new ContaCorrente(conta, saldoInicial);
		adicionarConta(novaConta);
	}

	private static void adicionarConta(ContaCorrente c) {
		acc.add(c);
	}

	private static void encontrarConta() {
		String numeroConta = leiaConta();
		ContaCorrente conta = obterConta(numeroConta);
		if (conta != null) {
			System.out.println("---------------------------------------");
			System.out.println("Conta		Saldo");
			System.out.println(conta.getNumero() + "		" + conta.getSaldo());
			System.out.println("---------------------------------------");
		} else {
			System.out.println("Conta não encontrada! :( Tente novamente");
		}
		voltarMenu();
	}

	//Método que retorna uma determinada conta
	private static ContaCorrente obterConta(String numConta) {
		for (int i = 0; i < acc.size(); i++) {
			if ((acc.get(i).getNumero()).equals(numConta))
				return acc.get(i);
		}
		return null;
	}

	// Método para odernar as contas
	private static void ordenarContas() {
		Collections.sort(acc, new Comparator() {
			public int compare(Object o1, Object o2) {
				ContaCorrente conta1 = (ContaCorrente) o1;
				ContaCorrente conta2 = (ContaCorrente) o2;
				return conta1.getNumero().compareToIgnoreCase(conta2.getNumero());
			}
		});
	}

	private static void exibirContas() {
            if(acc.isEmpty()) {
                System.out.println("N�o h� contas cadastradas!");
            } else {
                for (int i = 0; i < acc.size(); i++) {
                    System.out.println("---------------------------------------");
                    System.out.println("Conta		Saldo");
                    System.out.println(acc.get(i).getNumero() + "		" + acc.get(i).getSaldo());
                    System.out.println("---------------------------------------");
                }
            }
            voltarMenu();
        }
	
	private static void creditarValor() {
		ContaCorrente conta = obterConta(leiaConta());
		if (conta != null) {
			System.out.print("Digite o valor: ");
			double valor = Keyboard.readDouble();
			conta.creditar(valor);
		} else {
			System.out.println("Conta não encontrada!");
		}
		voltarMenu();
	}

	private static void debitarValor() {
		ContaCorrente conta = obterConta(leiaConta());
		if (conta != null) {
			System.out.print("Digite o valor: ");
			double valor = Keyboard.readDouble();
			conta.debitar(valor);
		} else {
			System.out.println("Conta não encontrada!");
		}
		voltarMenu();
	}

	public static void removerConta(ContaCorrente conta) {
		if(conta != null) {
			acc.remove(conta);
			System.out.println("Conta removida com sucesso!");
		} else {
			System.out.println("Conta não encontrada! Remoção Cancelada.");
		}
		voltarMenu();
	}
        
        //Lê um numero de conta
	public static String leiaConta() {
		System.out.print("Digite o número da conta: ");
		String numeroConta = Keyboard.readWord();	
		return numeroConta;	
	}

	public static void voltarMenu() {
		System.out.print("Pressione 1 para retornar ao Menu...");
        int i = Keyboard.readInt();
	}
}