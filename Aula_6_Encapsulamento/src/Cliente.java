public class Cliente {
    private String cpf;
    private String nome;
    private String email;
    private Conta conta;

    public Cliente(String nome, String cpf, String email, Conta conta) {
        this.nome = nome;
        this.cpf = cpf; 
        this.email = email;
        this.conta = conta;
    }

    public void visualizarCliente() {
        System.out.println("Dados do cliente:");
        System.out.println("Nome do cliente: " + nome);
    }

    public String getNome() {
        //Mostra o nome na tela (get)
        return nome;
    }

    public void setNome(String nome) {
        //Armazena um nome no atributo nome da classe (set)
        this.nome = nome;      
    }

    public String getCpf(){
        return cpf;
    }

    public String getEmail(){
        return email;
    }

    public Conta getConta(){
        return conta;
    }

    public void setEmail(String email){
        this.email = email;
    }

}
