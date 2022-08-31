public class moto extends veiculo {

    public moto(int aluguel, String tipo) {
        super(aluguel, tipo);
    }
    
    public void testarM(String usuario) {
        System.out.println("\nUsuario" + usuario + "alugou moto");
        System.out.println("\nAluguel: " + this.aluguel + "/tipo de veiculo" + this.tipo);
    }
}
