
public class TesteGetterSetter {
	public static void main(String[] args) {
		Conta conta = new Conta(142, 65);

		conta.deposita(100.0);

		double valorSaque = 50.0;
		conta.saca(valorSaque);

		double valorDeposito = 70.0;
		conta.deposita(valorDeposito);
	}

}
