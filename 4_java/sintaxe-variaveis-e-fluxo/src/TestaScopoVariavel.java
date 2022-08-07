
public class TestaScopoVariavel {
	public static void main(String[] args) {
		System.out.println("testando condicionais");
		int idade = 18;
		int quantidadePessoas = 2;

		// boolean acompanhado = quantidadePessoas > 1;
		boolean acompanhado;
	
		if(quantidadePessoas >= 2) {
			acompanhado = true;
		}
		else {
			acompanhado = false;
		}

		if (idade >= 18 && acompanhado) {
			System.out.println("seja bem vindo");
		} else {
			System.out.println("infelizmente você não pode entrar");
		}
	}
}
