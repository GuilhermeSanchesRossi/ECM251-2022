import java.util.concurrent.ThreadLocalRandom;

public class veiculo {
    protected int id;
    protected double aluguel;
    protected String tipo;

    public veiculo (int aluguel, String tipo) {
        this.id = ThreadLocalRandom.current().nextInt(10000,99999);
        this.aluguel = aluguel;
        this.tipo = tipo;
    }

}
