public class PassagemValor {

    public static void alterarNumero(int x) {
        System.out.println("Dentro do método, antes da alteração: " + x);

        x = 100;

        System.out.println("Dentro do método, depois da alteração: " + x);
    }

    public static void main(String[] args) {

        int numero = 10;

        System.out.println("No main, antes da chamada: " + numero);

        alterarNumero(numero);

        System.out.println("No main, depois da chamada: " + numero);
    }
}
