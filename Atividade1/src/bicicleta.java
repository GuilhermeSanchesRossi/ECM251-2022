public class bicicleta extends veiculo {

    public bicicleta(int aluguel, String tipo) {
        super(aluguel, tipo);
    }
    
    public void testarB(String usuario) {
        System.out.println("\nUsuario" + usuario + "alugou bicicleta");
        System.out.println("\nAluguel: " + this.aluguel + "/tipo de veiculo" + this.tipo);
    }
}
