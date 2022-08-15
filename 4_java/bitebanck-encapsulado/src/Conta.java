

public class Conta {
	private double saldo;
	private int agencia;
	private int numero;
	private Cliente titular;
	private static int totalContas;
	
	public Conta(int agencia, int numero){
	    this.agencia = agencia;
	    this.numero = numero;
	    this.saldo = 100; //isso significa que toda conta começa com 100 de saldo.
	    System.out.println("Estou criando uma conta");
	}

	public void deposita(double valor) {
		this.saldo += valor;
	}
	
	public boolean saca(double valor) {
		boolean conseguiuSacar = false;
		if(this.saldo >= valor) {
			this.saldo -= valor;
			conseguiuSacar = true;
		}
		return conseguiuSacar;
	}
	
	public boolean transfere(double valor, Conta contaDestino) {
		if(this.saldo >= valor) {
			this.saldo -= valor;
			contaDestino.deposita(valor);
			return true;
		}
		return false;
	}

	public double getSaldo() {
		return this.saldo;		
	}
	
	public int getNumero() {
		return numero;
	}

	public void setNumero(int numero) {
		this.numero = numero;
	}
	
	public int getAgencia() {
		return agencia;
	}
	
	public void setAgencia(int agencia) {
		this.agencia = agencia;
	}
	
	public Cliente getTitular() {
		return titular;
	}
	
	public void setTitular(Cliente titular) {
		this.titular = titular;
	}


	public static int getTotalContas() {
		return totalContas;
	}

}
