public class carro extends veiculo {

    public carro(double aluguel, String tipo) {
        super(aluguel, tipo);
    }
    
    public void testarC(String usuario) {
        System.out.println("\nUsuario" + usuario + "alugou carro");
        System.out.println("\nAluguel: " + this.aluguel + "/tipo de veiculo" + this.tipo);
    }
}
