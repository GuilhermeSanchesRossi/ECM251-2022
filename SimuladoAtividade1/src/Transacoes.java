//Guilherme Sanches Rossi RA19.02404-5

public class Transacoes {
    public String gerarQRCode(Usuario recebedor, Conta pagador, double valor) {
        return pagador.idConta + ";" + recebedor.nome + ";" + valor;
    }

    public void destrincharQRCode() {
        
    }
}