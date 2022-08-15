
public class TestaBanco {
	
	public static void main(String[] args) {
		Cliente clientePaulo = new Cliente();
		clientePaulo.nome = "paulo silveira";
		
		
		Conta contaPaulo = new Conta ();
		contaPaulo.titular = clientePaulo;
		
		System.out.println(contaPaulo.titular.nome);
		
		Conta contaMarcela = new Conta();
		contaMarcela.titular = new Cliente();
		
		contaMarcela.deposita(150);
		System.out.println(contaMarcela.getSaldo());
	
	}

}
