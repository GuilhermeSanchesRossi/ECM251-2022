public class patinete extends veiculo {
 
    public patinete(int aluguel, String tipo) {
        super(aluguel, tipo);
    }

    public void testarP(String usuario) {
        System.out.println("\nUsuario" + usuario + "alugou patinete");
        System.out.println("\nAluguel: " + this.aluguel + "/tipo de veiculo" + this.tipo);
    }
}
