/*
$(document).ready(runProfile); // Executa a função runProfile quando o DOM está totalmente carregado

// Monitora mudanças no estado de autenticação do usuário
firebase.auth().onAuthStateChanged((user) => {
    // Verifica se o usuário está logado
    if (user) {
        // Se o usuário estiver logado, atualiza as informações de exibição
        $('#logged img').attr({
            'src': user.photoURL, // Define a imagem do perfil do usuário
            'alt': user.displayName // Define o nome de exibição como texto alternativo da imagem
        });

        $('#logged h4').html(user.displayName); // Atualiza o nome do usuário
        $('#id').html('ID: ' + user.uid); // Exibe o ID do usuário
        $('#email').html('E-mail: ' + user.email); // Exibe o e-mail do usuário
        $('#registered').html('Cadastrado em ' + dateConvert(user.metadata.creationTime)); // Exibe a data de cadastro
        $('#lastLogin').html('Último login em ' + dateConvert(user.metadata.lastSignInTime)); // Exibe a data do último login

        $('#notLogged').hide(); // Esconde a seção para usuários não logados
        $('#logged').show(); // Mostra a seção com informações do usuário logado
    } else {
        // Se não houver um usuário logado
        $('#logged').hide(); // Esconde a seção de usuário logado
        $('#notLogged').show(); // Mostra a seção para usuários não logados
    }
});

// Função para inicializar interações na página
function runProfile() {
    // Ao clicar no botão, abre a conta do Google em uma nova aba
    $('#toGoogle').click(() => {
        window.open('https://myaccount.google.com/', '_blank');
    });

    // Define ações para os botões de logout e login
    $('#btnLogout').click(logout); // Chama a função logout ao clicar no botão
    $('#btnLogin').click(login); // Chama a função login ao clicar no botão
};

// Função que converte uma data para o formato 'dd/mm/aaaa'
function dateConvert(date) {
    // Cria um novo objeto Date a partir da string de data fornecida
    const dateObj = new Date(date);

    // Obtém o dia do mês (1-31) e formata para dois dígitos
    const day = dateObj.getDate().toString().padStart(2, '0');
    
    // Obtém o mês (0-11), adiciona 1 para ajustar ao formato (1-12) e formata para dois dígitos
    const month = (dateObj.getMonth() + 1).toString().padStart(2, '0');
    
    // Obtém o ano completo (ex: 2024)
    const year = dateObj.getFullYear();

    // Formata a data no padrão 'dd/mm/aaaa'
    const formattedDate = `${day}/${month}/${year}`;
    
    // Retorna a data formatada
    return formattedDate;
};
*/


$(document).ready(runProfile); // Executa a função runProfile após o DOM estar pronto

// Monitora o estado de autenticação do usuário
firebase.auth().onAuthStateChanged(user => {
    const $logged = $('#logged'); // Seleciona o elemento que exibe informações do usuário logado
    const $notLogged = $('#notLogged'); // Seleciona o elemento que exibe informações para usuários não logados

    if (user) {
        // Atualiza as informações do usuário se ele estiver logado
        $logged.find('img').attr({
            'src': user.photoURL, // Define a foto do usuário
            'alt': user.displayName // Define o nome de exibição como texto alternativo
        });
        $logged.find('h4').text(user.displayName); // Exibe o nome do usuário
        $logged.find('#id').text('ID: ' + user.uid); // Exibe o ID do usuário
        $logged.find('#email').text('E-mail: ' + user.email); // Exibe o e-mail do usuário
        $logged.find('#registered').text('Cadastrado em ' + dateConvert(user.metadata.creationTime)); // Data de cadastro
        $logged.find('#lastLogin').text('Último login em ' + dateConvert(user.metadata.lastSignInTime)); // Último login

        $notLogged.hide(); // Esconde a seção para não logados
        $logged.show(); // Mostra a seção de usuário logado
    } else {
        // Caso não haja um usuário logado
        $logged.hide(); // Esconde a seção de usuário logado
        $notLogged.show(); // Mostra a seção para não logados
    }
});

// Função que inicializa interações na página
function runProfile() {
    // Abre o link da conta do Google em uma nova aba
    $('#toGoogle').click(() => window.open('https://myaccount.google.com/', '_blank'));
    
    $('#btnLogout').click(logout); // Define a ação de logout ao clicar no botão
    $('#btnLogin').click(login); // Define a ação de login ao clicar no botão
}

// Função que converte a data para o formato 'dd/mm/aaaa'
function dateConvert(date) {
    const dateObj = new Date(date); // Cria um novo objeto Date a partir da string de data
    const day = String(dateObj.getDate()).padStart(2, '0'); // Obtém e formata o dia
    const month = String(dateObj.getMonth() + 1).padStart(2, '0'); // Obtém e formata o mês (ajusta para 1-12)
    const year = dateObj.getFullYear(); // Obtém o ano completo
    
    // Retorna a data formatada
    return `${day}/${month}/${year}`;
}

/*
Comentários sobre as funções:

    Estrutura Geral: O código usa jQuery para manipular o DOM e Firebase para autenticação, garantindo que a interface reaja de forma dinâmica ao estado do usuário.

    onAuthStateChanged: Este método é fundamental para monitorar a autenticação do usuário e atualizar a interface automaticamente quando o estado muda.

    Função runProfile: Centraliza a lógica de inicialização e interação, separando claramente a configuração de eventos dos outros processos.

    dateConvert: Uma função utilitária que formata datas de forma amigável para o usuário, garantindo que a apresentação seja consistente.

}
*/