

public class Conta {
	private double saldo;
	int agencia;
	int numero;
	Cliente titular;
	
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
}
