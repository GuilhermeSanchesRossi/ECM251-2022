public class Conta {
    //Atributos da classe conta
    private int numero;
    private double saldo;

    public Conta (int numero) {
        //inicializa e instancia uma nova conta
        this.numero = numero;
        saldo = 0;
    }

    //Metodos da classe
    public void visualizarSaldo() {
        System.out.println("Saldo na conta" + numero + ": R$" + saldo);
    }

    public boolean depositar(double valor) {
        
        if(valor < 0) return false;
        this.saldo += valor;
        return true;
    }

    public boolean sacar(double valor) {

        if(valor > this.saldo) return false;
        if(valor < 0) return false;
        this.saldo -= valor;
        return true;
    }

    public boolean transferirDinheiro(double valor, Conta destino) {

        if(!sacar(valor)) return false;
        if(!destino.depositar(valor)) return false;
        return true;
    }
}
