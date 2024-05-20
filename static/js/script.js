// Função para gerar dados aleatórios

function geradorDados() {
    console.log("Hello World");
    // Lista de dados
    const nome = [
        "Alice",
        "Alan",
        "Bianca",
        "Carol",
        "Daniel",
        "Felipe",
        "Joana",
        "Nathalia",
        "Thiago",
        "Pedro",
    ];
    const sobrenome = [
        "Almeida",
        "Barbosa",
        "Carvalho",
        "Gomes",
        "Herrero",
        "Martins",
        "Oliveira",
        "Rocha",
        "Rodrigues",
        "Sagrado",
    ];
    const cpf = [
        "012.345.678-90",
        "123.456.789-01",
        "234.567.890-12",
        "345.678.901-23",
        "456.789.012-34",
        "567.890.123-45",
        "678.901.234-56",
        "789.012.345-67",
        "890.123.456-78",
        "901.234.567-89",
    ];
    const dominio = ["@example.com", "@gmail.com", "@company.com"];

    // Gerador de dados
    const nomeAleatorio = nome[Math.floor(Math.random() * nome.length)];
    const sobrenomeAleatorio =
        sobrenome[Math.floor(Math.random() * sobrenome.length)];
    const cpfAleatorio = cpf[Math.floor(Math.random() * cpf.length)];
    const dominioAleatorio =
        dominio[Math.floor(Math.random() * dominio.length)];
    const emailAleatorio =
        nomeAleatorio.toLowerCase() +
        "_" +
        sobrenomeAleatorio.toLowerCase() +
        dominioAleatorio;

    // Preenchendo os campos com os dados gerados
    document.getElementById("id_nome").value = nomeAleatorio;
    document.getElementById("id_sobrenome").value = sobrenomeAleatorio;
    document.getElementById("id_cpf").value = cpfAleatorio;
    document.getElementById("id_email_funcional").value = emailAleatorio;
}
