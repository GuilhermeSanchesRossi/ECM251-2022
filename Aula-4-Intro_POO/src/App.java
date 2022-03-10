public class App {
    public static void main(String[] args) {
        //Declara e instancia um objeto Caneta
        Caneta c1 = new Caneta();
        c1.iniciarCaneta("Bic", "Azul", 0.7);
        Caneta c2 = new Caneta();
        c2.iniciarCaneta("Stabillo", "Vermelha", 0.5);
        
        System.out.println("Minha caneta 1:\n" + c1.pegarDados());
        System.out.println("Minha caneta 2:\n" + c2.pegarDados());

        c1.escrever("Vai Corintia porra");
        c2.escrever("parmera bi rebaixado sem mundial");

        System.out.println("Minha caneta 1:\n" + c1.pegarDados());
        System.out.println("Minha caneta 2:\n" + c2.pegarDados());
    }
}
