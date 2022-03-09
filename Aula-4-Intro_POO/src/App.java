public class App {
    public static void main(String[] args) {
        //Declara e instancia um objeto Caneta
        Caneta c1 = new Caneta();
        c1.modelo = "Bic";
        c1.cor = "Azul";
        c1.carga = 100;
        c1.ponta = 0.7;
        System.out.println("Minha caneta" + "\n" + c1.modelo + "\n" + c1.cor + "\n" + c1.carga + "\n" + c1.ponta);
    }
}
