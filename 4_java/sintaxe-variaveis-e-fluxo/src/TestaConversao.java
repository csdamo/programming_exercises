
public class TestaConversao {
	
	public static void main(String[] args) {
		double salario = 2500.60;
		// int valor = salario; // n�o compila
		
		int valor = (int)salario;
		
		System.out.println(valor);
		
	}
}
