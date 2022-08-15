package bytebank;

public class TesteReferencia {
	public static void main(String[] args) {
		Conta conta1 = new Conta();
		System.out.println(conta1.saldo);
		
		Conta conta2 = conta1;
		System.out.println(conta2);
		
		if(conta1 == conta2) {
			System.out.println("mesma conta");
		}else {
			System.out.println("não são iguais");
		}
		
	}
}
