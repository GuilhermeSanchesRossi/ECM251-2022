public class sistema {
    
    public static void iniciar(String nome) {
        bicicleta b = new bicicleta(50, "individual");
        carro c = new carro(1000, "coletivo");
        moto m = new moto(500, "individual");
        patinete p = new patinete(100, "individual");
        usuario u = new usuario(nome);
    }

    public boolean alugar(patinete p, moto m, carro c, bicicleta b, String escolha, String nome) {
        if (escolha == "patinete") {
            p.testarP(nome);
            return true;
        }
        if (escolha == "moto") {
            m.testarM(nome);
            return true;
        }
        if (escolha == "carro") {
            c.testarC(nome);
            return true;
        }
        if (escolha == "bicicleta") {
            b.testarB(nome);
            return true;
        }
    }
}
